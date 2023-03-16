s=["·"]*9;d=print
def draw():d(f"\n{s[0]} {s[1]} {s[2]}\n{s[3]} {s[4]} {s[5]}\n{s[6]} {s[7]} {s[8]}")
draw();p,f=1,True
while f:
    sym="X"if p==1else"O"
    try:sq=int(input("\nChoose a square to move: "))-1
    except ValueError:d("Invalid character");draw();continue
    if not 0<=sq<=8:d("Invalid character")
    elif s[sq]=="·":s[sq]=sym;p*=-1
    else:d("That square is already occupied")
    draw()
    for i in range(0,7,3):
        if s[i]==s[i+1]==s[i+2]!="·":d(f"{s[i]} wins");f=0;break
    for i in range(3):
        if s[i]==s[i+3]==s[i+6]!="·":d(f"{s[i]} wins");f=0;break
    if s[0]==s[4]==s[8]!="·"or s[2]==s[4]==s[6]!="·":d(f"{s[4]} wins");f=0
    if f and all(sq!="·"for sq in s):f=0;d("Draw")
