def collatz(number):
    if number % 2 == 1:
        return number * 3 + 1
    else:
        return number / 2

print("Input a integer here")

try:
    num = int(input())
    while True:
        if num == 1:
            print(str(num))
            break
        else:
            print(str(num))
            num = collatz(num)
except ValueError:
    print("Please enter a integer greater than 0.")