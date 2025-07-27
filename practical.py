
#1
courses = {
    "CS101": ("AI", 3),
    "Math01": ("Calculus ", 4),
    "ENG150": ("English ", 2),
    "00P110": ("OOP", 3)
}
#2
students = {}

def add_student(name, enrolled_course_codes):
    students[name] = enrolled_course_codes
print("*************************************")
#3
def display_all_courses():
    print("All Courses Offered:")
    for code, details in courses.items():
        print("Course Code:", code)
        print("Course Info:", details)  # This will show the tuple directly
        print("-----------")


#4
def display_student_enrollments():
    print("Student Enrollments:")

    for student in students:
        print("Student:", student)
        print("Courses Enrolled:")

        for code in students[student]:
            if code in courses:
                course_name = courses[code][0]
                credit_hours = courses[code][1]
                print("  Course Code:", code)
                print("  Course Name:", course_name)
                print("  Credit Hours:", credit_hours)
            else:
                print("  Course Code:", code)
                print("  Course Not Found")
        print("-----------")



#5
def display_unique_enrolled_courses():
    unique_courses = set()

    for course_list in students.values():
        for code in course_list:
            unique_courses.add(code)

    print("Unique Enrolled Courses:")

    for code in unique_courses:
        if code in courses:
            name = courses[code][0]
            credits = courses[code][1]
            print("Course Code:", code)
            print("Course Name:", name)
            print("Credit Hours:", credits)
        else:
            print("Course Code:", code)
            print("Course not found")
        print("-----------")


#6
def calculate_total_credits(student_name):
    if student_name not in students:
        print(f"\nStudent {student_name} not found.")
        return

    total_credits = 0
    print(f"\nCalculating credit hours for {student_name}...")

    for code in students[student_name]:
        if code in courses:
            credit = courses[code][1]  # Access credit hours directly
            print(f"  Course Code: {code}, Credit Hours: {credit}")
            total_credits += credit
        else:
            print(f"  Course Code: {code} not found. Skipping.")

    print(f"\nTotal credit hours for {student_name}: {total_credits}")



add_student("Ali", ["CS101", "Math01"])
add_student("Tuba", ["ENG150", "00P110", "CS101"])

#fuction calls
display_all_courses()
print("*************************************")
display_student_enrollments()
print("*************************************")
display_unique_enrolled_courses()
print("*************************************")
calculate_total_credits("Ali")
