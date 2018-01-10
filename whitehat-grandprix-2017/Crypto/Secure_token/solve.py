# solve.py
import sys
import string
# sys.path.append("D:\\VietAnh\CTF\\bearctf\\crypto300")
from netcat import Netcat
if sys.argv[1] == 'local':
    host = 'localhost'
else:
    host = sys.argv[2]
port = 3333
block_size = 16*2
size = 48*2
characters = string.lowercase+string.digits+'"'
base_c = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
base_x = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "flag": "'
guess_x = ""
print guess_x
def block(s):
	return [s[x:x+32] for x in range(0, len(s), 32)]
def encrypt(msg):
	nc = Netcat(host, port)
	nc.read(1024)
	nc.read(1024)
	nc.write(msg.encode('hex')+'\n')
	data = nc.read(1024)
	nc.read(1024)
	nc.write('n')
	nc.close()
	# print block(data[12:])
	return data[12:]
def encrypt2(msg):
	nc = Netcat(host, port)
	nc.read_until('\n')
	nc.read_until('\n')
	# print "[1]", nc.read_until('\n')
	# print "[2]", nc.read_until('\n')
	nc.write(msg.encode('hex')+'\n')
	print msg#.encode('hex')
	data = nc.read_until('\n').strip()
	# print "[+]", data
	nc.read_until('\n')
	# print "[3]", nc.read_until('\n')
	nc.write('n\n')
	nc.close()
	# print block(data[12:])
	return data[12:]

# import hashlib
# print hashlib.md5('vietanhvodoi').hexdigest()
# print block(encrypt('xxxxxxxxxx"xxxxxxxxxxxxxxxx'))
# print block(encrypt('xxxxxxxxxx"xxxxxxxxxxxxxxxx, "flag:"aa6d6d1'))
# print block(encrypt('xxxxxxxxxxxxxxxxxxxxxxxx'))
# print block(encrypt('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'))
# 			# {"a": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "flag": "aa6d6d161485abaa74cb5516bccde55d"}
# print block(encrypt('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "flag": "aa6d6d161485abaa74cb5516bccde55d'))

# exit(1)

def oracle(c, x, pos):
	s = encrypt2(base_x[pos:]+c)
	print s#[size:size+block_size]
	print x
	return s[size:size+block_size] == x

def guess_xpost(pos):
	base_cipher = encrypt2(base_c[pos:])[size:size+block_size]
	for c in characters:
		print c
		if oracle(guess_x+c, base_cipher, pos):
			return c
	return ''

# def main(guess_x):
i = 0
import time
t = time.time()
while True:
	g = guess_xpost(i)
	if len(g) == 0:
		print "[!] Error!"
		break
	elif g == '"':
		print "[+] Complete, secret is:", guess_x
		break
	else:
		guess_x+=g
		i+=1
		print "[+] Found!", g, guess_x
print "[+] Done in", time.time()-t, "s"

# for i in xrange(100):
# 	encrypt2('aa')
# if __name__ == '__main__':
	# encrypt2('aa')
	# main(guess_x)
