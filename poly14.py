
first_name = (input('student name:'))
surname = (input('student surname:'))
exam_mark = int(input('exam_mark:'))

if (exam_mark <= 100)and(exam_mark >= 80):
    print(first_name,surname,"oustanding")
elif (exam_mark <= 79)and(exam_mark >= 60):
    print(first_name, surname, "Satisfactory")
elif(exam_mark <= 59)and(exam_mark >= 50):
    print(first_name, surname, "Pass")
elif(exam_mark <= 49)and(exam_mark >= 40):
    print(first_name, surname, "Fail")
elif(exam_mark > 100):
    print(first_name,surname,"please re-enter mark")
