#Let's learn about lists in Python. 
#In variables, we can store a single values

#so, how can we store multiple values in a single variable?
#We can use lists to store multiple values in a single variable.

#For example, we can create a list of fruits like this:
fruits = ["apple", "banana", "orange", "grape"]

print(fruits) 

#one thing to remember in the list the order of the values is important 
#we also inlucde the numbers in the list

numbers = [2, 4, 5, 6, 7, 8]
print(numbers)

#We can also have a list with mixed data types

mixed_list = ["apple", 1.0, 2, "banana", True]
print(mixed_list)

#We use square brackets [] and elements are separated by comma 

#Now, let's learn how to access the elements in the list 
#@3 can access the elment by using the index. Remember, index always starts with 0

print(fruits[0])
print(numbers[1])
print(mixed_list[2])

#For exxample, you want to access last element in the list?
#There are two ways to do access the last element?
#First - Find the length of the list and access the last element 

print("The length of mixed_list is ", len(mixed_list)) #Length is 5,but the last element position is 4 (index start with 0)
print(mixed_list[4])

#Second way is to use the negative index -1 to access the last element, -2 to access the second last element and so on.
print(mixed_list[-1]) #Output - True

#Similiarly, we can access the second last element using -2 index
print(mixed_list[-2]) #Output - "banana"


#Practice 

my_friends= [ "Ramesh", "Rajesh", "Suresh", "Mahesh"]
print(my_friends)
print(my_friends[0])
print(my_friends[3])
print(my_friends[-2])

greeting = "Happy Birthday to you my dear friend."
print(my_friends[0] + ", " + greeting)
print(my_friends[-2] + "," + greeting + " " + "Have a great year ahead!")
           
#So far looks good, you are able to create a list with different data types 
#Such as strings, numbers, floats and boolean values. 

#So can you do any modifications to the existing list?
     #Like 
        #added a new element 
        #change the existing elememt 
        # remove an element from the list. 

#Let's say super market has a list of fruits and they want to add a new fruit to the list, how can they do that?
list_of_fruits = ["apple", "banana", "orange", "grape", "grapes"]
print(list_of_fruits)

#now, we want to add a two new fruits to the list. 
#How do we do it? - Remember, this is an action right, so whenever we want to do an action, we will use a function right?

#so here we use the function called append() to add a new element to the list 

list_of_fruits.append("mango")
list_of_fruits.append("kiwi")
print(list_of_fruits)

#Two things to remember here - for function, we use parenthesis ()
#In parenthesis, we pass the element value and it will take only one element at a time 
#This is how we can add a new element to the existing list and new elemets are added at the end of the list. 

#Now, how can we change the existing element in the list?

#['apple', 'banana', 'orange', 'grape', 'grapes', 'mango', 'kiwi']
list_of_fruits[2] = "strawberry" #Replacing the orange with strawberry
print(list_of_fruits)

users = [] #This is an empty list

users.append("Alex")
users.append("Bob")
users.append("Charlie")
users.append("David")
users.append("Eva")
print(users)

#another wway to instet a new element, by using insert() function

#users.insert("Frank") #TypeError: insert expected 2 arguments, got 1

#so insert() function takes two arguments - the index where we want to insert the new element and the value of the new element.

users.insert(4, "Raj")
print(users)

#Next, how to remove an element from a list?
#We use pop() function to remove an element from the list.
users.pop()
print(users)

#Here we did not pass any argument to the pop() function, so the last element is removed
users.pop(2) #This will remove the element at index 2 which is "Charlie"
print(users)

#You can also use del keyword to remove an elment from the list by specifying the index of the element to be removed.
del users[1]
print(users) 

users.remove("Raj") #This will remove the element "Raj" from the list
print(users)
#Remove() function will be used only when you know the value of the element you want to remove, and it will remove the first occurrence of that value in the list.

new_customers = []
new_customers.append("Alice")
new_customers.append("Bob")
new_customers.append("Charlie")
new_customers.append("David")
new_customers.append("Eva")
print(new_customers)

recently_added_customer = new_customers.pop()
print("Recently added customer is ", recently_added_customer)

#Who is the first customer in the list?
first_customer = new_customers[0]
print("Our first customer is ", first_customer)
print(new_customers)

#when we the pop() function is used, it removes the last element from the list and returns that element, so we can store it in a variable and use it later.

#Sometimes the data in the list is not in the order we want to we use the sort() function to sort the elements in the list in ascending order.
my_fav_cars = []
my_fav_cars.append("BMW")
my_fav_cars.append("Marcedes")
my_fav_cars.append("Audi")
my_fav_cars.append("Tesla")
print(my_fav_cars)
my_fav_cars.sort()
print(my_fav_cars)

#We can also sort the list in descending order by passing the argument reverse=True to the sort() function.
my_fav_cars.sort(reverse=True)
print(my_fav_cars)

#Other way is to reverse the list by using the reverse() function, but this will not sort the list in descending order, it will just reverse the order of the elements in the list.
my_fav_cars.reverse()
print(my_fav_cars)


#Temprarly sort the list in ascending order without modifying the original list by using the sorted() function.
item_id  = []
item_id.append(2001)
item_id.append(1009)
item_id.append(1001)
item_id.append(2005)
print(item_id)
print(sorted(item_id)) #Output - [2001, 1009, 1001, 2005]
print(item_id) #Output - [2001, 1009, 1001, 2005] - Original list is not modified

#Finding the length of the list using len() function
print(len(item_id))
