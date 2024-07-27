from hashlib import sha3_256
import os
lis = []
for file in os.listdir('task2'):
  f = open("task2/"+file,"rb")
  lis.append(sha3_256(f.read()).hexdigest())
lis = sorted(lis)
fina = ''.join(lis) + ''
fina = fina.encode()
print(sha3_256(fina).hexdigest())