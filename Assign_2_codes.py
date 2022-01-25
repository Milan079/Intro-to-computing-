#Ques1: Write Python codes for the following on the string 


#Define the string
string = "Python is a case sensitive language"

#Part a: print length of string
length_of_string=len(string)
print("Part a: Length of the string = ",length_of_string)

#Part b: Reverse the order of string in one line code
reverse_string=string[::-1]
print("Part b: Here's the reverse order =\n",reverse_string)

#Part c: using slice function store "a case sensitive" in new string
new_string = slice(10,26)
print("Part c: Here's the new string = ", string[new_string])

#Part d: Replace "a case sensitive" with "object oriented"
replace_string=string.replace("a case sensitive", " object oriented")
print("Part d: Here's the replacement = ",replace_string)

#Part e: Index of "a"
index_of_a=sentence.find("a")
print("Part e: Here's the index of 'a' =", index_of_a)

#Part f: Remove white spaces
remove_spaces=string.replace(" ","")
print("Part f: Here's the string without white spaces:",remove_spaces)


#Q1 completed
##############################################

#Ques 2: Store your name, SID, department name and CGPA into different variables. 
# With the help of String formatting print the following output.


#Takes input from user
Name = input("Enter your name : ")
SID = input("Enter your SID : ")
Department = input("Enter your dept. : ")
CGPA = input("Enter your CGPA : ")

#Printing the statement with with given format by string formatting
print("Hey, %s Here! \nMy SID is %s \nI am from %s department and my CGPA is %s" %(name, SID, department, CGPA))



#Q2 completed
#################################################




#Ques 3: For a=56 and b=10 with the help of bitwise operators calculate the following

#Define variable with given values 
a = 56
b = 10 

#Part a: a&b
print("Part a: a&b = ", a&b)

#Part b: a|b
print("Part b: a|b = ", a|b)

#Part c: a^b
print("Part c: a^b = ", a^b)

#Part d: Left shift both a and b with 2 bits
print("Part d: Left shift a = ", a << 2)
print("Part d: Left shift b = ", b << 2)

#Part e: Right shift both a with 2 bits and b with 4 bits
print("Part e: Right shift a = ", a >> 2)
print("Part e: Right shift b = ", b >> 4)


#Q3 completed
#####################################################



#Ques 4: Write a python program to find the greatest of three numbers entered by the user. 

#Take inputs from user
#User inputs three number
num_1 = int(input("enter the no. 1:  "))
num_2 = int(input("enter the no. 2 :  "))
num_3 = int(input("enter the no. 3:  "))

#Using if-else to find the largest number
if num_1>=num_2:
  if num_1>=num_3:
      print("Largest no. is : ",num_1)
  else :
      print("Largest no. is : ",num_3)
else :
  if num_2>=num_3:
      print("Largest no. is : ",num_2)
  else :
      print("Largest no. is : ",num_3)
#Q4 completed
##################################################



#Ques 5: Write a python program to check if the word “name” is present in 
#the string entered by the user (Print : “Yes” or “No”).


#Take input from user
input_statement = str(input("Please type a statement:\n"))

#Condition to find "name"
if "name" in statement:
    print("Yes")
else:
    print("No")

#Q5 completed
####################################################

    

#Ques 6: Program to find if triangle exists or not. 


#Take inputs from user for three sides of a triangle:
side_1 = int(input("Enter first side:\n"))
side_2 = int(input("Enter second side:\n"))
side_3 = int(input("Enter third side:\n"))

#Putting conditions using if else
if side_1 + side_2 < side_3:
    print("No")
elif side_2 + side_3 < side_1:
    print("No")
elif side_1 + side_3 < side_2:
    print("No")
else:
    print("Yes")  

#Q6 completed 
#################################################
#################################################
