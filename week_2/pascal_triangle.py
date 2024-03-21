# pascal's triangle
#Date:22/2/2024
# Name:Jane

from math import factorial

rows = int(input("enter the nuimber of rows : "))
for n  in range(rows):
   for space in range(1,rows - n):
     print(end = " ")

   for r in range (n+1):
      ncr=factorial(n) // (factorial(r) * factorial(n-r))
      print(ncr, end= " ")

      print(" ")