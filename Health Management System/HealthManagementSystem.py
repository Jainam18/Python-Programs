def getdate():
    import datetime
    return datetime.datetime.now()

def log(name):
    a = int(input("Enter:\n1:To Log Data about Diet\n2:To Log Data about Exercises : \n"))
    if a==1:
        food = input("Enter the Food Item : ")
        with open(f"{name}Diet.txt","a") as f:
            f.write(str(getdate())+" "+food+"\n")
        print("Data Entered Sucessfully")
    elif a==2:
        exercise = input("Enter the Exerise : ")
        with open(f"{name}Exercise.txt","a") as f:
            f.write(str(getdate())+" "+exercise+"\n")
        print("Data Entered Sucessfully")
    else:
        print("Invalid Input")

def retrieve(name):
    a = int(input("Enter:\n1:To Retrieve Data about Diet\n2:To Retrieve Data about Exercises : \n"))
    if a==1:
        with open(f"{name}Diet.txt") as f:
            for i in f:
                print(i,end="") 
    elif a==2:
        with open(f"{name}Exercise.txt") as f:
            for i in f:
                print(i,end="") 
    else:
        print("Invalid Input")
        
#MAIN CODE
repeat = 'Y'
while(repeat=='Y'):
    print("Welcome To Health Mangement System : ")
    print("Enter\n1:To Log Data About Clients\n2:To Retrieve Data About Clients")
    i = int(input())
    name = input("Enter the name of Client:\n")
    if i==1:
        log(name)
    elif i==2:
        retrieve(name)
    else:
        print("Invalid Input")
    repeat = input("Enter 'Y' To Log Or Retrieve Data Again : ")
print("You Have Sucessfully Closed The System.")
