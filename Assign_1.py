#Question 1 
number_1=int(input("Enter the no 1: "))
number_2=int(input("Enter the no 2: "))
number_3=int(input("Enter the no 3: "))

#Average
average=(number_1+number_2+number_3)/3
print("The average of numbers are: " ,average) 



#Question 2
#All values are in $
standard_deduction=10000
dependent_deduction=3000
gross_income=int(input("Enter your income : "))
no_of_dependents=int(input("Enter the no of dependents : "))
taxable_income=gross_income-int(standard_deduction)-(int(dependent_deduction)*no_of_dependents)
tax=(taxable_income*0.2)
if taxable_income<0:
    print("No need to pay the tax")
else:
    print(float(tax))


#Question 3
Name=input("Enter your  name: ")
SID=input("Enter your student id: ")
Gender=input("Enter your gender: ")
Course_name=input("Enter your course name: ")
CGPA=float(input("Enter your CGPA: "))
STUDENT=[SID , Name , Gender , Course_name , CGPA]
print(STUDENT)
 

#Question 4
Student_1_marks = int(input("Enter student 1 marks: "))
Student_2_marks = int(input("Enter student 2 marks: "))
Student_3_marks = int(input("Enter student 3 marks: "))
Student_4_marks = int(input("Enter student 4 marks: "))
Student_5_marks = int(input("Enter student 5 marks: "))
my_list = [Student_1_marks, Student_2_marks, Student_3_marks, Student_4_marks, Student_5_marks]
print(my_list)
x = my_list.sort()
print("sorted list of students marks : " ,my_list)



#Question 5
#(a)

color_list=['Red','Green','White','Black','Pink','Yellow']
color_list.remove("Black")
print(color_list)


#b
color_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_list[3:5]=['Purple']
print(color_list)










