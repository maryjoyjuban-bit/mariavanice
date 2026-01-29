# even_odd_checker.py

def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

def main():
    num = int(input("Enter a number: "))
    print(check_even_odd(num))

if _name_ == "_main_":
    main()
