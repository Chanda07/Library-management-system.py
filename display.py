'''This module consists function to display the books list in a certain way'''

import listdt #importing listdt module


def display(l1):  #defining display function and calling l1 from listdt
    
    print("------------------------------------------------------------------------------------")
    print(" ID "+"\t"+"  BookName  "+"\t\t"+"Author's Name  "+"\t"+"    Quantity "+"\t\t"+"Price ")
    print("------------------------------------------------------------------------------------")
    
    counter = 1
    
    file=open("Stock.txt", "r") #reading stock text file
    
    for disp in file:
        
        x=disp.replace(",","\t\t")
        
        print(counter,"\t",x)
        
        counter = counter+1
        
    print("------------------------------------------------------------------------------------")

    
 
