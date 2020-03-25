#Ex 1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

ini = 2000
fin = 3200
resultado = []
for i in range(ini, fin+1):
  if (i mod 7 == 0) and (i mod 5 !=0):
    resultado.append(i)

for num in resultado:
  print("%s," % num, end="")
