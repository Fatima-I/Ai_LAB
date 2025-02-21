# -*- coding: utf-8 -*-
"""Lab 02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yQJ7bbXfkg29IJNVXcjUF0i1_iutNPOg
"""



"""#Activity 1"""

myList1 = []
print("Enter objects of first list...")
for i in range(5):
  val = input("Enter a value: ")
  n = int(val)
  myList1.append(n)

myList2 = []
print("Enter objects of second list...")
for i in range(5):
  val = input("Enter a value: ")
  n = int(val)
  myList2.append(n)

list3 = myList1 + myList2
print(list3)

"""#Activity 2"""

def isPalindrome(word):
  temp = word[::-1]
  if temp.capitalize() == word.capitalize():
    return True
  else:
    return False
print(isPalindrome("deed"))

"""# Activity 3"""

a = [[1,0,0],[0,1,0],[0,0,1]]
b = [[1,2,3],[4,5,6],[7,8,9]]
c = []
for indrow in range(3):
  c.append ([])
  for indcol in range(3):
    c[indrow].append(0)
    for indaux in range(3):
      c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]
print(c)

"""#Activity 4"""

def perimeter(listing):
  leng = len(listing)
  perimeter = 0;
  for i in range(0, leng - 1):
    dist = (((listing[i][0]-listing[i+1][0])**2)+((listing[i][1]-listing[i+1][1])**2))**0.5
    perimeter = perimeter + dist
  perimeter = perimeter + (((listing[0][0]-listing[leng-1][0])**2)+((listing[0][1]-listing[leng-1][1])**2))**0.5
  return perimeter

L = [(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))

"""#Activity 5"""

def SymmDiff(a,b):
  e = set()
  for i in a:
    if i not in b:
      e.add(i)
  for i in b:
    if i not in a:
      e.add(i)
  return e

set1 = {0,1,2,4,5}
set2 = {4,5,7,8,9}
print(SymmDiff(set1,set2))

#verification using inbuilt function
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)

"""#Activity 6"""

sample = {("sohaib","ali"):"0246585468445",("aib","li"):"0246585468445",("sib","ai"):"0246585468445",}
firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
searchtuple = (firstname,lastname)
if searchtuple in sample:
  print(sample[searchtuple])
else:
  print("name not found")

"""#Lab Task 1"""

list1 = []
num_items1 = int(input("Enter the number of items for the first list: "))
for _ in range(num_items1):
    item = input("Enter an item: ")
    list1.append(item)
list2 = []
num_items2 = int(input("Enter the number of items for the second list: "))
for _ in range(num_items2):
    item = input("Enter an item: ")
    list2.append(item)
merged_list = list1 + list2
merged_list.sort()
print("Sorted merged list:", merged_list)

"""#Lab Task 2"""

list1 = []
num_items1 = int(input("Enter the number of items for the first list: "))
for _ in range(num_items1):
    item = int(input("Enter an integer item: "))
    list1.append(item)

list2 = []
num_items2 = int(input("Enter the number of items for the second list: "))
for _ in range(num_items2):
    item = int(input("Enter an integer item: "))
    list2.append(item)

merged_list = list1 + list2
smallest = min(merged_list)
largest = max(merged_list)
print("Merged list:", merged_list)
print("Smallest element:", smallest)
print("Largest element:", largest)

"""#Lab Task 3"""

from math import sin, cos, pi

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

h = 0.001
x_values = [i for i in frange(-pi, pi, h)]

print("x\t\tApprox Derivative\tcos(x)")

for x in x_values:
    derivative = (sin(x + h) - sin(x)) / h
    actual = cos(x)
    print(f"{x:.5f}\t{derivative:.5f}\t\t{actual:.5f}")

"""#Lab Task 4"""

birthday_dict = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
    "Isaac Newton": "01/04/1643",
    "Marie Curie": "11/07/1867"
}
print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday_dict.keys():
    print(name)

name_to_lookup = input("Who's birthday do you want to look up? ")

if name_to_lookup in birthday_dict:
    print(f"{name_to_lookup}'s birthday is {birthday_dict[name_to_lookup]}.")
else:
    print("Sorry, we don't have that person's birthday.")

"""#Lab Task 5"""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]
new_dict = {key: sample_dict[key] for key in keys if key in sample_dict}
print(new_dict)