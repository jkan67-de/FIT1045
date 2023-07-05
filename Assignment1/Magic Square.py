"Josh Kannemeyer 27845508"

def Inputfile():
        try:           
            InputMagicSquare=input('Enter file name: ')            # Input of folder name
            return MagicNumInput(InputMagicSquare)
    
        except (FileNotFoundError):                             # if invalid name then it will ask for another filename
            print("This file does not exist, try again")
            return Inputfile()

def MagicNumInput(InputMagicSquare):                                                                                 
    inputfile=open(InputMagicSquare,"r")
    Name=inputfile.name
    try:           
            Magicnumber=int(input("Enter magic number: "))                  # Input magic number
            return opening(Name,Magicnumber)             # send it to opening function
    except (ValueError):
            print("select an actual number please")
            return MagicNumInput(InputMagicSquare)

def opening(Name,Magicnumber):
    str=open(Name,'r').read()             # read file
    A=str.split()                        # make file a list
    return Setup(A,Magicnumber)     # send to Setup module to made into a matrix

def Setup(A,Magicnumber):
    D=int(len(A)**(0.5))
    i=0
    Matrix=[]                      # make list a matrix(list of lists)
    while i<len(A):
      Matrix.append(A[i:i+D])
      i+=D
    B=0                           # set a value to be the index values
    A=[int(i) for i in A]
    
    if (min(A)<0):          # check for negative values
        print("There is a negative in the magic square, therefore this is not a partial magic square")
        sys.exit()

    return Rowcheckintial(A,Matrix,D,B,Magicnumber)  #send to Rowcheckintial for rows be checked


def Rowcheckintial(A,Matrix,D,B,Magicnumber):

    Row=Matrix[B]                 # checking each list within the matrix
    
    Row = [int(i) for i in Row]

    print(Row)

    if(sum(Row)>Magicnumber):           # end if rule has been violated
        print("This is not a magic square")

    if(sum(Row)<=Magicnumber):
        B=B+1           
        if (B==D):
            B=0           # set index back to 0
            return Columncheckintial(D,Matrix,Magicnumber,B,A)  # send to Columncheckintial to check columns            
        return Rowcheckintial(A,Matrix,D,B,Magicnumber)    # loop to make it check each row


def Columncheckintial(D,Matrix,Magicnumber,B,A):
    Col=[]
    
    for j in range(0,D):          # checking each column within the matrix
        Col.append(Matrix[j][B])   

    Col = [int(i) for i in Col]
       
    if(sum(Col)>Magicnumber):               # end if rule has been violated
        print("This is not a magic square")

    if(sum(Col)<=Magicnumber):
        B=B+1
        if (B==D):
            B=0          # set index back to 0
            return Diagonalscheckintial(D,Magicnumber,Matrix,A,B)  # send to Diagonalscheckintial to check diagonals 
        return Columncheckintial(D,Matrix,Magicnumber,B,A)   # loop to make it check each column
    
def Diagonalscheckintial(D,Magicnumber,Matrix,A,B):
    
    E=[]                        # checking diagonal from left to right within the matrix
    for j in range(0,D):
        E.append(Matrix[j][j])
        E = [int(i) for i in E]

    if (sum(E)>Magicnumber):
        print("This is not a magic square")

    F=[]                       # checking diagonal from right to left within the matrix
    for j in range(-D,0):
        F.append(Matrix[j][-j-1])
        F = [int(i) for i in F]       
    
    if (sum(F)>Magicnumber):        # end if rule has been violated
        print("This is not a magic square")

    if (min(A)== 0):                # Send to Numberchange module to replace numbers
        print("This is a partial magic square")
        return Numberchange(Matrix,A,Magicnumber,D,B)

    if (min(A)> 0):                # send to be checked to check modules
        print("This may be a complete square, let me check")
        return CheckRow(Matrix,A,Magicnumber,D,B)

    

def Numberchange(Matrix,A,Magicnumber,D,B):           # selecting a cell to be changed
    try:
        print("The first row is one")
        R=int(input('select row of number you would like to replace:'))     # Input Row
        print("the first column is one")
        C=int(input('select column of number you would like to replace:'))  # Input Column

    except (ValueError):
        print("Enter in a proper value")
        return Numberchange(Matrix,A,Magicnumber,D,B)


    if (D<R or D<C or C<1 or R<1):                   # make sure cell exists
        print("please select cell that exists")
        return Numberchange(A,Matrix,Magicnumber,D,B)

    W=int(R-1)
    J=int(C-1)
    
    H=Matrix[W][J]

    H=int(H)


    if (H != 0):          # make sure the value selected is a zero element
        print("please select cell with a zero element")
        return Numberchange(Matrix,A,Magicnumber,D,B)

    if (H==0):
        N=int(input('enter in number:'))       # change the zero element
        O=(R-1)*D+C-1
        return Insertnumber(Matrix,A,Magicnumber,D,B,N,O)


def Insertnumber(Matrix,A,Magicnumber,D,B,N,O):    # new list made with new number
    A[O]=N 
    i=0
    Matrix=[]        # new matrix made
    while i<len(A):
      Matrix.append(A[i:i+D])
      i+=D
    
    return CheckRow(Matrix,A,Magicnumber,D,B,O) # sent to check rows


def CheckRow(Matrix,A,Magicnumber,D,B,O):   #Check new matrix rows
    
    Row=Matrix[B]
    
    Row = [int(i) for i in Row]

    print(Row)

    if (sum(Row)<=Magicnumber):
        B=B+1
        if (B==D):
            B=0
            return Checkcol(Matrix,A,Magicnumber,D,B,O)
        if ((sum(Row)<Magicnumber and min(Row)!=0)):   # check for a zero element in row
            return Wrongnumber(Matrix,A,Magicnumber,D,B,O)
            
        return CheckRow(Matrix,A,Magicnumber,D,B,O)

    if(sum(Row)>Magicnumber):
        return Wrongnumber(Matrix,A,Magicnumber,D,B,O)


def Checkcol(Matrix,A,Magicnumber,D,B,O):    #Check new matrix columns

    Col=[]
    
    for j in range(0,D):
        Col.append(Matrix[j][B])   

    Col = [int(i) for i in Col]

    if (sum(Col)<=Magicnumber):
        B=B+1
        if (B==D):
            B=0
            return CheckDiagonals(Matrix,A,Magicnumber,D,B,O)
        if ((sum(Col)<Magicnumber and min(Col)!=0)):            # check for a zero element in column
            return Wrongnumber(Matrix,A,Magicnumber,D,B,O)
        
        return Checkcol(Matrix,A,Magicnumber,D,B,O)
       
    if(sum(Col)>Magicnumber):
        return Wrongnumber(Matrix,A,Magicnumber,D,B,O)
        

def CheckDiagonals(Matrix,A,Magicnumber,D,B,O):   #Check new matrix diagonals
    E=[]

    for j in range(0,D):
        E.append(Matrix[j][j])
        E = [int(i) for i in E]


    if (sum(E)>Magicnumber or (sum(E)<Magicnumber and min(E)!=0)):  # check for a zero element in diagonal
        return Wrongnumber(Matrix,A,Magicnumber,D,B,O)

    F=[]
    for j in range(-D,0):
        F.append(Matrix[j][-j-1])
        F = [int(i) for i in F]       
    
    if (sum(F)>Magicnumber or (sum(F)<Magicnumber and min(F)!=0)):  # check for a zero element in diagonal
        return Wrongnumber(Matrix,A,Magicnumber,D,B,O)

    if(min(A)==0):     # send back to numberchange module to get rid of the zero cells 
        Numberchange(Matrix,A,Magicnumber,D,B)
        

    if (sum(F)==Magicnumber and sum(E)==Magicnumber):   #congratulate
        print("YAY YOU'VE MADE A MAGIC SQUARE")
        print("This is a complete magic square")
        sys.exit()

def Wrongnumber(Matrix,A,Magicnumber,D,B,O):    # reset the new number to 0 
    print("wrong! pick another number")
    A[O]=0 
    i=0
    Matrix=[]
    while i<len(A):
      Matrix.append(A[i:i+D])
      i+=D
    return Setup(A,Magicnumber)
        
    

Inputfile()     #call for first module



