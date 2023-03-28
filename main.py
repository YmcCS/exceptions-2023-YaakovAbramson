try:
    first = input("Enter the first value: ")
    second = input("Enter the second value: ")
    print(first/second)
except TypeError:
    print("TypeError")
except EOFError:
    print("Don't do that. ")
except ZeroDivisionError:
    print("Imagine that you have zero cookies and you split them evenly among zero friends, How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends. ")
except:
    print("The brown cat jumped over the quick fox after committing suicide on the beach. ")
