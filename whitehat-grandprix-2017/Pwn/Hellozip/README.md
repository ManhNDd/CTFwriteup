* Writeup for hellozip

** Vulnerability

The call to memcpy() inside print_entry copies a potentially large file name to a small buffer in the stack -> stack-based buffer overflow without canary enabled.

** Exploitation

This challenge is designed to be exploited offline, so there are 2 intended solutions:
(note: PIE & canary are off)

- build a ROP chain to mmap() our input file to memory to a specified address, with PROT_EXECUTE enabled (might be harder)

- build a ROP chain with given map_input_file() function to a specified address, do a memcpy() linkmap data from input file to .bss (the binary won't check zip data integrity), then perform return-to-dlresolve
