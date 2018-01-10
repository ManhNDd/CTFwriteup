Challenge: `color_blend.png`

Solution:

- Open file with a hex editor. At the end of the file you see (password): `hello_vn`.

- Read the color of the overlapped area of two squares. (R, G, B) are printable ascii value. For example, (52, 100, 109) is ('4', 'd', 'm').

- Join these then we get `aes_encrypt.py` and decrypted flag.

- Use password hello_vn to decrypt it and get flag.