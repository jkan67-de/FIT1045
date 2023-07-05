"Josh Kannemeyer 27845508"


def Inputn():
    print("This number n will give you n+1 terms of the continued fraction for e") 
    "n for number"
    n=int(input("Enter in a value greater or equal to 0: "))                        # number of iterations input
    "t for terms"
    t=n+1                                                   # number of terms being used in the continued fraction
    
    if (n<0):
        print("please select a positive integer or zero")   # make sure positive or zero input
        return Inputn()
        
    if (n>=0):
        return Calculations(n,t)                            # values sent to the Calculations Module
        


def Calculations(n,t):
    "D for denominator"
    D=n+(n/(n+1))                                                                              # set up first term

    while(n>=0):

        if(n==0):
            print("The approximation for e with 1 term of the continued fraction is: 3")
            break

        if (n==1):                                                                                          # make sure n+1 terms are used in the continued fraction
            D=1/D
            ND=2+D                                                                                           # add 2, as the Calculations module only works out the decimal component 
            print("The approximation for e with "+str(t)+" terms of the continued fraction is: "+str(ND))    # print the approxiamtion and the number of terms in the continued fraction
            break
        

        D=(n-1)/D                                                                                         # create reciprocal 
        "ND for New Denominator"
        ND=(n-1)+D                                                                                         # sets up the next denominator
        
        n=n-1                                                                                              # start next iteration
        
        D=ND                                                                                               # calculated variable becomes new denominator
       
       
print("This is a program to approximate e")
Inputn()






