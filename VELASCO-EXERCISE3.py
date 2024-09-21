#John Michael Luis Velasco BSCPE 2-3
def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."
    
    for i in range(n//2 + 1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (n//2 - i)
        print(spaces + stars)

    for i in range(n//2 - 1, -1, -1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (n//2 - i)
        print(spaces + stars)

n = int(input("Enter an odd integer: "))
result = print_diamond(n)
if result:
    print(result)
