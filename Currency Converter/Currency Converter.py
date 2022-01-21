with open("Currency Data.txt","r") as f:
    data = f.readlines()

CurrencyConverter = {}

print("****CURRENCY CONVERTER****")      
choice = int(input("Enter:\n1)To Convert From Indian Rupees TO Other Currency : \n2)TO Convert from Other currency to Indian Rupees +:\n"))
if(choice==1):
    for line in data:
        parsed = line.split("\t")
        CurrencyConverter[parsed[0]] = parsed[1]
    amount = int(input("Enter The Amount : "))
    print("Enter the Currency in which you want to convert :\nAvailable Options :")
    [print(item) for item in CurrencyConverter.keys()]
    currency = input("Enter : ")
    print(f"{amount} INR is equal to {amount*float(CurrencyConverter[currency])} {currency}")
if(choice==2):  
        for line in data:
            parsed = line.split("\t")
            CurrencyConverter[parsed[0]] = parsed[2]
        amount =int(input("Enter the Amount : "))
        print("Enter the Currency in which Amount is :\nAvailable Options :")
        [print(item) for item in CurrencyConverter.keys()]
        currency = input("Enter : ")
        print(f"{amount} {currency} is equal to {amount * float(CurrencyConverter[currency])} INR")