#SLICING
# word="python"
# print(word[2:4]) #starting index:ending index(ending index is not included)


#STRING FORMATTING
#=>using format()
# a=5
# b=10
# sum=a+b

#normal formatting
# print("language is {} ,{}".format("python","js"))
# print("sum of {}, {} is {}".format(a,b,sum))

#index based formatting
# print("sum of {1}, {0} is {2}".format(a,b,sum))

#value based formatting
# print("values of variables {a} {b}".format(a=5,b=10))

#=>using f-strings 
# a=5
# b=10
# print(f"sum of {a} and {b} is {a+b}")


#LISTS
# marks=[90,76,43,87,89,56,"abc",10.44]
# print(type(marks))

#slicing in lists
# marks=[90,76,43,87,89,56,"abc",10.44]
# print(marks[:6])

#METHODS IN LISTS
#append
# nums=[1,2,3]
# nums.append(4)
# print(nums)

#insert (in particualr index)
# nums.insert(2,10)
# print(nums)

#sort(arranges in increasing order)
# nums.sort()
# print(nums)

# to sort in decreasing order simply use:
# nums.sort(reverse=True)
# print(nums)

#to reverse the whole lists
# nums.reverse()
# print(nums)

#LOOPS IN LISTS
#program to find value of x in lists
# list=[1,2,3,10,4]
# x=10
# idx=0
# for ch in list:
#     if ch==x:
#         print(f"x found at {idx}")
#         break
#     idx +=1
  


#TUPLES
# tup=(1,2,3,4,5)
# print(type(tup))

#slicing in tuple
# tup=(1,2,3,4,5)
# print(tup[:2])

#loops in tuple
# tup=(1,2,3,4,5)
# sum=0
# for val in tup:
#     sum +=val

# print(f"sum of values is {sum}")

#METHODS in tuple
#t.index(value) it returs 1st occurence index
# tup=(1,2,2,3,4,2)
# print(tup.index(2)) 

#t.count(value) it counts the total number of occurences
# tup=(1,2,2,3,4,2)
# print(tup.count(2)) 

#DICTIONERY 
# info={
#     "name":"zohra",
#     "cgpa":8.54,
#     "subjects":["math","science"]
# }

# info["name"]="gori"
# print(info["name"])

#METHODS IN DICT
# info={
#     "name":"zohra",
#     "cgpa":8.54,
#     "subjects":["math","science"]
# }

# print(info.keys()) #returns all the keys
# print(info.values())#retuns all the values
# print(info.items())#retuns all the key value pairs
# print(info.get("name2")) #returns the value of key(refer notes)
# info.update({
#     "city":"delhi"
# })
# print(info)#adds a new item to dict


#SETS
# s={1,2,2,2,3}
# print(s)

#METHODS in sets
# s.add(5)#to add elements in set
# print(s)

# s.remove(1)#removes element from set
# print(s)

# s.clear()#empties the set
# print(s)

# s.pop()#removes a random values from set
# print(s)

# s1={1,2,3,4,5}
# s2=[4,5,6,7,8]

# print(s1.intersection(s2))#returns common entries
# print(s1.union(s2))#returns all entries



# info = [
#         ("Alice", "Math"),
#         ("Bob", "Science"),
#         ("Alice", "Science"),
#         ("Charlie", "Math"),
#         ("Bob", "Math"),
#         ("Alice", "English"),
#         ("Charlie", "English")
# ]

#list all unique courses
# courses=set()
# for tup in info:
#     courses.add(tup[1])
# print(courses)


#list students enrolled in english
#=>me
# for tup in info:
#     if(tup[1]=="English"):
#         print(tup[0])

#=>maam
# for name,course in info:
#     if(course=="English"):
#         print(name)


#create a dictionery (student,set of course)
# dict={}

# for name,course in info:
#     if(dict.get(name)==None):
#         dict.update({name: set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)

# print(dict)