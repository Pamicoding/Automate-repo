#%%
grid = [['1','2','3'],
        ['2','3','4']
]

grid[1][2]
# %%
# the utilization of dict
allGuest = {'Alice':{'apple':5,'pretzls':12},
            'Bob':{'ham sandwiches':3, 'apple': 2},
            'Carol':{'cups':3,'apple pies':1}
            }

def total_brought(guest, item): # parameter calls item != the method .item()
    numBrought = 0
    for k,v in guest.items(): 
        # this place is .item(), to list the all information in the allGuest.
        # k represent the name, v represent the picnic dictionary.
        numBrought = numBrought + v.get(item,0) 
        # using get() to find the picnic item and get the value in it.
    return numBrought

print('Number of things being brouhgt:')
print('-Apple         '+ str(total_brought(allGuest,'apple'))) 
print('-pretzls       '+ str(total_brought(allGuest,'pretzls')))    
print('-ham sandwitch '+ str(total_brought(allGuest,'ham sandwich')))    
print('-cups          '+ str(total_brought(allGuest,'cups')))    
print('-apple pie     '+ str(total_brought(allGuest,'apple pie')))    


# %%
# validate the chessboard
# 1. the board should not more than 16 pieces, and should not more than 1 queen. (done)
# 2. the piece should not exceed the chessboard, for example, 9z is not available. (done)
# 3. using boolean as an output to check the status of chessboard.
# name: pawn x 8, bishop x 2, knight x 2, rook x 2, queen x1, king x 1
def isValidChessBoard(theboard):
    # acquiring the value for conditional expression.
    num_queen_black = 0
    num_queen_white = 0
    num_black = 0
    num_white = 0
    for piece in theboard.values(): # using .values() to acquire the value after colon
        if piece == 'bqueen':
            num_queen_black += 1
        elif piece == 'wqueen':
            num_queen_white += 1
        if piece in ['bqueen','bpawn', 'bbishop', 'bknight', 'brook', 'bking']:
            num_black += 1
        elif piece in ['wqueen', 'wpawn', 'wbishop', 'wknight', 'wrook', 'wking']:
            num_white += 1      

    for location in theboard.keys():
        firstcharacter = location[0]
        secondcharacter = location[1]
    
    # to return the True or False
    if num_queen_white > 1 or num_queen_black > 1:
    # just a remider
    # if I type a or b > 1, it will become answering which one > 1 but not the condition I want to ask.
        return False
    if num_black > 16 or num_white > 16:
        return False
    if firstcharacter not in '12345678':
        return False
    if secondcharacter not in 'abcdefgh':
        return False
    
    return True, print(f"num_queen_black:{num_queen_black}, num_queen_white:{num_queen_white}, num_black:{num_black}, num_white:{num_white}")
 


rightboard = {'1h':'bbishop', '2a': 'bqueen', '2g':'wbishop', '5h':'wqueen'}
wrongboard = {'1h':'bbishop', '2a': 'wqueen', '2g':'wbishop', '9h':'wqueen'}
#isValidChessBoard(rightboard)
isValidChessBoard(rightboard)
# %%
before, sep, after = 'hello, world!'.partition(' ')
# we can separate the string into 3 parts (because of the partition() method ) and allocate them into different variables.
# In this case, before = 'hello,', sep = ' ', after = 'world!'.
# %%
def printPicnic(itemDict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-')) # print the PICNIC ITEMS in the middle as a title.
    for k, v in itemDict.items(): # k for keys, v for values.
        print(k.ljust(leftwidth, '.'), str(v).rjust(rightwidth))

picnicItem = {'sandwitches': 4, 'apples': 12,'sushi': 9, 'new jeans': 5}
printPicnic(picnicItem, 20, 6)
# %%
