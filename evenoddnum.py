# take user input and seperate into even and odd 

def input_num():
    uinput= input("space sepatered numbers:")
    return list(map(int,uinput.split()))

def sep(number):
    evens= [num for num in number if num % 2 ==0]
    odds= [num for num in number if num % 2 != 0]
    return evens,odds


number= input_num()
evens, odds = sep(number)
    

print("Even number:", evens)
print("Odd numbers:", odds)