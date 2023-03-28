try:
    first = input("Enter the first value: ")
    second = input("Enter the second value: ")
    print(first/second)
except TypeError:
    print("TypeError")
except EOFError:
    print("Don't do that. ")
