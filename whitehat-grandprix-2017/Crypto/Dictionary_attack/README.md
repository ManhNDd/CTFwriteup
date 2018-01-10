It's a block shuffle puzzle

evil minds captured flags

tester d
evil min <-- 
 test ba
ds captu <--
re test 
red flag <--
ship hat
s 		 <--

Encrypt "tester devil min test bads capture test red flagship hats", we got:

k1drRqxEI3QVbnH57TujzYo5fLxH2ORmSyGTVd3iSOqgoMbRax8XR+CFDYjNijkbKEJGOJGfIBEH 0d3t2HNj/g== 

x= "k1drRqxEI3QVbnH57TujzYo5fLxH2ORmSyGTVd3iSOqgoMbRax8XR+CFDYjNijkbKEJGOJGfIBEH0d3t2HNj/g== "
x= x.decode('base64')
print ''.join([x[i:i+8] for i in range(8,len(x),16)]).encode('base64').replace('\n','')

-> Submit "FW5x+e07o81LIZNV3eJI6uCFDYjNijkbB9Hd7dhzY/4=" got flag