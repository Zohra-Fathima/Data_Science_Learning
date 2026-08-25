# f= open("sample2.txt","a") #file object(this function returns us the file object , the f variable now stores all the info related to file)

# data=f.read()
# data=f.readline()
# print(data)
# f.write("text to overwrite \n the complete code")
# f.write("\nthis is used to append")#appends /adds new text to the file
# f.write("this is some random text")
# f.close()

# with open("sample.txt","r") as f: #here we dont have to use close() operation to close our file, because with handels it

#     data=f.read()
#     print(len(data))

# import os
# os.remove("sample2.txt")#to delete a file

#EXCEPTION HANDLING
# try:
#     x=int(input("enter x: "))
#     ans=10/x

# except(ZeroDivisionError):
#     print("Error:division by 0 not allowed")

# except(ValueError):
#      print("invalid input")

# else:
#         print(ans)

# finally:
#      print("end of code")



#LIST COMPREHENSIONS
# square=[]#normal list

# for i in range(6):
#     square.append(i*i)

# print(square)

#example1:
# sq=[i*i for i in range(6) if i%2!=0 ]#list comprehension
# print(sq)

#example2:
# list=[-1,-3,5,4,-9,0,7]

# ans=[0 if val<0 else val for val in list]
# print(ans)

#example3:
# words=["hello","apple","fruit"]

# words=[val.upper() for val in words]
# print(words)


#json.loads(dealing with strings):-
# import json
# json_str='{"name":"zohra","isTeacher":null}'

# py_object=json.loads(json_str)
# print(type(py_object))
# print(py_object)

#json.dumps(dealing with strings):-
# import json

# py_obj={
#     "name":"zohra",
#     "isTeacher":True
# }

# json_str=json.dumps(py_obj)
# print(type(json_str),json_str)


#json.load(dealing with files):-
# import json

# with open("data.json","r") as f:

#     py_obj=json.load(f)
#     print(type(py_obj))

#json.dump(dealing with files):-
import json
data={
    "name":"zohra",
    "city":"kashmir",
    "isTeacher":True
}

with open("data.json","w") as f:
    json.dump(data,f,indent=5,sort_keys=True)#indent=5,sort_keys=True are just a special knowledege to know where we can add spaces and use sort to arange in ascending or descending order
    print(type(data),data)


