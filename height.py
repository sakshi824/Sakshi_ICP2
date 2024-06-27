def convertinginchestocm():
    list=[110,115, 135, 146]#Declaring the list
    e=[]#empty list
    for items in list: #for loop
        e.append(items*2.54) # appending
    print("output for loop",e)
    #For list comprehension
    print("output for List Comprehension",[items*2.54 for items in list])
    
convertinginchestocm()
