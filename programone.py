

lloyd = {"name":"lloyd" ,
      "homework" :[100, 92, 98, 100] ,
      "quizzes" :[100, 70, 85, 95] ,
      "test" : [0, 87, 75, 70]}

alice = {"name": "alice",
      "homework" :[100, 70, 85, 95] ,
      "quizzes" : [100, 92, 98, 100] ,
      "test": [0, 87, 75, 70]}

tyler = {"name":"tyler" ,
      "homework" :[0, 87, 75, 70],
      "quizzes" :[100, 92, 98, 100],
      "test": [100, 70, 85, 95]}

students = [lloyd , alice, tyler]


for student in students:
    print (student["name"])
    print (student["homework"])
    print (student["quizzes"])
    print (student["test"])

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["test"])
    total = homework * .1 + quizzes * .3 + tests * .6
    return total

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print (get_letter_grade(get_average(lloyd)))


    
        
    


