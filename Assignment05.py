# ---------------------------------------------------------------------------#
# Title: Assignment05
# Desc: This assignment demonstrates data processing using dictionaries and exception handling
# Change Log: (Who, When, What)
#   MonishaGrover,11/11/2024,Created Script
# ---------------------------------------------------------------------------#

# Define the Data Constants
MENU:str ="""
    -----Course Registration Program------
    Select from the following menu:
    1. Register a student for a course
    2. Show current data
    3. Save data to a file
    4. Exit the program
    ---------------------------------------"
"""
FILE_NAME:str = "Enrollments.csv"

# Define the Data Variables
student_first_name:str=str()
student_last_name:str=str()
course_name:str=str()
csv_data:str=str()
file_obj = None
menu_choice:str=str()
student_data: dict[str,str]={}
#students:list[dict]=[]

student1:dict[str,str] = {"FirstName": "Vic", "LastName": "Vu","CourseName":"Python100"}
student2:dict[str,str] = {"FirstName": "Su", "LastName": "Salias","CourseName":"Python100"}
students = [student1,student2]
print(students)
file_obj = open(FILE_NAME,'w')
file_obj.close()
print("saved data success")

try:
    file_obj = open(FILE_NAME,'r')
    for each_row in file_obj.readlines():
        student_data = each_row.split(',')
        student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name.strip()}
        students.append(student_data)
    file_obj.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("----Technical error message----")
    print(e, e._doc_, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("----Technical error message----")
    print(e, e._doc_, type(e), sep='\n')
finally:
    if file_obj.closed == False:
        file_obj.close()

    # Input user data
while True:
    #Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do?")

    if menu_choice=='1':
      try:
        student_first_name = input("Enter your first name: ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")

        student_last_name = input("Enter your last name: ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")

        course_name = input("Enter your course name: ")
        if not course_name.isalnum():
            raise ValueError("The course name should be alphanumeric.")

        csv_data += (f"{student_first_name},{student_last_name},{course_name}\
                \n")
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
        students.append(student_data)

      except Exception as e :
        print('This is a technical error')
        print(e, type(e))

      finally:
        if file_obj.closed==False:
            file_obj.close()

    elif menu_choice == '2':
        print(csv_data)
        print(students)
        continue

    elif menu_choice == '3':
        try:
            file_obj = open(FILE_NAME, "w")
            for student in students:
                file_obj.write(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n')
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("----Technical error message----")
            print(e, e._doc_, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("----Technical error message----")
            print(e, e._doc_, type(e), sep='\n')

        finally:
            file_obj.close()

        print("Wrote to file successfully")
        continue

    elif menu_choice == '4':
        break

    else:
        print("Enter correct menu choice")

