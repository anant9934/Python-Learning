#write a python programe using function to convert celsius into fahrenhite

f = float(input("enter temprature in farenhite : "))

def converter(f):
    return 5*(f-32)/9

c = converter(f)
print(f"the temprature in celsius is {c}°C")     #using round tag wil improve output result
print(f"the temprature in celsius is {round(c)}°C")

