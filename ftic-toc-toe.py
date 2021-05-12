theBoard = {'7':' ','8':' ','9':' ',
             '4':' ','5':' ','6':' ',
              '1':' ','2':' ','3':' '}

board_Keys =[]
for key in theBoard:
    board_Keys.append(key)

def gameBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
    
def startGame():
    turn = 'x'
    count = 0
    for i in range(10):
        gameBoard(theBoard)
        print("Its your turn," + turn + " Move to which place?")
        move = input()
        if theBoard[move] == " ":
            theBoard[move] = turn
            count = count+1
        else:
            print("That place is already filled\nMove to which place?")
            continue       
        
        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ "won ***")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
            elif theBoard['7']==theBoard['4']==theBoard['1']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
            elif theBoard['8']==theBoard['5']==theBoard['2']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
            elif theBoard['9']==theBoard['6']==theBoard['3']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
            elif theBoard['1']==theBoard['5']==theBoard['9']!='':
                gameBoard(theBoard)
                print("\nGame over\n")
                print("*** " +turn+ " won ***")
                break
        if count==9:
            print("\nGame Over\n")
            print("*** It's a tie ***")
        
        if turn == 'x':
            turn = 'y'  
        else:
            turn = 'x' 

    playAgain = input("Do you want playAgain?(y/n)")
    if playAgain== 'y' or playAgain == 'Y':
       for key in board_Keys:
           theBoard[key] =''
startGame()