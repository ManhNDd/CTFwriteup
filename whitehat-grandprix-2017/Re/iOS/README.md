The binary is a iOS machO.

The key to decryption is obfuscated. There are 2 ways to solve this challenge:

1. Static: deobfuscate the key (very difficult and time consuming)

2. Dynamic: Install Xcode on Mac (or MacVM), with iphone simulator. Install the app in blank project and debug using IDA, this requires specific understanding of reverse engineering.

* Hook using frida / or Debug with IDA (will be slow) we got the deobfuscated key: "--whitehat2017--"

However, this is not the final key to decrypt the hardcoded AES256 (in base64 encoded). Look at the xref to cfg key we see there's a calling hierachy from ReceiveMemoryWarning (when app running in low memory circumstance). We can simulate this in XCode, or read the static code in didReceiveMemoryWarning which actually doubles the input string.

-> org key = "--whitehat2017----whitehat2017--"

which gave us the decrypted flag: WhiteHat{13752bdddca3eebb230dcd490d4bd574acdd94eecda428d7b5a640068fcdc110}

