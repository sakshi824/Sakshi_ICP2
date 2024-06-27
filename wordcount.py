def wordcount(): #Declaring the function
        fileinput= open("C:/Users/pothu/OneDrive/Documents/Divya_neural_deep/input_files.txt", "r")#Getting the input file
        fileoutput= open("C:/Users/pothu/OneDrive/Documents/Divya_neural_deep/output_files.txt", "w")#Writing the outout file
        inputting_data = fileinput.readlines()#for reading the input file
        fileoutput.writelines(inputting_data)#for writing the data
        #Displaying the word count
        fileoutput.write("The word count of input file is : ")
        
        dict={}
        for i in inputting_data:# for lines
            words = i.strip().split(" ")    #for words splitting
            #print(i,words)      
            for j in words:
                separate= "\n" +j + " "+str(words.count(j))  #to separate the word and count their occurence
                print(separate)             
                fileoutput.write(separate)# writing to output file
        
wordcount()