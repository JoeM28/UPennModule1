list1 = [1, 2, 3, '1', '2', '3', 'man', "#@#@#@"]
list2 = [1, 2, 3, '1', '2', '3']
print(list1)
list1.append(4)
print(list1)
print(list1[0])
print(len(list1))
list1.pop()  # Removes last item
print(list1)
list1.pop(7)
print(list1)
list1.insert(2, 32832)
print(list1)
print(1 in list1)
print(list1)
list3 = list1 + list2
print(list3)
list4 = list1 * 2
print(list4)
print("Check Extend")
print(list1)
print(list2)
list5 = list1.extend(list2)
print(list5)
print(list1)
for l in list1:
    print(l)
print("Slice a List")
print(list1)
print(list1[2:5])  # index 2 to 4  # element 3 to 5
print(list1[4:])   # index 4 to end  # element 5 to end
print(list1[:])  # element from 1 to end
print(list1[:-4])  # Removes the last 4 elements
print(list1)
print(list1[::2])
"""
start → where to begin (default is 0, the first element).
stop → where to end (default is the end of the list).
step → the interval (stride) between elements.
Here, ::2 means:
Start from the beginning (start omitted).
Go until the end (stop omitted).
Take every 2nd element (step = 2).
"""
print(list1)
list11 = list1[:]
print(list11)
print(list11 is list1)
print(list11 == list1)
oddlist = [2, 4, 6, 8]
oddlist[0] = 1  # You can change an index value content on list
print(oddlist)
oddlist[1:4] = [3, 5, 7]  # you can change multiple values on list
print(oddlist)
# String is a sequence of chars
# List is Mutable Vs String Immutable
s1 = "Hello World!"
print(s1)
print(s1[1])  # you can access a letter from string
# s1[1]='f' BUT you cannot change string content
print(s1.upper())
print(s1.lower())
print(s1[:3])  # gives 1 to 3 chars
name1 = 'Joe Mohan'
M_index = name1.index('M')
print(M_index)
Space_index = name1.index(' ')
print(Space_index)
print(name1[:Space_index])
print(name1[Space_index+1:])
print(name1.capitalize())
print(name1.title())
print(name1.upper())
print(name1.lower())
print(name1.startswith('J'))
print(name1.endswith('M'))
print(name1.isupper())
print(name1.islower())
print(name1.find('M'))
print(name1.index('Mo'))
print(name1.replace('M', 'Z'))
print(name1)
name2 = "   JOHN  SMITH   "
print(name2)
print(name2.strip())  # trims spaces at start and end
# SPLIT
colors = 'ble,red,green'
colors_list = colors.split(',')
print(colors_list)
print(colors_list[2])

# JOIN
human_list = ['man', 'animal', 'human']
human1 = ','.join(human_list)
print(human1)

print(name2)
name2_list = list(name2)
print(name2_list)
name2_list[0] = 'H'
name2_string = ','.join(name2_list)
name3_string = ''.join(name2_list)
print(name2_string)
print(name3_string)
