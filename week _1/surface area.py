#Program is used to solve for the surface area of figures
#Date:21/2/2024
#Name:Jane
p=22/7
d= float(input ( "the diameter of cylinder is"))
h= float(input ( "the height of cylinder is"))
r= float(input ( "the radius of cylinder is"))
s = (p*d*h)+(p*(r**2))
print("surface area of cylinder is",s)

p =22/7
r= float(input ( "the radius of sphere is"))
s = 4*p*r**2
print("surface area of sphere is",s)