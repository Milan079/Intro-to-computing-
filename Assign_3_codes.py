#Question 1
#Asking user for the  input-----------
sentence = str(input("Please Enter the statement- "))

#count occurences of words incase of whitespace character is detected
if " " in sentence: 
    #split at the spaces and store words in a list
    sentence_list = sentence.split()
    sentence_dict = {}
    #store list items as a dictionary with key = word, occurence = value
    for word in sentence_list:
        if word in sentence_dict:
            sentence_dict[word] += 1
        else:
            sentence_dict[word] = 1
    #pretty print dictionary for better readability
    import pprint
    pprint.pprint(sentence_dict)
#if no whitespace detected: find occurences of letters
else: 
    sentence_dict = {}
    #store each character in dictionary with key = character, value = occurence
    for chr in sentence:
        if chr in sentence_dict:
            sentence_dict[chr] += 1
        else:
            sentence_dict[chr] = 1
    #pretty print the dictionary
    import pprint
    pprint.pprint(sentence_dict)

#----------------------------------------------------

#Question 2 

#Taking input of date from the user-------
Day=int(input('Please enter a Day - '))
Month=int(input('Please enter Month - '))
Year=int(input('Please enter Year - '))


#Eliminating  all the invalid cases
if Day>30 and Month in {2,4,6,9,11}:
    condition=False
elif Day>31 and Month in {1,3,5,7,8,10,12}:
    condition=False
elif (Day==29 or Day==30) and Month==2 and Year%4!=0:
    condition=False
elif Day==30 and Month==2 and Year%4==0:
    condition=False
else:
    condition=True

#After checking condition, following code executes (if-else)
if condition:
    #checking and changing for new year
    if Day==31 and Month==12:
        New_Year=Year+1
    else:
        New_Year=Year
    if Month==12 and Day==31:
        New_Month=1
    else:
        New_Month=Month
#changing dates
    #checking for months with 31 days
    if Month in {1,3,5,7,8,10,12}:
        if Day==31:
            Next_Day=1
            if Month!=12:
                New_Month=Month+1
            else:
                New_Month=1
        else:
            Next_Day=Day+1
    #checking for the month of february
    elif Month==2:
        if Year%4==0:
            if Day==29:
                Next_Day=1
                New_Month=3
            else:
                Next_Day=Day+1
        else:
            if Day==28:
                Next_Day=1
                New_Month=3
            else:
                Next_Day=Day+1
                    
    #covering all the remaining cases
    else:
        if Day==30:
            Next_Day=1
            New_Month=Month+1
        else:
            Next_Day=Day+1
    #printing the calculations
    print(f"Next Date is: {Next_Day}/{New_Month}/{New_Year}")
else:
    #gives a warning and ends the program
    print("Invalid date")


#----------------------------------------------------

#Question 3

#Ask user for input of integers
Input_number = str(input("Enter the list of numbers (separated with space): \n "))

#Converting string input to list
number_List = Input_number.split()

#Converting each item of list to integer (string till now)
for i in range(len(number_List)):
    number_List[i] = int(number_List[i])

#Forming tuples and storing it in a list
number_squarelist = [(number_List[i], number_List[i]**2) for i in range(len(number_List))]

print(number_squarelist)


#----------------------------------------------------
#Question 4

#Take input from the user 
input_Grade_point = int(input("Enter Grade Point - "))

#if-else to check if input is in range
if (4 <= input_Grade_point <= 10):
     Grade_points = [4,5,6,7,8,9,10]
    
     ind = Grade_points.index(input_Grade_point)
      
     Grade_letter = ["D", "C", "C+", "B", "B+", "A", "A+"]
     Grade_performance = ["Poor", "Below Average", "Average", "Good", "Very Good", "Excellent", "Outstanding"]
      
     print ("Your grade is '%s' and %s Performance" % (Grade_letter[ind], Grade_performance[ind]))
else:
    print("Grade Point is Out of Range")


#----------------------------------------------------

#Question 5
    
#Make list of alphabets
Alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

#if-else to print inverted pyramid
for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(Alphabets_list[counter], end="")
            counter=counter+1
        column=column+1
    print("")

#----------------------------------------------------
#Question 6

#Use if-else to ask if the user wants to input student details or not
Student_dict = {}
while True:
    decision = input("Type Y to enter student details, otherwise type N: ")
    if decision == 'Y' or decision == 'y':
        name = str(input("Enter the name:"))
        sid = int(input("Enter the SID:"))
        Student_dict[sid] = name
    elif decision == "N" or decision == 'n':
        print("Program Input Mode ended.")
        break
    continue

#Ans a)
print("Ans a")
print("Details of students - ")
for key,value in Student_dict.items():
    print(f"SID = {key}, Name = {value}")
print("")

#Ans b)
print("Ans b")
Val_sort_dict= sorted(Student_dict.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

#Ans c)
print("Ans c")
Key_sort_dict= sorted(Student_dict.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

#Ans d)
print("Ans D")

# Ask for user input for SID to be finded
SID_find = int(input("Please enter the student's SID whose detail you need- "))

if SID_find in Student_dict.keys():
    print(f"Name of the required student is {Student_dict[SID_find]}")
else:
    print("The SID is not present in the given Data")
print("")

#----------------------------------------------------

#Question 7

#Asking input from the user 
number_of_elements=int(input("No of elements in the fibonnaci series (must be greater than 1)- "))


#using the formula of the sum of previous two terms is equal to the present term.
first_term=0
second_term=1
n=0
#initializing sum with first two terms
sum=first_term+second_term

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {number_of_elements} terms")
print(first_term)
print(second_term)

#Printing the remaining fibonnaci terms
while n<number_of_elements-2:
    next_term=first_term+second_term
    first_term=second_term
    second_term=next_term
    print(next_term)
    n=n+1
    sum+=next_term
average=sum/number_of_elements
#printing the program end prompt
print(f"Average of total {number_of_elements} terms of sequence is {average}")
print("END")

#----------------------------------------------------

#Question 8


Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#Finding symmetric difference of both the sets
print("Part a")
set_notboth=Set1^Set2
print(f"set with elements not common in both is {set_notboth}")

#Finding symmetric difference of all sets
print("Part b")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

#Finding elements that is common in any two sets
print("Part C")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

#Finding elements common in set1 and range 1 to 10
print("Part d")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

#Finding elements common in sets 1,2,3 and range 1 to 10
print("Part e")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")

#----------------------------------------------------
