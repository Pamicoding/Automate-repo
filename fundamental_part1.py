#%%
# The difference between if and while.
spam = 6
if spam<5: # if only pass the word, so print it once.
    print('hello world')
    spam = spam+1
#%%
spam = 0
while spam<5: # while will loop it from the beginning, so it print the text 5 times.
    print('hello world')
    spam = spam+1
# %%
name = '' # pass an empty string to start the loop
while name != 'your name': 
    print(f"please type your name")
    name = input()
print('Thank you')
# %%
while True: # if True, continue looping
    print('who are u')
    name = input()
    if name == 'abc':
        print(f"welcome 87 {name}")
    else:
        continue
    print('password for login')
    password = input()
    if password == 'abc':
        print('4 real?')
        break
    else:
        continue    
# %%
# combination practice
name = ''
while not name: # because not name == 0, 0.0, or '', so this is equal to True.
    print('enter it:')
    name = input() # if I enter the wrong name, the while loop continue.
print('what?') 
abc = input() # I have to type int to pass the if conditional expression, 
if abc == str:
    print('???')
elif abc == int:
    print('what happen?')
else:
    while True:
        print('extreme code')
        code = input()
        if code == '12':
            print('Good Luck')
            break
        else:
            continue
# %%
# guess number
import random
secret_number = random.randint(0,20)

for guess_time in range(1,10):
    print('take a guess')
    guess = int(input())
    if guess < secret_number:
        print('larger!')
    elif guess > secret_number:
        print('smaller!')
    else:
        print('Bingo!')
        break # for statement can also use break and continue
if guess_time < 4:
    print(f'nice work, you guess in {guess} times')
else:
    print(f"it's ok, {guess_time} is fine")

    
# %%
# zigzag animation practice
import sys, time
lines = 15
indent = 0
indentIncreasing = True

try:
    while lines > 0:
        print(' ' * indent, end='') 
        # indent times the ' ' (space) will be plotted before the astericks
        # end='' is designed to print the putput in the same line to avoid adding the new line.
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent == 8:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
                lines -= 1
except KeyboardInterrupt:
    sys.exit()
# %%
# def and try function practice
def collatz(number: int):
    if number % 2 == 0:
        print('number//2')
        return number // 2
    else:
        print('3*number+1')
        return 3*number+1

while True:
    try:
        youwant = int(input("please enter an interger:"))
    except ValueError:
        print("please type the interger, are you blind?")
        continue

    result = collatz(youwant)
    if result != 1:
        print(f"keep going! now your number is {result}")
        continue
    else:
        print('u got the answer 1!')
        break
# %%
# ch4 string
# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# create the list of cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1)==0: # decide the living status of cell randomly
            column.append('#') # append it along the y
        else:
            column.append(' ') # append it along the y
    nextCells.append(column) # jump back to x for loop to store the y value of the specific x coordinate.
# and loop it until the x coordinate is finish.
while True:
    print('\n\n\n\n\n') # separete the output in am interval of 5 lines.
    currentCells = copy.deepcopy(nextCells) # if we have list in list, we should use the deepcopy.

    # this part wants to display the list in the real xy coordination.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print() # print a new line! because we use end='', if we don't print a new line it will over the limitaiton.
    
    # counting the neighbor with '#'
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y+1) % HEIGHT
            belowCoord = (y-1) % HEIGHT

            numNeighbor = 0
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbor += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbor += 1            
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbor += 1            
            if currentCells[leftCoord][y] == '#':
                numNeighbor += 1            
            if currentCells[rightCoord][y] == '#':
                numNeighbor += 1            
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbor += 1            
            if currentCells[x][aboveCoord] == '#':
                numNeighbor += 1            
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbor += 1


            
            if currentCells[x][y] == '#' and (numNeighbor == 2 or numNeighbor == 3):
                nextCells[x][y] == '#'
            elif currentCells[x][y] == ' ' and numNeighbor == 3:
                nextCells[x][y] == '#'
            else:
                nextCells[x][y] == ' '
    time.sleep(1)
#%%

def basket(ball:list):
    a = ', '.join(map(str, ball[:-1]))
    # if I use the str(ball[:-1]) but not map(str, ball[:-1]), it will consume more memory.
    b = str(ball[-1])
    artery = a + ", and "+ b
    return artery

spaghetti = [1,2,3,4,5,6]
basket(spaghetti)

# %%
