# finds the mean of a list of numbers
def input_numbers():
    user_input = input("Space seperated numbers: ")
    return list(map(int, user_input.split()))

def mean(num):
    return sum(num) / len(num)

num = input_numbers()
m = mean(num)
print("You entered:", num)
print("Mean:", m)
