print("1: celsius to fahrenheit")
print("2: fahrenheit to celsius")
chooise = int(input('enter your chooise:'))

if (chooise==1):
    cel = float(input("enter temperature in celsius :"))
    far = (cel*9/5)+32
    print('the fahrenheit  value for the given celsius temp:',far)
elif (chooise==2):
    far = float(input("enter temperature in fahrenheit :"))
    cel = (far-32)*5/9
    print('the celsius value for the given fahrenheit temp:',cel)
    print('bye')
