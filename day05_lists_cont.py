#Let's continue learning lists
#Today you will learn about the how loops work with lists 

#Why do we need learn looping with lists?

#Let's say there are 100000 itemrs in the super market
#You check check the price of each item and add it to the total bill, how do you do that?
#or you want to update the price of each item by 10% in the list, how do you do that?
#or you want to print the name of each item in the list, how do you do that?

#In all the above scenarios, we need to perform the same action on each item in the list, right?

#This is where loops come in handy, they allow us to perform the same action on each item in the list without having to write the same code multiple times.

items = ["apple", "banana", "sugar", "salt", "milk", "water",
         "chiken", "fish", "almonds","rice", "jam", "bread", 
         "eggs", "butter", "cheese", "coffee", "beer","chocolate", 
         "cookies", "cereal", "yogurt", "juice", "tea","soda",
         "ice cream", "cake", "pie", "pasta", "noodles", 
         "sauce","oil", "vinegar", "spices", "herbs", "nuts",
         ]
#Now, we want to print the name of each item in the list, how do we do that?
#We can print using print function like print (items) but it will print the whole list in one line, right?
print(items)

#But we want to print each item in a new line, how do we do that?
#We can use a loop to iterate through each item in the list and print it in a new line.

for item in items:
    print(item)

#Don't worry about the syntax - I will explain in details 
# Here what we are saying is 
    # for each item in the list of items, 
    # print the item in a new line. 
    #so we use the for keyword to start the loop 
    #creating a variable called item, so we can use it to store the current items
    #from where we want to get the items - in lists right? so we specify the list name which is items in this case.
    #and then we use a colon : to indicate the start of the loop body, and
    #we indent the code inside the loop body, so that Python knows which code belongs to the loop.
    #and then we use the print function to print the current item in a new line.

#now compare the output for print(items) and the for loop. 

#what else can we do with loops and lists? - we can perform any action on each item in the list, for example, we can convert each item to uppercase and print it.
for item in items:
    print(item.upper())

#What else can we do with loops and lists?
# we can also perform some calculations on each item in the list, for example, we can calculate the length of each item and print it.

for item in items:
    print(len(item))
#what else can we do with loops and lists?
# we can also create a new list by performing some action on each item in the existing list, for example,
#  we can create a new list of the lengths of each item in the existing list.
length_of_items = []
for item in items:
    length_of_items.append(len(item))
print(length_of_items)


#so far we looked at each item in the list and did some action

#Now we will print the name to each item 

for item in items:
    print(item.title() + " is available in the super market")

for item in items:
    print(f"{item} is available in the super market")
    print(f"so, you can buy any of the {item} from the super market");
#In the above code, we are using item.title() to convert the first letter of each item to uppercase and the rest to lowercase, and then we are concatenating it with the string " is available in the super market" to create a complete sentence for each item in the list.
#Next, we are using an f-string to achieve the same result, which is a more concise and readable way to format strings in Python. The f-string allows us to directly embed the variable item within the string, making it easier to read and write.

#One thing to remeber here is that indentation is very important in Python, 
# it is used to indicate the block of code that belongs to the loop.

#for item in items:
#print(item) #this will give an error because it is not indented properly, it should be indented to indicate that it belongs to the loop.

#Let's learn about range function and how it works with loops and lists in the next lesson.

for number in range (1, 10):
    print(number)

#Range function is used to generate a sequence of numbers, 
# it takes three arguments - start, stop and step,
# start is the number from which the sequence starts,
# stop is the number at which the sequence stops (not included in the sequence),
# step is the number by which the sequence is incremented (default is 1).

for number in range(1,20,2):
    print(number)

#We can create a list using the range function as well 

item_id = list (range (1, 21))
print(item_id)

for number in item_id:
    print(number)

#Let's look at some more functions

item_price = list(range(1, 99, 5))
print(item_price)
min_price = min(item_price)
print(f"The minimum price is {min_price}"  )
max_price = max(item_price)
print(f"The maximum price is {max_price}")
sum_price = sum(item_price)
print(f"The total price is {sum_price}")

#Now let's look how to use slice to get a part of the list
print(items[0:5]) #this will print the first 5 items in the list, it starts from index 0 and goes up to index 4 (not included in the output)
print(items[30:35]) #this will print the remaining items in the list starting from index 30
print(items[:20]) #this will print the first 20 items in the list, it starts from index 0 and goes up to index 19 (not included in the output)
print(items[20:]) #this will print the remaining items in the list starting from index 20
print(items[-5:]) #this will print the last 5 items in the list, it starts from index -5 and goes up to the end of the list

#Looping through a slice of the list
for item in items[:5]: #this will loop through the first 5 items in the list, it starts from index 0 and goes up to index 4 (not included in the output)
    print(item)

for item in items[30:]: #this will loop through the remaining items in the list starting from index 30
    print(item)

for item in items[-20:]:#this will loop through the last 20 items in the list, it starts from index -20 and goes up to the end of the list
    print(item)

for item in items[10:20]: #this will loop through the items in the list starting from index 10 and goes up to index 19 (not included in the output)
    print(item)

for item in items[::2]: #this will loop through the items in the list starting from index 0 and goes up to the end of the list, but it will skip every other item (step is 2)
    print(item)

for item in items[1::2]: #this will loop through the items in the list starting from index 1 and goes up to the end of the list, but it will skip every other item (step is 2)
    print(item)

#copying a list using slice
final_items = items[:]
print(final_items)

final_items.append("toothpaste")
print(final_items)

items.append("toothbrush")
print(items)

#Now we have two different lists, final_items and items, and we can perform different actions on each list without affecting the other list.