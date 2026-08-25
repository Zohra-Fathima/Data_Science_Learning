ans1= int(5+10.0) #casting
ans2= 5+10.0 #conversion

# print(ans1, type(ans1))
# print(ans2, type(ans2))

#MATCH CASE
# color=input("enter color: ")

# match color:
#     case "green":
#         print("walk")
#     case "yellow":
#         print("look")
#     case "red":
#         print("stop")
#     case _:
#         print("wrong color")


#LOOPS
#for loop
string ="hello"

#in => membership operator
# for var in string:
#     print(var)


#range function
# for i in range(5):
#     print(i)


# word="artificial intelligence"
# count=0

# for ch in word:
#     if ch=='i':
#         count +=1

# print("count of i=",count)

#VOWEL COUNT
# word="artificial"
# vowel="aeiouAEIOU"
# count=0
# for ch in word:
#     if ch in vowel:
#         count +=1
# print("the number of vowels in string is: ",count)

#RANGE FUNCTION
# for i in range(2,10,2):
#     print(i)

#SUM OF DIGITS
# n=int(input("enter the number: "))
# sum=0
# for i in range(n+1):
#     sum +=i
# print(sum)

#FUNCTIONS
def name():#fnx definition
    print("hello")

name()#function call


#LAMBDA FUNCTION
# sum=lambda a,b: a+b/2
# print(sum(4,5))
n=int(input("enter number: "))
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print(fact(n))