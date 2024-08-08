from student import Student

welcome = """
=================================================
       Welcome to Learning Nest 
=================================================       
Please select option for:

1. Registration
2. Student detail
3. Total Student

"""


if __name__ == "__main__":
    print(welcome)
    value = True
    while value:
        option = int(input())
        if option == 1:
            s1 = Student()
            s1.add()
        elif option == 2:
            print(Student.students)
        else:
            value = False
