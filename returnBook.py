'''This module consists a return function to return books.'''

from datetime import datetime   #importing datetime function
import listdt   #importing listdt module  
import borrow   #importing borrow module

def returnBook():   #defining function for return book process

    global name     #declaring name as global variable 

    total = 0
    
    books_name=[]   #creating empty list to store books name
    
    listb_r=[]  #creating empty list to store 
    
    file = open("stock.txt","r")    #opening and reading stock text file
    
    for each in file:
        
        listb_r.append(each.replace("\n","").split(","))    #replacing " " with ,
        
    file.close()

    name = input("\n Enter the name or ID by which you borrowed the book : ") #asking user input for name
    
    borrow_note="Borrow - " +name+ ".txt"
    
    try:  #test the code for errors
        
        with open(borrow_note,"r") as f:   #opening and reading borrow text file
            
            lines = f.readlines()   #reading all lines at a single go
            
            lines = [borrow_note.strip("$") for borrow_note in lines] 
    
        with open(borrow_note,"r") as f:  #opening and reading borrow text file
            
            data = f.read()     #reads borrow text file data
            
            print(" ")
            
            print(data)     #prints the data
            
    except:  # catch any error and handle it
        
        print("\n No borrower with this name !!! ")   #prints if the name doesnot exists
        
        returnBook()  

    returnbook = True   #declaring and assigning returnbook variable with boolean
    
    while returnbook == True:  #to check the boolean variable for loop
        
        try:   #to detect error occurred
            
            enter_id = input("\n Enter the ID of the book you want to return : ")  #asking for user input
            
            num = int(enter_id)   #converting string to integer
            
            books = listb_r[num-1][0]   #decreasing the input by 1
        
            #stores books name
            for i in range(len(listb_r)):
                
                if books.upper()== listb_r[i][0].upper():
                    
                    listb_r[i][2] = int(listb_r[i][2])+1
                    
                    books_name.append(books+" \t\t "+listb_r[i][1]+" \t\t"+ "$ "+listb_r[i][-1])   #add books to books_name list

                    total = float(total) + float(listb_r[i][-1])
                    
                    break
        
            again_return = input("\n Do you want to return more books?(Y/N):")   #asking for user input
            
            if again_return == "Y" or again_return == "y":
                
                returnbook = True
                
            else:
                
                returnbook = False
                
        except:         #catch any error and handle
            
            print("\n Invalid ID !!!")
            
    # create and write the texts in the return text file to print the return receipt        
    file = open("Return - " +name+ ".txt","w")  #opening and writing for return text file
    file.write("                 INGCollege Library            ")  #write the text in return text file
    file.write("\n")
    file.write("                   Return Receipt              ")
    file.write("\n")
    file.write(" Name : " +name)    #writes the name
    file.write("\n")
    file.write(" Returned date : " +str(datetime.now().date()))   #writes the date and time in text file
    file.write("\n")
    file.write("S.N \t Book Name \t\t  Author \t\tPrice \n")

    for i in range(len(books_name)):
        sn = i+1 
        file.write(str(sn))
        file.write(" ")
        file.write(" \t "+str(books_name[i])+"\n")  #writes the books listed in books_name list
    file.close()

    #adding fine and total calculation in the return text file         
    file = open("Return - " +name+ ".txt","a")   #opening an adding fine, total in the return text file
    
    extra = 0
    
    no_days = False  #assigning number of days with boolean
    
    while no_days == False:
        
        try:   #checking error
            
            days = int(input("\n Enter the number of days since you borrowed books : "))  #asking for user input
            
            no_days = True
            
        except:   #handling error
            
            print("\n Invalid !!! ")
       
    #calculation for fine 
    if days<10:   
        file.write(" ")
        file.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t         Total : $ "+str(total))  #write the total amount in file
        print("\n No Fine charged !!! ")
    else:
        extra = days -10  #calculating extra number of days
        file.write("\n")
        file.write(" ------------------ Late submission by  "+str(extra)+ " days !!! ----------------------- "+"\n")
        file.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t      Fine : $ 2 per day"+"\n")   
        file.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t      Total fine : "+" $ " + str(extra*2)+"\n")  #calculating fine per day and write in th file
        file.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t      Grand Total : "+" $ "+str(total+(extra*2))+"\n")  #calculating total sum and writing in the file   
    file.write("")
    file.close()   #close the opened file
    
    #displays the return text file data 
    file = open("Return - " +name+ ".txt","r")  
    print("---------------------------------------------------------------------")
    for each in file:
        print(each)
    print("---------------------------------------------------------------------")
    print("         Thank you for visiting !!! Hope to see you soon !!!       \n ")
    file.close()
    
    #creating and writing a return details file to store information for librarian
    file = open("Return Details - "+name+ ".txt","w")
    file.write("        **Details stored for the librarian**       "+"\n\n")
    file.write(" Borrowed by : "+name+"\n")
    file.write(" Return Status : Yes"+"\n")
    file.write(" Returned date : "+str(datetime.now().date())+"\n\n")
    file.write("\t Book Name \t\t  Author \t\tPrice \n")
    
    for i in range(len(books_name)):
        file.write(str("\t"+books_name[i]+"\n"))
    file.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t      Payment : $ "+str(total+(extra*2)))
    file.close()
    
    #the quantity of the stock text file is overwritten and new data is written
    file = open("stock.txt","w")
    for i in range(len(listb_r)):
        final_list = (listb_r[i][0]+","+listb_r[i][1]+","+(str(listb_r[i][2]))+","+listb_r[i][3]+"\n")
        file.write(final_list)
    file.close()




                
    
        
        
        


