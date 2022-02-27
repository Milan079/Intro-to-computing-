#################Question 1 ####################
def Tower_of_Hanoi(n,p,q,r):
     # p is source , q is helper , r is destination
    if n==1:
        print("move 1st disk from",p, "to" ,r)
        return
     # recursive call foer n-1 disk in which r act as helper
    Tower_of_Hanoi(n-1,p,r,q)
    print ("move", n,"th disk from ",p,"to", r)
    # recursive call foer n-1 disk in which p act as helper 
    Tower_of_Hanoi(n-1,q,p,r)                            
Tower_of_Hanoi(3,"source","helper","destination")     






##################Question 2 #############################
from math import factorial, remainder
from tracemalloc import start
n=int(input("Enter the size of pascal's triangle: "))

print("Using loop")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")                #for giving space 

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	      # nCr = n!/((n-r)!*r!)
	print()	                          #  for new line 
print("\n\n")

print("Using recursion")

def Pascal_Triangle(n,original_length=n):
    if n == 0:
        return
    Pascal_Triangle(n-1,original_length)
    #for giving spaces 
    print('  '*(original_length-n), end='')

    #We know first no is always 1 
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i                # using Binomial Coefficient                         

    print()
Pascal_Triangle(n)
print("\n")






###############Question 3 ##############
No_1, No_2 = map(int,input("Enter two numbers: ").split())
Quotient = No_1// No_2
Remainder = No_1 % No_2

#Part a
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#Part b
print("\n")
if (Quotient == 0):
    print("b. The quotient is zero\n")
if (Remainder == 0):
    print("b. The reminder is zero\n")
if (Quotient != 0 and Remainder != 0):
    print("b. All the values are non zero\n")

#Part c
list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f"c. Filtered out numbers that are greater than 4 are : {result}\n")

#Part d
Set_result = set(result)
print("d. Set:",Set_result)

#Part e
print("\n")
Immutable_Set = frozenset(Set_result)        #frozen Set is used to make the set immutable
print("e. Immutable set:",Immutable_Set)

#Part f
print("\n")
print("f. The maximum value from the set is :", max(Immutable_Set))
print(" Hash value of the max value from the above set:", hash(max(Immutable_Set)))
print("\n")







###############Question 4 ########################
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")
#creating object
student_1 = Student("Milan", 21103077) 
print("Object created")
#printing  the assigned values
print(f"The name of the student is {student_1.name} and SID is {student_1.roll_no}.")  
 #deleting object
del student_1 
print("\n")







#################Question 5 #######################
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#Creating records of the employee 
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)

#part a: Updating salary of Mehak 
employee_1.salary = 70000
print(f"a. The updated salary of {employee_1.name} is {employee_1.salary} ")
#part b: deleting a record of viren 
print("b. Record of Viren deleted", end='')
del employee_3
print("\n")







####################Question 6#################
#Input  word from the first friend
word =input("Enter the word: ")
word=word.lower()

#input a meaningful word with the exact same letters
other_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
other_word=other_word.lower()
#define dictionary
def count_in_dict(word):
    count = {}
    list_1 = list(word)
    
    n = len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(other_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()





#################END###############################


