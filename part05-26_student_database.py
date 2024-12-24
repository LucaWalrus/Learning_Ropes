# Write your solution here

def add_student(database: dict, name: str):
    """Adds a new student to the database with no courses initially."""
    if name not in database:
        # Initialize with an empty list of courses
        database[name] = []

def print_student(database: dict, name: str):
    """Prints the student's information."""
    if name in database:
        courses = database[name]
        if courses:
            # If the student has courses, print the courses and average grade
            print(f'{name}:')
            print(f' {len(courses)} completed courses:')
            total_grade = 0
            for course in courses:
                print(f'  {course[0]} {course[1]}')
                total_grade += course[1]
            avg_grade = total_grade / len(courses)
            print(f' average grade {avg_grade:.1f}')
        else:
            print(f'{name}: \n no completed courses')
    else:
        print(f'{name}: no such person in the database')

def add_course(database: dict, name: str, result: tuple):
    """Adds a completed course for a student, ensuring the course is not repeated with a lower grade, and ignoring grade 0."""
    if name in database:
        course_name, grade = result
        if grade == 0:
            return  # Simply return and do not add the course if the grade is 0

        # Check if the course is already in the database
        for course in database[name]:
            if course[0] == course_name:
                # If the course already exists, don't lower the grade
                if course[1] < grade:
                    database[name].remove(course)
                    database[name].append(result)
                return
        
        # If the course is not repeated, add the course
        database[name].append(result)

def summary(database: dict):
    """Prints a summary of the database."""
    num_students = len(database)
    most_courses_student = None
    most_courses_count = 0
    best_avg_student = None
    best_avg_grade = 0

    for name, courses in database.items():
        num_courses = len(courses)
        total_grade = sum(course[1] for course in courses)
        avg_grade = total_grade / num_courses if num_courses > 0 else 0

        # Check if this student has the most courses
        if num_courses > most_courses_count:
            most_courses_count = num_courses
            most_courses_student = name

        # Check if this student has the best average grade
        if avg_grade > best_avg_grade:
            best_avg_grade = avg_grade
            best_avg_student = name

    print(f"students {num_students}")
    if most_courses_student:
        print(f"most courses completed {most_courses_count} {most_courses_student}")
    if best_avg_student:
        print(f"best average grade {best_avg_grade:.1f} {best_avg_student}")
