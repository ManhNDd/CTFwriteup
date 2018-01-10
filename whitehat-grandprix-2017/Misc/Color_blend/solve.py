from PIL import Image
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:

    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:])).decode('utf8')

		
im = Image.open("color_blend.png")
pix = im.load()
import string
s=""		

for x in range(26, im.size[0], 52):
	for y in range(26, im.size[1], 52):
		colors = str(pix[x,y]).replace("(","")
		colors = colors.replace(")", "")
		colors = colors.replace(" ", "")
		colors = colors.split(",")
		for i in colors[::-1]:
			if chr(int(i)) in string.printable:
				s=s+chr(int(i))

enc = s.split("#")[1].strip()
print AESCipher("hello_vn").decrypt(enc)