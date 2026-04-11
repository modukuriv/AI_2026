#Data Types - Strings 
#In programming we define and father some sort of data
#With that data we can do something useful with it. 

#So let's learn strings 
#A string is a sequence of characters and it should be inside quotes.

myName = "Alex"
yourName = " Robinson"
print (myName + yourName) #Output - Alex Robinson - This is String concatination

#You can also use single quotes as well 

myName = 'Alex'
yourName = 'My name is "Robinson"'

print(myName + yourName)

#Let's learn some methods...ohhh wait a minute, what is a methods?

#A methods is a action that Python can perform on a piece of data. 

#Some examples are:

fullName = "Alex Robinson"
print(fullName.upper()) #Output - ALEX ROBINSON

'''
So, what's happening here?
There is an existing methods called upper(), the assigned action for this methods 
is to covert the string to uppercase and we use the dot notation to call the method with () parenthesis.
like this fullName.upper() - methods often need additiona info to process, so we pass this info as arguments in the parenthesis. 
In this case, there are no arguments needed for the upper() method, so we just leave the parenthesis empty.
'''

print(fullName.lower()) #Output - alex robinson
print(fullName.title()) #Output - Alex Robinson

x = "Programming is fun!"
y = "but you have to practice a lot to improve the skill"
# now let's combinte the x and y statememts 
z = x + " " + y
print(z)

# you might have noticed that we added a space in between x and y when we combined them to create z.
z = x + y
print(z) #Output - Programming is fun!but you have to practice a lot to improve the skill   

#if you observer the output there is no space between statement 1 ans statement 2

#Other things you can add \t for tab and \n for new line
print(x +  "\t" + y)
print (x + "\n" + y)

#since we are already discussing about whitespaces, let's look at hoe python sees whitespaces in a string.
#Python considers all the characters in a string, including spaces, as part of the string.
#For example, if we have a string with leading or trailing spaces, those spaces are included in the string. 

fullName_with_right_space = "Alex Robinson  "
print(fullName_with_right_space) #Output - Alex Robinson
#here in the output we can't any spaces but they are there, so how do we deal with it?

#Remember there already actions in python, so we need use a method here 
print(fullName_with_right_space.rstrip()) #Output - Alex Robinson

fullName_with_left_space = "  Alex Robinson"
print(fullName_with_left_space) #Output -   Alex Robinson
print(fullName_with_left_space.lstrip()) #Output - Alex Robinson    

'''
so far looks good, but let's print again and see what happens

'''
print(fullName_with_left_space) #Output -   Alex Robinson
print(fullName_with_right_space) #Output - Alex Robinson

#so the original string values are not changed and they still have the leading and trailing spaces
#so how do we remove the spaces permanently?
#After removing the spaces, either can assign to the original variable or create a new variable to store the modified string.

fullName_after_removing_right_space = fullName_with_right_space.rstrip()
print(fullName_after_removing_right_space) #Output - Alex Robinson
fullName_after_removing_left_space = fullName_with_left_space.lstrip()
print(fullName_after_removing_left_space) #Output - Alex Robinson



#=======Practice Exercise===========
person_name = "Eric"
message = "Would you like to learn some Python today?"
print("Hello " + person_name + "," + " " + message)

print(person_name.lower())
print(person_name.upper())
print(person_name.title())

scientist_name = "albert einstein"
quote = ' "A person who never made a mistake never tried anything new"'
print(scientist_name.title() + " " + "once sair," + quote)
