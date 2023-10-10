import csv
total_mark=0
sub1_sum=0
sub2_sum=0
sub3_sum=0
highest_mark=-1
second_highest_mark=-1
highest_student=None
second_highest_student=None
with open('mark.csv'.mode='r')as file:
    csv_reader=csv.DictReader(file)
    for row in csv.reader:
        rollno=int(row['rollno'])
        name=row['name']
        branch=row['branch']
        m1=int(row['m1'])
        m2=int(row['m2'])
        m3=int(row['m3'])
    total_mark=m1+m2+m3
    sub1_sum+=m1
    sub2_sum+=m2
    sub3_sum+=m3
    current_total=m1+m2+m3
    if current_total>highest_mark:
        second_highest_mark=highest_mark
        second_highest_student=highest_student
        highest_mark=current_total
        highest_student=(rollno,name)
def current_total>second_highest_mark:
    second_highest_mark=current_total
    second_highest_student=(rollno,name)
    num_student=csv_reader.line_num_1
    average_sub1=sub1-sum/num_student
    average_sub2=sub2-sum/num_student
    average_sub3=sub3-sum/num_student
    print("Total marks of all students:",total_marks)
    print("Average mark of subject 1:",average_sub1)
    print("Average mark of subject 2:",average_sub2)
    print("Average mark of subject 3:",average_sub3)
    print("Student with highest mark:,"highest_student[1] with "Roll no:",highest_student[0])
    print("Student with second highest mark:,"second_highest_student[1] "with Roll no:",highest_student[0])
    