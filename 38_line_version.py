state = ["·"]*9
def draw(x):
    print("\n{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}".format(*x))
draw(state)
player = 1
flag = True
while flag:
    symbol = "X" if player == 1 else "O"
    try:
        square = int(input("\nChoose a square to move: "))
    except ValueError:
        print("Invalid character")
        draw(state)
        continue
    if not 1 <= square <= 9:
        print("Invalid character")
    elif state[square-1] == "·":
        state[square-1] = symbol
        player *= -1
    else:
        print("That square is already occupied")
    draw(state)
    for i in range(0, 7, 3):
        if state[i] == state[i+1] == state[i+2] != "·":
            print("{0} wins".format(state[i]))
            flag = False
            break
    for i in range(3):
        if state[i] == state[i+3] == state[i+6] != "·":
            print("{0} wins".format(state[i]))
            flag = False
            break
    if state[0] == state[4] == state[8] != "·" or state[2] == state[4] == state[6] != "·":
        print("{0} wins".format(state[4]))
        flag = False
    if flag and all(square != "·" for square in state):
        flag = False
        print("Draw")