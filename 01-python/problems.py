# with open("names.txt","w") as f:

#     for i in range(5):
#         name=input("enter the name: ")
#         f.write(name + "\n")


# with open("names.txt","r") as f:
#     print(f.read())


# with open("names.txt","a")as f:
#     f.write("program run successfully")

# with open("names.txt","r")as f:
#     print(f.read())

# list=[5,10,15,20,25]

# new=[i for i in list if i>15]

# print(new)

# import json
# data={
#     "bengalure":1000,
#     "pune":5000,
#     "mumbai":9000,
    
# }

# with open("cities.json","w")as f:
#     json.dump(data,f,indent=5)

# with open("cities.json","r")as f:
#     json.load(f)


# for city in data:
#     print(city,data[city])

# city = input("Enter city: ")
# population = int(input("Enter population: "))

# data[city]=population

# with open("cities.json","w")as f:
#     json.dump(data,f)


# for city in data:
#     print(city,data[city])

try:
    with open("data.txt","r")as f:
        print(f.read())

except(FileNotFoundError):
    print("Error:file does not exists.")

