Board = {'1': ' ' , '2': ' ' , '3': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '7': ' ' , '8': ' ' , '9': ' ' }

keys =[]

for key in Board:
    keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def getPlayer():
    p = input("Player's name: ")
    return p

def game():
    
    player1 = getPlayer()
    player2 = getPlayer()
    cplayer = player1
    count = 0

    for x in range(10):
        printBoard(Board)
        print("It's %s turn" % cplayer + ". Where to move?")

        move = input()

        if Board[move] == ' ' and cplayer == player1:
            Board[move] = "X"
            count += 1
        elif Board[move] == ' ' and cplayer == player2:
            Board[move] = "O"
            count += 1
        else:
            print("That place is already filled.\nWhere to move?")
            continue
        
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': # across the top
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': # across the middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': # across the bottom
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': # down the left side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': # down the middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': # down the right side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " + cplayer + " won. ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        
        if cplayer == player1:
            cplayer = player2

        else:
            cplayer = player1
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in keys:
            Board[key] = " "
        game()

    

if __name__ == "__main__":
    game()