def next_palindrome(a):
    a = a+1
    while not is_palindrome(a):
        a += 1
    return a

def is_palindrome(a):
    return str(a) == str(a)[::-1]





if __name__ == '__main__':
    a = int(input("Enter the size of your list:\n"))
    num_list = []
    for x in range(a):
        num_list.append(int(input("Enter the number of your list:\n")))

    print(f"Your list is {num_list}")

    new_list = []
    for element in num_list:
        if element > 10:
            n = next_palindrome(element)
            new_list.append(n)

        else:
            new_list.append(element)

    print(f"output list: {new_list}")