'''This module consists the borrow function where user can borrow books'''

import listdt  #importing listdt module
import datetime   #importing datetime

def borrowBook(l1):  #defining borrowBook function for borrowing process and calling l1 from listdt
   
   listbb = []   #creating empty list to store borrowed details
   
   total = 0     #declaring total for calculation
   
   name = input("\n Please enter the name or ID by which you want to borrow books : ")   #asking user input
   
   que_= "y" or "Y"   #initializing variable for question
   
   while que_ == "y" or que_ == "Y":
      
      check = True    #declaring and assigning check variable with boolean
      
      while check == True:
         
          id_select = input("\n Enter the ID of the book you want to borrow : ")   #asking user input
          
          if id_select == "1" or id_select == "2" or id_select == "3" or id_select == "4" or id_select == "5":   #user input options
             
             for i in range(len(l1)):
                
                 if int(id_select)-1 == i:
                    
                    file = open("Borrow - " +name+ ".txt","w")   #opening and writing borrow receipt details 
                    file.write("                 INGCollege Library            ")
                    file.write("\n")
                    file.write("                   Borrow  Receipt              ")
                    file.write("\n")
                    file.write(" Name : " +name)
                    file.write("\n")
                    file.write(" Borrowed date : " +str(datetime.datetime.now()))
                    file.write("\n")
                    file.write("S.N \t Book Name \t\t  Author \t\tPrice \n")
                    
                    if int(l1[i][2])>0:    #checking if quantity is available
                       
                       l1[i][2] = int(l1[i][2])-1   #decreasing quantity if book is borrowed
                       
                    else:
                       
                       print( " \n The requested book is out of stock. ")

                       break
                       
                    check = False
                    
                    listbb.append(  "      " +  l1[i][0]   +   "\t\t"   +  l1[i][1]  +  "\t\t"   +    " $ "  +    l1[i][3]  +'\n')   #adding borrowed book details in the text file
                    
                    total = float(total) + float(l1[i][3])  #calculating the total amount of the books borrowed
                    
                    return_ = (datetime.datetime.now().date() + datetime.timedelta(days = 10))  #setting return day for 10 days
                    
                    #writing borrowed book details in the file
                    for i in range(len(listbb)):
                      chooseb = i+1
                      file.write(str(chooseb))
                      file.write("")
                      file.write(str(listbb[i]))
                      
                    file.write("\n")
                    file.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t         Total : $ "+str(total))
                    file.write("\n\n")
                    file.write(" ***Note: Please return the books within 10 days i.e " +str(return_)+".")
                    file.close()
                    
                    #overwriting return details by new details
                    returndetails = open("Return Details - "+name+ ".txt","w")
                    returndetails.write("        **Details stored for the librarian**       "+"\n\n")
                    returndetails.write(" Borrowed by : "+name+"\n\n")
                    returndetails.write(" Return Status : No "+"\n\n")
                    returndetails.write(" To be returned within : " +str(return_)+"\n\n")
                    returndetails.write("\t Book Name \t\t  Author \t\tPrice \n"+"\n")
                    
                    for i in range(len(listbb)):
                      returndetails.write(str(listbb[i]))  #writing list stored in list
                    returndetails.write("\t\t \t \t\t \t\t\t\t\t\t\t \t\t\t         Total : $ "+str(total)+"\n")
                    returndetails.close()
          else:
                print("\n Invalid ID !!!")
                
                check = True
                
      #asking user input for borrowing more books       
      que_ = input("\n Do you want to borrow more books? (y/n) : ")
      
      if que_.lower() == "y":   # if user input is yes
         
         ids = input("\n Enter the ID of the book you want to borrow : ")  #asking user input for ID of the book
         
         if ids == id_select:   #if the new id is same as the id_select then print a message
            
            print("\n Same book cannot be borrowed twice !!! ")

            break
         
         else:

            print("\n Please re-enter the ID if you are certain !!! ")
         
            
         check = False
         
   #displays the borrow text file data
   file = open("Borrow - " +name+ ".txt","r")
   print("---------------------------------------------------------------------")
   for each in file:   
      print(each)
   print("---------------------------------------------------------------------")
   print("         Thank you for visiting !!! Hope to see you soon !!!       \n ")
   file.close()

   ##the quantity of the stock text file is overwritten and new data is written
   file = open("stock.txt","w")
   for i in range(len(l1)):
      end_list = l1[i][0]+","+l1[i][1]+","+(str(l1[i][2]))+","+l1[i][3]+'\n'
      file.write(end_list)
   file.close()


