#Friends
friends = ["Yvonne","Patty","Grace","Sipai","Mercy"]

for friend in friends:
    print(friend)


enemies = friends[:]#to copy one list into another
#enemies = enemies.append("Mark")
for enemy in enemies:
    print(enemy)

fruits=("guava","Strawberry","Mango","Lemon","pineapple")
#slice the list to get part of the list

print(fruits[0:3])

print(fruits)
squares =[]#intialises an empty list
for x in range (0,11):
    squares.append(x**2)
print(squares)