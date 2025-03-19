valid= False
while not valid:
    try:
        n=int(input("Enter a number: "))
        while n%2==0:
            print("bye \n hi")
        valid=True
    except ValueError:
        print("Invalid")
