# Simple program 1
# grade calculator

student_name = str(input("What is the name of the student?"))

exam1 = int(input("Enter the grade for the first exam (0-100)"))
exam2 = int(input("Enter the grade for the second exam (0-100)"))
final = int(input("Enter the grade for the final exam (0-100)"))

total = float(20*(exam1/100)) + (20*(exam2/100)) + (60*(final/100))

print ("The final grade for " + student_name + " is " + str(total) + " out of 100")


