#stings in python
#Date:22/2/2024
#Name:Jane

city = "nairobi"

#convert to  uppercase
print(city[0])#prints n
print(city[1])#prints a
print(city[2])#prints i
print(city[3])#prints r
print(city[4])#prints o
print(city[5])#prints b
print(city[6])#prints i

print(city[-1])#prints reverse starting with i
print(city[-2])#prints reverse starting with b

#replacing a character
fruit= "OrangeOOOO"

print(fruit.replace("O" ,"Y"))

SUBJECT ="Phyical :Sciences"
print(SUBJECT.split(":"))



print("\n") #prints a new line
print(city.upper())
name ="JANE"
print(name)
print(name.lower()) # converts strings to lower case

town = "   Naivasha   "
print(town)
print("\t") # new tab
print(town.strip())# strip removes spacing

#add  two strings

f_name = "Jane"
s_name = "Njeri"
full_name =f_name + s_name


print(full_name)
age  =30
height = 1.2
print("I am age{0} years old and {1}meters tall".format(age,height))

activity ="dancing"
print("My hobby is %s"%(activity)) #printing a string %s


height = 1.23490999 
print("My height is %5.3f"%(height)) #printing a  float %f

age =32
print("My age is %d"%(age)) # printing an interger %d
#printing character %c




name = "Jane Njeri"
print(len(name))# Gives number of characters in the string
#str
print (f"My full name|{name}")

school ="Engeering"
course = "Electrical"

print("I am studying {course} in the school of {school} ". format(course="Medicine",school ="Human sciences"))
