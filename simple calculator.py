x=int(input(" Enter first number : "))
y=int(input(" Enter second number : "))
print("Type your operation \nAddition\nSubtraction\nMultiplication\nDivision")
a=input()
if (a=="Addition") :
    print(x+y)
elif (a=="Subtraction")  :
    print(x-y)   
elif (a=="Multiplication") :
    print(x*y)   
elif (a=="Division")   :
    print(x/y) 
else :
    print("type your operation carefully")  