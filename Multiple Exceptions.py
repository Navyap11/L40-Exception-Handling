try:
    num1, num2= eval(input("Enter two numbers. Put a comma between both: "))
    result= num1/num2
    print("The result of ",num1," divided by ",num2, " is: ",result)
except ZeroDivisionError:
    print("This can't be divided by '0'. Try Again!")
except SyntaxError:
    print("The comma is missing. Try Again!")
except:
    print("Wrong input. Try Again!")
else:
    print("No exceptions (errors)!")
finally:
    ("Your code wil follow through no matter what!")