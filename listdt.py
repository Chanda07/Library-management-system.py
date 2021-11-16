'''This module consists function to store stock in list'''

def listb():  #defining listb function
    
    l1=[]  #creating empty list to save data
    
    read = open("stock.txt","r")  #reading stock text file
    
    for i in read:
        
        l1.append(i.replace('\n',"").split(","))  #add and replace "" with ,
        
    read.close()
    
    return l1  
    
