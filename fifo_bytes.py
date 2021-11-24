# as well as plain text, we have 'byte' data
b = bytes( range(0,256) ) # 0 to 255 inclusive
# print(b)

# we can write and read bytes to exeternal files
fout = open('bfile', 'wb') # 'wb' will (over)write bytes
fout.write(b)
fout.close()

# read back in again
fin = open('bfile', 'rb') # read bytes (can also use 'x' for exclusive and 'a' for append)
r = fin.read()

print(r)
