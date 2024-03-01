# a block of code running together as a unit
# firdt intialise a function-use a key word (def)
#then call the function
#two types -user defined in built 


#define afunction
def print_name():
    print("My name is Jane Gitata")

#calling the function one can call a function as many times as possible
print_name()

def print_details(name,age,Id,gender):#has parameters
    print("I am {0},{1} years old.My Id no is {2} and my gender is {3}".format(name,age,Id,gender))


print_details("Jane","17","35322697","female")
print_details("Lucy","59","3452687218","female")


#sum of  numbers
def sum_nums (x,y):
    return x + y

z =sum_nums(10,20)
print (z)

#products of numbers
def prod_nums(x,y):
    return(x*y) #how to return a function
print(prod_nums(5,6))
print(prod_nums(5,16))

#for loop inside the function
def  print_odds(first_no,last_no):
    for i in range (first_no,last_no):
        print(i)
print_odds(0,15)

