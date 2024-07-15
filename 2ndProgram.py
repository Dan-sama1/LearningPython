#hospital activity
name = "John Smith"
age = 20
newPatient = True

print("Patient's name: ", name)
print("Patient's age: ", age)
print("Is he a new patient?: ", newPatient)

#String slicing
web = "https://lamaw.com"
print(web)
sli = slice(0, 8)
sli2 = slice(-4, 17)

inp = input("Input website name: ")

print(f"{web[sli]}{inp}{web[sli2]}")
