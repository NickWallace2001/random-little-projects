#calulate your term GPA

#set qp according to letter grade
def getqp(grade, credit):
    if grade == "A":
        qp = 4*credit
    elif grade == "B+":
        qp = 3.5*credit
    elif grade == "B":
        qp = 3*credit
    elif grade == "C+":
        qp = 2.5*credit
    elif grade == "C":
        qp = 2*credit
    elif grade == "D+":
        qp = 1.5*credit
    elif grade == "D":
        qp = 1*credit
    elif grade == "F":
        qp = 0*credit
    return qp

print("Please only enter classes that effect your GPA")
number_of_classes = int(input("How many classes are you taking? "))

#total credits and quailty points
totalc = 0
totalqp = 0

#gather info
for i in range(number_of_classes):
    grade = input("What is your letter grade for your class?(E.x. B, B+) ")
    credit = input("How many credits is this class worth? ")
    totalc += int(credit)
    n = getqp(grade.upper(), int(credit))
    totalqp += n

#calculate and print term gpa
gpa = format(totalqp/totalc, ".3f")
print("Your term GPA is: " + str(gpa))
