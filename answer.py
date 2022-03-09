def game_menu():
    flag = True
    while flag:
        print('Καλωσήλθατε στο παιχνίδι!')
        ans=input('Θέλετε να αρχίσετε νέο παιχνίδι (N) ή να φορτώσει ένα αποθηκευμένο παιχνίδι από αρχείο (S);')
        if ans == 'n' or ans == 'N':
            flag = False
            return 0
        elif ans == 's' or ans == 'S':
            flag = False
            return 1
        else:
            print('Λάθοςαπάντηση, ξανά προσπάθησε!')
            

     
def maketable(num_st):
    """
    >>> maketable(5)
         1    2    3    4    5
     -------------------------
     A|    |    |    |    |    |
     B|    |    |    |    |    |
     C|    |    |    |    |    |
     D|    |    |    |    |    |
     E|    |    |    |    |    |
     F|    |    |    |    |    |
     G|    |    |    |    |    |
     H|    |    |    |    |    |
     -------------------------
    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    """

    print(' ', *range(1,num_st+1), sep="    ")
    print('','-' * num_st * 5)

    ls=['A','B','C','D','E','F','G','H']

    board=[]
    for j in range(8):
        board += [[]]
        for i in range(num_st):
            board[j] += [' '] 

    for j in range(8):
        print(' ', ls[j] , '|', sep='' , end='')
        for i in range(num_st):
            print('   ',board[j][i] , '|', sep='' ,end='')
        print('')


    print('','-' * num_st * 5)

    return board


def table(num_st,board):
    print(' ', *range(1,num_st+1), sep="    ")
    print('','-' * num_st * 5)

    ls=['A','B','C','D','E','F','G','H']

    for j in range(8):
        print(' ', ls[j] , '|', sep='' , end='')
        for i in range(num_st):
            print('   ',board[j][i] , '|', sep='' ,end='')
        print('')

    print('','-' * num_st * 5)

    return board


def position(player,num_st,board):
    
    flag = True
    while flag:
        print('Παίκτης ', player ,': ' ,sep='',end='')
        col=int(input('Επέλεξε στήλη για το πιόνι σου:'))

        if col < 1 or col > num_st:

            while col < 1 or col > num_st:
                print('Στήλη εκτόσ ορίων. Εισάγετε νέο αριθμό!')
                col=int(input('Επέλεξε στήλη για το πιόνι σου:'))

        hight=0

        if board[0][col-1] == ' ':
            if player==1:
                for j in range(8):
                    if board[7-j][col-1] == ' ':
                        board[7-j][col-1] = 'O'
                        hight = 7-j
                        flag = False
                        break
            else:
                for j in range(8):
                    if board[7-j][col-1] == ' ':
                        board[7-j][col-1] = 'X'
                        hight = 7-j
                        flag = False
                        break  
        else:
            print('Εισάγετε νέο αριθμό στήλης, η στήλη είναι γεμάτη!')

    return board , hight , col                      
    
def win_horiz(i,char,num_st,board):

    """
    >>> board = [[' ','O',' ',' ',' ',' ',],\
                [' ','O',' ',' ',' ',' ',],\
                [' ','O',' ',' ',' ',' ',],\
                [' ','O',' ',' ',' ',' ',],\
                [' ',' ','X',' ','O',' ',],\
                [' ',' ',' ',' ','X',' ',],\
                ['X','X','X','X',' ',' ',],\
                [' ','X','O',' ',' ','0',]]
    >>> win_horiz(6,'X',6,board)
    (True, [0, 1, 2, 3])
    >>> win_horiz(7,'O',6,board)
    (False, 0)
    """

    sum = 0
    winpos=[]
    for x in range(num_st):
        if board[i][x] == char:
            winpos += [x]
            sum += 1
            if sum == 4:
                return True, winpos
                break
        else:
            sum = 0
            winpos=[]
    if sum != 4:
        return False, 0
        
 
def win_vertical(j,board,char):
    """
    >>> board = [[' ','',' ',' ',' ',' ',],[' ','O',' ',' ',' ',' ',],\
                [' ','X',' ',' ',' ',' ',],[' ','O',' ',' ',' ',' ',],\
                [' ',' ','X',' ','X',' ',],[' ',' ',' ',' ','X',' ',],\
                [' ','0',' ',' ','X',' ',],[' ','X','O',' ','X','0',],]
    >>> win_vertical(5,board,'X')
    (True, [4, 5, 6, 7])
    >>> win_vertical(1,board,'O')
    (False, 0)
    >>> win_vertical(6,board,'X')
    (False, 0)
    """
    sum=0
    winpos=[]
    for i in range(8):
        if board[i][j-1] == char:
            winpos += [i]
            sum += 1
            if sum==4:
                return True, winpos
                break
        else:
            sum = 0
            winpos=[]
    if sum !=4:
        return False, 0




def win_diagn(board,char,num_st,i,j):
    """
    >>> board = [[' ',' ','O',' ',' ',' '],[' ','O',' ',' ',' ',' '],\
                [' ','X',' ',' ',' ',' '],[' ','O',' ',' ',' ',' '],\
                [' ',' ','X','O','X',' '],[' ','X','O','X',' ',' '],\
                [' ','0',' ',' ','X',' '],['O','X','O',' ','X','X']]
    >>> board[7][5]
    'X'
    >>> board[0][2]
    'O'
    >>> win_diagn(board,'0',6,7,0)
    (False, 0)
    >>> win_diagn(board,'X',6,7,5)
    (True, [[7, 5], [6, 4], [5, 3], [4, 2]])
    >>> win_diagn(board,'0',6,2,4) == 'X'
    False
    """
    i2 = i
    j2 = j
    pos = [i,j]
    while i <=7 and j >=0 :
        pos = [i,j]
        i += 1
        j -= 1
    sum= 0
    table =[]
    i = pos[0]
    j = pos[1]
    while i >=0 and j< num_st:
        if board[i][j] == char:
            sum += 1
            table += [[i,j]]
            if sum == 4:
                return True, table
                break
        else:
            table =[]
            sum=0
        i -= 1
        j += 1

    if sum != 4:
        i = i2
        j = j2
        pos = [i,j]
        while i <=7 and j < num_st :
            pos = [i,j]
            i += 1
            j += 1
        sum = 0
        table =[]
        i = pos[0]
        j = pos[1]
        while i >=0 and j >= 0:
            if board[i][j] == char:
                sum += 1
                table += [[i,j]]
                if sum == 4:
                    return True, table
                    break
            else:
                table =[]
                sum=0
            i -= 1
            j -= 1
    
    if sum != 4:
        return False, 0




def circle(board,winpos,case,char,i,j,num_st):
    """
    >>> board = [[' ',' ','O','X',' ',' '],[' ','O',' ',' ',' ',' '],\
                [' ','X',' ',' ',' ',' '],[' ','X',' ','O',' ',' '],\
                ['X','O','O','O','0','X'],[' ','O','O','X',' ','X'],\
                [' ','O','X','0','X','X'],['O','O','O',' ','X','X']]
    >>> winpos=[1,2,3,4]
    >>> circle(board,winpos,'horizontal','O',4,4,6)
    [[3, 1], [5, 1], [3, 2], [5, 2], [3, 3], [5, 3], [3, 4], [5, 4], [4, 0], [4, 5]]
    >>> winpos=[[7,0],[6,1],[5,2],[4,3]]
    >>> circle(board,winpos,'diagnal','O',7,0,6)
    [[6, 0], [6, 2], [5, 1], [5, 3], [7, 1], [4, 2], [4, 4], [3, 3]]
    >>> winpos=[7,6,5,4]
    >>> circle(board,winpos,'vertical','X',7,5,6) == [[7, 4], [6, 4], [5, 4], [4, 4], [5, 5]]
    True
    """
    if case == 'vertical':
        ls = []
        if j == 0:
            for k in range(4):
                ls += [[winpos[k],j+1]]
        elif j + 1 == num_st:
            for k in range(4):
                ls += [[winpos[k],j-1]]
        else:
            for k in range(4):
                ls += [[winpos[k],j+1]]
                ls += [[winpos[k],j-1]]

        if winpos[3] < 7:
            ls += [[winpos[3]+1,j]]
    elif case == 'horizontal':
        ls =[]
        if i == 7:
            for k in range(4):
                ls += [[i-1,winpos[k]]]
        elif i == 0:
            for k in range(4):
                ls += [[i+1,winpos[k]]]
        else:
            for k in range(4):
                ls += [[i-1,winpos[k]]]
                ls += [[i+1,winpos[k]]]
        
        if winpos[0] > 0:
            ls += [[i,winpos[0]-1]]
        
        if winpos[3] < num_st-1:
            ls += [[i,winpos[3]+1]]
    else:
        ls = []
        if winpos[1][1] == winpos[0][1] + 1:
            #diagnal
            for k in range(1,3):
                ls += [[winpos[k][0],winpos[k][1]-1]]
                ls += [[winpos[k][0],winpos[k][1]+1]]
            if winpos[0][1] == 0:
                ls += [[winpos[0][0],winpos[0][1]+1]]
                ls += [[winpos[3][0],winpos[3][1]-1]]
                ls += [[winpos[3][0],winpos[3][1]+1]]
                if winpos[3][0] > 0:
                    ls += [[winpos[3][0]-1,winpos[3][1]]]
                if winpos[0][0] < 7:
                    ls += [[winpos[0][0]+1,winpos[0][1]]]
            elif winpos[3][1] == num_st-1:
                ls += [[winpos[3][0],winpos[3][1]-1]]
                ls += [[winpos[0][0],winpos[0][1]-1]]
                ls += [[winpos[0][0],winpos[0][1]+1]]
                if winpos[0][0] < 7:
                    ls += [[winpos[0][0]+1,winpos[0][1]]]
                if winpos[3][0] > 0:
                    ls += [[winpos[3][0]-1,winpos[3][1]]]   
            elif winpos[3][0] == 0:
                ls += [[winpos[3][0],winpos[3][1]-1]]
                ls += [[winpos[3][0],winpos[3][1]+1]]
                ls += [[winpos[0][0],winpos[0][1]+1]]
                if winpos[0][1] > 0:
                    ls += [[winpos[0][0],winpos[0][1]-1]]   
            else:
                for k in range(0,4,3):
                    ls += [[winpos[k][0],winpos[k][1]-1]]
                    ls += [[winpos[k][0],winpos[k][1]+1]]
                if winpos[0][0] < 7:
                    ls += [[winpos[0][0]+1,winpos[0][1]]]
                if winpos[3][0] > 0:
                    ls += [[winpos[3][0]-1,winpos[3][1]]] 
        else:
            #inver diagnal
            for k in range(1,3):
                ls += [[winpos[k][0],winpos[k][1]-1]]
                ls += [[winpos[k][0],winpos[k][1]+1]]
            if winpos[3][1] == 0:
                ls += [[winpos[3][0],winpos[3][1]+1]]
                ls += [[winpos[0][0],winpos[0][1]-1]]
                ls += [[winpos[0][0],winpos[0][1]+1]]
                if winpos[3][0] > 0:
                    ls += [[winpos[3][0]-1,winpos[3][1]]]  
                if winpos[0][0] < 7:
                    ls += [[winpos[0][0]+1,winpos[0][1]]]
            elif winpos[0][1] == num_st-1:
                ls += [[winpos[0][0],winpos[0][1]-1]]
                ls += [[winpos[3][0],winpos[3][1]-1]]
                ls += [[winpos[3][0],winpos[3][1]+1]]
                if winpos[0][0] < 7:
                    ls += [[winpos[0][0]+1,winpos[0][1]]]
                if winpos[3][0] > 0:
                    ls += [[winpos[3][0]-1,winpos[3][1]]]   
            elif winpos[3][0] == 0:
                ls += [[winpos[3][0],winpos[3][1]-1]]
                ls += [[winpos[3][0],winpos[3][1]+1]]
                ls += [[winpos[0][0],winpos[0][1]-1]]
                if winpos[0][1] < num_st-1:
                    ls += [[winpos[0][0],winpos[0][1]+1]]   
            else:
                for k in range(0,4,3):
                    ls += [[winpos[k][0],winpos[k][1]-1]]
                    ls += [[winpos[k][0],winpos[k][1]+1]]
                if winpos[0][0] < 7:
                    ls += [[winpos[0][0]+1,winpos[0][1]]]
                if winpos[3][0] > 0:
                    ls += [[winpos[3][0]-1,winpos[3][1]]] 
    return ls

def slip(board,i,j):
    """
    >>> board = [['P','Y'],['T','H'],['O','N']]
    >>> slip(board,2,0)
    [[' ', 'Y'], ['P', 'H'], ['T', 'N']]
    >>> board = [['P','Y'],['T','H'],['O','N']]
    >>> slip(slip(board,2,0),2,1)
    [[' ', ' '], ['P', 'Y'], ['T', 'H']]
    >>> board = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
    >>> slip(board,2,3) == [[1, 1, 1, ' '], [2, 2, 2, 1], [3, 3, 3, 2], [4, 4, 4, 4]] 
    True
    """
    while i>0:
        if board[i-1][j] != ' ':
            board[i][j] = board[i-1][j]
            board[i-1][j] = ' '
            i -= 1
        else:
            board[i][j] = ' '
            break
    if i == 0 and board[i][j] != ' ': 
        board[i][j] = ' '

    return board



def status(player1,player2):        
    answer=input('Θέλετε να συνεχίσετε να παίζετε;(Πατήστε οτιδήποτε για ΝΑΙ ή Ο για ΟΧΙ);')
    if answer=='o' or answer=='O' :
        play=False
        if player1>player2:
            print('Νίκησε ο Παίκτης 1:','(',player1,'-',player2,')')
        elif player1<player2:
            print('Νίκησε ο Παίκτης 2:','(',player2,'-',player1,')')
        else:
            print('Ισοπαλία!!!')
        return False
    else:
        return True
        


def cont_save(board,score1,score2):
    print('Πατήστε οποιοδήποτε πλήκτρο για να συνεχίσετε,')
    ans=input('Για παύση του παιχνιδιού και αποθήκευση σε αρχείο επιλέξτε "s":')
    if ans=='s' or ans=='S':
        name = input('Δώσε όνομα αρχείου.')
        n_board = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    board[i][j]=0
                elif board[i][j] == 'O':
                    board[i][j]=1
                else:
                    board[i][j]=2
        n_board = board + [[score1,score2]]
        import csv

        with open(name+'.csv','w', newline='') as name:
            game_writer = csv.writer(name, quoting=csv.QUOTE_MINIMAL,delimiter=',')
            game_writer.writerows(n_board)

        return True
    else: 
        return False


def read_file():
    file_name=input('Δώσε όνομα αρχείου: ')
    from csv import reader

    with open(file_name+'.csv', 'r') as item:
        csv_reader = reader(item)
        board = list(csv_reader)

    score1 = board[-1][0]
    score2 = board[-1][1]

    board.pop(-1)

    length=len(board[0])

    for i in range(len(board)):
        for j in range(length):
            if board[i][j] == '0':
                board[i][j]=' '
            elif board[i][j] == '1':
                board[i][j]='O'
            else:
                board[i][j]='X'
    
    

    return board, int(score1) , int(score2)

    
    
##################################### MAIN ####################################

if game_menu() == 0:
    num_st = 0
    while num_st >10 or num_st < 5:
        num_st = int(input('Δώσε αριθμό στηλών (5-10):'))
    board = maketable(num_st)
    player1=0
    player2=0
else:
    board, player1, player2 = read_file()
    num_st = len(board[0])
    table(num_st,board)

play=True
skip = False
while play:
    win_h=False 
    win_d=False 
    win_v=False 
    end=True
    
    while (win_h != True and win_d != True and win_v != True) and end:
        
        if not skip: # gia na mhn xana paixei
            board , i , j = position(1,num_st,board)
            table(num_st,board)
            win_h , winpos_h = win_horiz(i,'O',num_st,board)  
            win_d , winpos_d = win_diagn(board,'O',num_st,i,j-1)
            win_v , winpos_v = win_vertical(j,board,'O')

            if win_h == True or win_v == True or win_d == True:
                player1 +=1
                char='O'
                skip = True 
                break
        skip = False

        board , i , j = position(2,num_st,board)
        table(num_st,board)
        win_h , winpos_h = win_horiz(i,'X',num_st,board) 
        win_d , winpos_d = win_diagn(board,'X',num_st,i,j-1)
        win_v , winpos_v = win_vertical(j,board,'X')

        if win_h == True or win_v == True or win_d == True:
            player2 +=1
            char='X'
            break

        end_sum=0
        if i == 0:
            for l in range(num_st):
                if board[0][l] != ' ':
                    end_sum += 1
        if end_sum == num_st or cont_save(board,player1,player2):
            end = False

    if end == False:
        break

    if win_h == True:
        for k in range(4):
            board[i][winpos_h[k]] = '*'
        table(num_st,board)

        
        temp=circle(board,winpos_h,'horizontal',char,i,j-1,num_st)

        ls = []
        for k in range(len(temp)):
            if board[temp[k][0]][temp[k][1]] == char:
                ls += [temp[k]]
        
        if i == 7:
            for k in range(len(ls)):
                board = slip(board,ls[k][0],ls[k][1])
            for k in range(4):
                board = slip(board,i,winpos_h[k])    
        elif i == 0:
            for k in range(4):
                board[i][winpos_h[k]] = ' '
            for k in range(len(ls)):
                board[ls[k][0]][ls[k][1]] = ' '
        else:
    
            for k in range(len(ls)):
                if i > ls[k][0]:
                    board = slip(board,ls[k][0],ls[k][1])

            for k in range(4):
                board = slip(board,i,winpos_h[k])

            for k in range(len(ls)):
                if i <= ls[k][0]:
                    board = slip(board,ls[k][0],ls[k][1])

        if char == 'O':
            player1 += len(ls)
        else:
            player2 += len(ls) 

        table(num_st,board)

        if not status(player1,player2):
            play=False
    elif win_d == True:

        for k in range(4):
            board[winpos_d[k][0]][winpos_d[k][1]] = '*'
        table(num_st,board)

        temp = circle(board,winpos_d,'diagnal',char,i,j-1,num_st)
    
        ls = []
        for k in range(len(temp)):
            if board[temp[k][0]][temp[k][1]] == char:
                ls += [temp[k]]

        for k in range(len(ls)):
            for l in range(4):
                if winpos_d[l][0] > ls[k][0]:
                    board = slip(board,ls[k][0],ls[k][1])

        for k in range(4):
            board = slip(board,winpos_d[k][0],winpos_d[k][1])

        for k in range(len(ls)):
            for l in range(4):
                if winpos_d[l][0] <= ls[k][0]:
                    board = slip(board,ls[k][0],ls[k][1])

        if char == 'O':
            player1 += len(ls)
        else:
            player2 += len(ls) 

        table(num_st,board)
        if not status(player1,player2):
            play=False
    elif win_v == True:
        for k in range(4):
            board[winpos_v[k]][j-1] = '*'
        table(num_st,board)
        

        temp = circle(board,winpos_v,'vertical',char,i,j-1,num_st)

        ls = []
        for k in range(len(temp)):
            if board[temp[k][0]][temp[k][1]] == char:
                ls += [temp[k]]

        for k in range(4):
            board[winpos_v[k]][j-1] = ' '


        for k in range(len(ls)):
            board = slip(board,ls[k][0],ls[k][1])

        if char == 'O':
            player1 += len(ls)
        else:
            player2 += len(ls) 

        table(num_st,board)
        if not status(player1,player2):
            play=False
    else:
        None
    



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    