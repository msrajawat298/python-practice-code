
play = True

while play:

    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

    if input("Play again? ") == "no":
        play = False
