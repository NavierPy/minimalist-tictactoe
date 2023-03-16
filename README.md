# tictactoe

A minimalist version of the traditional tic-tac-toe game.

The basic game, well structured and commented, is in the file "long_version.py" and has 93 lines, of which almost half are blank lines and comments. Eliminating these, we obtain a program of 52 lines.

By consecutively optimizing the code to reduce its lines, we obtain successive versions: 38, 17 and 10 lines, at the cost of increasing the abstraction and reducing the readability of the code.

As a sample, the 10-line version is included here:

```
s=["·"]*9;d=print
def draw():d(f"\n{s[0]} {s[1]} {s[2]}\n{s[3]} {s[4]} {s[5]}\n{s[6]} {s[7]} {s[8]}")
draw();p,f=1,True
while f:
    sym="XO"[p<0];sq=input("\nChoose a square to move: ")
    if sq.isnumeric()and 0<=int(sq)-1<=8and s[int(sq)-1]=="·":s[int(sq)-1],p=sym,-p
    else:d("Invalid character"*(not sq.isnumeric()or not 0<=int(sq)-1<=8or s[int(sq)-1]!="·"))
    draw()
    if any(s[i]==s[i+1]==s[i+2]!="·"for i in range(0,7,3))or any(s[i]==s[i+3]==s[i+6]!="·"for i in range(3))or s[0]==s[4]==s[8]!="·"or s[2]==s[4]==s[6]!="·":d(f"{sym} wins");f=0
    if f and all(sq!="·"for sq in s):d("Draw");f=0
```
