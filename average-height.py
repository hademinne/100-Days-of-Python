# you are going to write a program that calculate the average student height from a
#list of heights . students_hieghts=[180,124,165,173,189,169,146]


student_hieghts =input('Input a list of student heights').split()
for n in range(0,len(student_hieghts)):
    student_hieghts[n]=int(student_hieghts[n])
print(student_hieghts)

total_student =0
for student in student_hieghts:
    total_student +=1

print(total_student)

total_height=0
for height in student_hieghts:
    total_height+=height
print(total_height)
print(total_height/total_student)