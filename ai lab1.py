#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[2]:


import sys
print(sys.version)


# In[3]:


if 5 > 2:
  print("Five is greater than two!")


# In[4]:


2 > 5


# In[5]:


if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 


# In[6]:


x = 5
y = "Hello, World!"


# In[7]:


print(x)


# In[8]:


print(y)


# In[9]:


#This is a comment.
print(x+1)


# In[10]:


#This is a comment
#written in
#more than just one line
print("Hello, World!")


# In[11]:


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


# In[12]:


x = 5
y = "John"
print(x)
print(y)


# In[13]:


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# In[14]:


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


# In[15]:


x = 5
y = "John"
print(type(x))
print(type(y))


# In[16]:


x = "John"
# is the same as
x = 'John'


# In[17]:


a = 4
A = "Sally"
#A will not overwrite a


# In[18]:


#legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# In[19]:


#illegal variable names
#2myvar = "John"
#my-var = "John"
#my var = "John"


# In[20]:


#Camel Case
#Each word, except the first, starts with a capital letter:

myVariableName = "John"


# In[21]:


#Pascal Case
#Each word starts with a capital letter:

MyVariableName = "John"


# In[22]:


#Snake Case
#Each word is separated by an underscore character:

my_variable_name = "John"


# In[23]:


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# In[24]:


x = y = z = "Orange"
print(x)
print(y)
print(z)


# In[25]:


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# In[26]:


fruits = ["apple", "banana", "cherry"]
x, y, z, a = fruits
print(x)
print(y)
print(z)
print(a)


# In[27]:


x = "Python is awesome"
print(x)


# In[28]:


#In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# In[29]:


#You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# In[30]:


x = 5
y = 10
print(x + y)


# In[31]:


x = 5
y = "John"
print(x, y)


# In[32]:


#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# In[33]:


#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[34]:


#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[35]:


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[36]:


x = 5
print(type(x))


# In[37]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))


# In[38]:


#Integers

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# In[39]:


#Floats

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# In[40]:


#Floats

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


# In[41]:


#Complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# In[42]:


#Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[43]:


#list


# In[44]:


thislist = ["apple", "banana", "cherry"]
print(thislist)


# In[45]:


#allow duplicates


# In[46]:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# In[47]:


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[48]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]


# In[49]:


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# In[50]:


#list constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# In[51]:


thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# In[52]:


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# In[53]:


thislist = ["apple", "banana", "cherry"]
print(thislist[-4])


# In[54]:


thislist = ["apple", "banana", "cherry"]
print(thislist[-3])


# In[55]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# In[56]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# In[57]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# In[58]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# In[59]:


#check if item is present

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[60]:


#change item value


# In[61]:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# In[62]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[63]:


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# In[64]:


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# In[66]:


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = "watermelon"
print(thislist)


# In[67]:


#dictionaries


# In[68]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[69]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.get("brand")


# In[70]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.get("model")


# In[71]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d["model"]


# In[72]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["model"]


# In[73]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["mod"]


# In[74]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.get("mod")


# In[75]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False

