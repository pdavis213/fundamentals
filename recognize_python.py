# variable declaration interger
num1 = 42
# variable declaration float
num2 = 2.3
# variable declaration boolean
boolean = True
# variable declaration interger string
string = 'Hello World'
# variable declaration composite list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration composite dictionary
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
# variable declaration tuple
fruit = ('blueberry', 'strawberry', 'banana')
# log statement object type check
print(type(fruit))
# log statement object list access value
print(pizza_toppings[1])
# log statement list change value
pizza_toppings.append('Mushrooms')
# log statement tuple initialize
print(person['name'])
# composite dictionary list initialize vlaue
person['name'] = 'George'
# composite dictionary list initialize vlaue
person['eye_color'] = 'blue'
# composite log statment tuple
print(fruit[2])

#! Conditional if else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#! condtional if else if else if
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#! for loop
for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
#! while loop
while(x < 5):
    print(x)
    #! increment
    x += 1

#! composite list delete value
pizza_toppings.pop()
#! composite list delete integer value
pizza_toppings.pop(1)

#! log statment
print(person)
#! deleve vale
person.pop('eye_color')
#! log statment
print(person)

#! for loop
for topping in pizza_toppings:
    #! if statement conditional is true
    if topping == 'Pepperoni':
        continue
        #! log statment
    print('After 1st if statement')
    #! if statement conditional is true
    if topping == 'Olives':
        #! break loop
        break

#! function declaration


def print_hello_ten_times():
    #! for loop, paramater range
    for num in range(10):
        #! log statment
        print('Hello')


#! call to the function defined above
print_hello_ten_times()

#! function declaration


def print_hello_x_times(x):
    #! for loop considering argument
    for num in range(x):
        #! log statment
        print('Hello')


#! call to the function above passing argument 4
print_hello_x_times(4)

#! function declaration


def print_hello_x_or_ten_times(x=10):
    #! for loop range declaration
    for num in range(x):
        #! log statment
        print('Hello')


#! call function taking in defined parameter
print_hello_x_or_ten_times()
#! call function passing argument to function
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
