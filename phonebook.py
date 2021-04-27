import sys

def contact_storing(temp):
   file = open("./contact.txt","a")
   file.write(temp)
   file.close

def contact_deleting():
   file = open("./contact.txt","w")
   file.close

def contact_printing():
   file = open("./contact.txt","r")
   print(file.read())
   file.close

def check_if_string_in_file(string_to_search):
    #""" Check if any line in the file contains given string """
    # Open the file in read only mode
    with open("./contact.txt", 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False

def test (string1):
    file1 = open("./contact.txt", "r")
    
    # setting flag and index to 0
    flag = 0
    index = 0
    
    # Loop through the file line by line
    for line in file1:  
        index+=1 
        
        # checking string is present in line or not
        if string1 in line:
            flag=1
            break 
            
    # checking condition for string found or not
    if flag == 0: 
        return -1 
    else: 
        return index
    
    # closing text file    
    file1.close() 
  
def initial_phonebook():      

    print("\nEnter contact details in the following order" )
    print("NOTE: * indicates mandatory fields")
    print("....................................................................")
    temp_name=input("Enter name*: ")
    contact_storing("Enter name*: "+temp_name+"\n")
    temp_number=input("Enter number*: ")
    contact_storing("Enter number*: "+temp_number+"\n\n")
    
  
def menu():
    print("********************************************************************")
    print("\t\t\tPHONEBOOK DIRECTORY")
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice
   
def delete_all():
    print("\t\tdeleting Contacts\n")
    contact_deleting()
    print("All contacts deleted")

  
def search_existing():
    choice_t=int(input("enter your choice \n 1 for searching by name \n 2 for searching by number\n"))
    if(choice_t==1):
        print("Please enter the name")
        s=input()
        index=test("Enter name*: "+s)
        if(index==-1):
            print("Name not present")
        else:
            file = open("./contact.txt")
            # read the content of the file opened
            content = file.readlines()
            print(content[index-1])
            print(content[index])
    elif(choice_t==2):
        print("Please enter the number")
        s=input()
        index=test("Enter number you want to search: "+s)
        if(index==-1):
            print("Number you are searching for is not present in phonebook")
        else:
            file = open("./contact.txt")
            # read the content of the file opened
            content = file.readlines()
            print(content[index-2])
            print(content[index-1])
    else:
        print("Invalid choice")
      

def display_all():
    print("\t\tContact List\n")
    contact_printing()

def thanks():
    print("********************************************************************")
    print("Thank you for using our phonebook directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")
  
# Main function code
print("....................................................................")
print("Hello dear user, welcome to our phonebook directory system")
print("You may now proceed to explore this directory")
print("....................................................................")
ch = 0
while (True):
    ch = menu()
    if ch == 1:
        initial_phonebook()
    elif ch == 2:
        pass
    elif ch == 3:
        delete_all()
    elif ch == 4:
       search_existing()
    elif ch == 5:
        display_all()
    elif ch == 6:
        break
    else:
        print("Invalid Choice")
thanks()