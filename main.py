def is_palindrome():
    word = input("Enter your word : ")
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")
    menu()


def is_prime():
    num = int(input("Enter a number : "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not prime")
                break
            else:
                print(num, "is prime")
                break
    else:
        print(num, "is not prime")
    menu()

def menu():
    print("Choose an operation : ")
    print("[1] Check palindrome ")
    print("[2] Check if prime ")
    print("[3] End ")
    choose = int(input())
    if choose == 1:
        is_palindrome()
    elif choose == 2:
        is_prime()
    elif choose == 3:
        print("End")
    else:
        print("Invalid number. Try again!")
        menu()


menu()
