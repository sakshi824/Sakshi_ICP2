your_firstname=input("Enter your first name ") #for entering first name
your_lastname=input("Enter your last name ") # for entering lastname
#function for fullname
def fullname(your_firstname,your_lastname):
    global your_fullname
    your_fullname=your_firstname+" "+your_lastname #combining the first and last name
    print("Your fullname is " + your_fullname) #printing the fullname
fullname(your_firstname,your_lastname) #calling the fucntion
