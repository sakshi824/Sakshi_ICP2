# Sakshi_ICP
# Assignment2
STUDENT INFO: 
Name: Sakshi Jadhav
ID:700757772
Video link:https://drive.google.com/file/d/1m8tKXm9jBNZbxl9fazp807mtlsp8uyA-/view?usp=share_link

1. Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
fullname function that should return the (full name).
o For example:
▪ First_name = “your first name”, last_name = “your last name”
▪ Full_name = “your full name”
o Write function named “string_alternative” that returns every other char in the full_name string.
Str = “Good evening”
Output: Go vnn

SOLUTION:
Entering the first name and last name form the user and combining these values into the fullname and then displaying the fullname
<img width="701" alt="image" src="https://user-images.githubusercontent.com/122486644/213361498-e482fa53-3ca4-4809-84ad-d845422ecee7.png">

For string alteration it will take the fullname from the function and then returns the alternative values by using the slicing operator.
<img width="752" alt="image" src="https://user-images.githubusercontent.com/122486644/213362070-222f9321-86fd-4fd6-94dc-b8d3d062a7b5.png">


2.. Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
o Finally store the output in output.txt file.
 Example:
Input: a file includes two lines:
 Python Course
 Deep Learning Course
 Output:
Python Course
 Deep Learning Course
Word_Count:
 Python: 1
Course: 2
Deep: 1
Learning: 1

SOLUTION:opening the file by using the open() function and giving tha path of the files of both input and output files
<img width="252" alt="image" src="https://user-images.githubusercontent.com/122486644/213363132-1b9459b2-1f6d-4aa4-9a6c-a699eb835bd0.png">

<img width="350" alt="image" src="https://user-images.githubusercontent.com/122486644/213362867-e68e1c4f-86ab-4ad1-a2a5-64d702d07af3.png">
Then reading the file by using the readlines() function and writing the data by using writelines() function
then splitting the sentance by using the split() function and then separting then printing the words.

3.3. Write a program, which reads heights (inches.) customers into a list and convert these heights to
centimeters in a separate list using:
1) Nested Interactive loop.
2) List comprehensions
Example: L1: [150,155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]

<img width="672" alt="image" src="https://user-images.githubusercontent.com/122486644/213366388-03568dbd-5d2e-4aee-a414-1406bae91c81.png">
using list for declaring the values and then appending the values then using the for loop an d then list comphersion
