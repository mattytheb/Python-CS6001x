# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:51:51 2017

Matthew Barker@ Portsmouth Uni Library
"""
def count_digits(cc): 
    """ cc, credit card number, long long
        Returns the number of diigits in a crdit card
    """
       
    digits= len(str(cc))
    return digits


def first_digits(cc): 
    """ cc, credit card number, long long
        
        Returns the first 2 digits in the cc
    """
    number=str(cc)
    
    return int(number[0:2])


def check_sum(cc): 
    """ cc, credit card number, long long
        digits, no of digits in cc
        Returns true or false if the card is valid
    """
    
    A1=list(str(cc))    #turn cc into a list
    
    A1.reverse()        # reverse list
    
    A1 = [int(i) for i in A1]   #turn str into int
    
    sum_even=sum(A1[::2])
    
    A2=[]
    for i in A1[1::2]:
        A2.append(i * 2)
    
    #print(A2)
    str1 = ''.join(str(e) for e in A2)    #convert list to string
    #print(str1)
    odd_digits = [ int(char) for char in str(str1) ] #convert string to list
    #print(odd_digits)
    sum_odd=sum(odd_digits)
    #print(sum_odd)
    
    
    
    total=sum_odd+sum_even
    
    x=total%10
    
    if x==0:
        return True
    if x!=0:
        return False
    
def main():
    
    cc=input("Enter your credit card number to validate:")
    
    digits=count_digits(cc)
        
    checkSum=check_sum(cc)
    
    #print(digits)
    #print(checkSum)
    
    if checkSum==False:
        print("INVALID")
    
    elif checkSum==True:
        if digits==15:
            check=first_digits(cc)
            
            if check==34 or check==37:
                print("AMEX")
                
            else:
                print("INVALID")
                
        elif digits==16:
            check=first_digits(cc)
            
            if check==51 or check==52 or check==53 or check==54 or check==55:
                print("MASTERCARD")
                
            elif check==40 or check==41 or check==42 or check==43 or check==44 or check==45 or check==46 or check==47 or check==48 or check==49:
                print("VISA")
                
            else:
                print("INVALID")
                
        elif digits==13:
            check=first_digits(cc)
            
            if check==40 or check==41 or check==42 or check==43 or check==44 or check==45 or check==46 or check==47 or check==48 or check==49:
                print("VISA")
                
            else:
                print("INVALID")
                
        else:
            print("INVALID")
                   
    
    
if __name__=="__main__":
    main()