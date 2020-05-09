import base64
import sys
from base64 import *

with open(sys.argv[1],'r') as my_file:
        data = my_file.read()

for i in range (0,5):
        data = base64.b16decode(data)

print(data) 
my_file.close()
