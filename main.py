'''This module consists a function to carry out the borrow
and return process by importing the modules and calling the functions.'''

import listdt  #importing listdt module
import borrow   #importing borrow module
import returnBook  #importing returnbook module
import display   #importing display module

def menu():  #defining menu function to access main menu
    print("\n")
    print("                        Welcome                  ")
    print("")
    print("              ING Library Management System       ")
    print(" ")
    print(" Choose from the option below: ")
    print(" ")
    print("1. Show Books ")
    print(" ")
    print("2. Borrow Books ")
    print(" ")
    print("3. Return Books ")
    print(" ")
    print("4. Exit ")

    check = True #assigning check variable with boolean
    
    while check == True:
        
        enter = input("\n Choose from 1 to 4 : ")  #asking user input
        
        if (enter == "1"):      #if user input is 1 then it displays all the books list
            
            with open("stock.txt","r") as f:  #reading stock text file
                
                lines = f.read()   #read stock text file
                
                display.display(listdt.listb())   #calling display function and listb form listdt module

                print()
                
        elif(enter == "2"):  #if user input is 2 then borrow process is generated
            
            display.display(listdt.listb())  ##calling display function and listb form listdt module
            
            borrow.borrowBook(listdt.listb())  #calling borrowBook function form borrow module
            
        elif(enter == "3"):   #if user input is 3 then book returning process is generated
            
            display.display(listdt.listb())  ##calling display function and listb form listdt module
            
            returnBook.returnBook()   #calling returnBook function form returnBook module
            
        elif(enter == "4"):  #if user input is 4 then it exits the library
            
            print("\n Thank you for visiting INGCollege Library !!! ")
            
            exit
            
            check = False
        else:
            
            print("\n Invalid choice !!! ")
            
            check = True

menu()  #calling menu function                  
