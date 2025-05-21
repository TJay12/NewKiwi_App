# pyinstaller --onefile NewKiwi_App.py
import logging
import traceback
import datetime

# Error Logging
logging.basicConfig(
    filename="logging.txt",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# <--- Dictionary to Store Values from File --->
students = {

}

# <--- Function to Read File and Store Values in Dictionary --->
def import_data():
    # Loop input if file not found
    while True:
        file = input("Open File: ")
        students.clear()
        logging.info("students dictionary cleared")
        try:
            with open(file, "r") as file:
                all_lines = file.readlines()
            # Exit loop when file opened successfully
            break
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")
            logging.warning(f"File not found: {file}")

    logging.info(f"File loaded successfully: {file.name}")
    # Loop through lines in file, split up information,
    # and add student info to dictionary
    for line in all_lines:
        line = line.strip()
        split = line.rsplit(",", 2)
        student, mid_score, end_score = split
        student_id, student_name1, student_name2 = student.split(" ")
        students[student_id] = {"first_name": student_name1, "last_name": student_name2,
                                "mid_score": int(mid_score), "end_score": int(end_score)}
    logging.info(f"Imported {len(students)} students")

# <--- Function to Calculate The Average Score for Each Student and Add to Dictionary --->
def calculate_final_score():

    # Loop through all students take their mid-score and end-score from dictionary,
    # calculate average and add to dictionary.
    for stud_id, student_data in students.items():
        score_average = (student_data['mid_score'] + student_data['end_score']) / 2
        students[stud_id]['avg_score'] = float(score_average)
    logging.info(f"Successfully calculated final scores for {len(students)} students")

# <--- Function to Assign Grade based on Average Score for Each Student and Add to Dictionary --->
def assign_grade():
    # Loop through all students, take their average score from dictionary,
    # assign grade based on average score and add to dictionary.
    for stud_id, student_data in students.items():
        stud_grade = student_data['avg_score']
        if stud_grade >= 90:
            grade = "A"
        elif stud_grade >= 80:
            grade = "B"
        elif stud_grade >= 70:
            grade = "C"
        elif stud_grade >= 60:
            grade = "D"
        else:
            grade = "F"
        students[stud_id]['grade'] = grade
    logging.info(f"Grades assigned successfully for {len(students)} students")

# <--- Function to Calculate the Grade Totals for All Students --->
def total_grade_count():

    # Set up tuple for storage
    all_grades = "",
    # Loop through all students and take their grade from dictionary
    # 'add' grade to tuple (create new tuple with the old data plus the next grade)
    for stud_id, stud_data in students.items():
        stud_grade = stud_data['grade']
        all_grades += stud_grade,
    # Count how many of each letter (grade) is in final tuple,
    # and store in a list
    grade_count = [all_grades.count("A"), all_grades.count("B"), all_grades.count("C"),
                   all_grades.count("D"), all_grades.count("F")]
    logging.info(f"Grade totals counted: A={grade_count[0]}, B={grade_count[1]}, "
                 f"C={grade_count[2]}, D={grade_count[3]}, F={grade_count[4]}")
    return grade_count

# <--- Function to Print Full Report with Scores, Grades and Total Grade Count --->
def print_report(grade_count):

    print(f"{'-' * 51}")
    print(f"| {'Students Scores and Grade':^47} |")
    print(f"{'-' * 51}")

    print(f"| {'ID':<8} {'Name':<14} {'Mid':^5} {'End':^5} {'Avg':<5} {'Grade':<5} |")
    print(f"{'-' * 51}")
    for stud_id, stud_data in students.items():
        stud_name = f"{stud_data['first_name']} {stud_data['last_name']}"
        print(f"| {stud_id:<8} {stud_name:<14} {stud_data['mid_score']:^5} "
              f"{stud_data['end_score']:^5} {stud_data['avg_score']:^5.1f} {stud_data['grade']:^5} |")

    print(f"{'-' * 51}")
    print(f"| {'Students Total Grade Count':^47} |")
    print(f"{'-' * 51}")
    print(f"|{'A = '+str(grade_count[0]):^16}{'C = '+str(grade_count[2]):^17}"
          f"{'F = '+str(grade_count[4]):^16}|\n"
          f"|{'B = '+str(grade_count[1]):^16}{'D = '+str(grade_count[3]):^17}{' ' * 16}|")
    print(f"{'-' * 51}")
    logging.info("Report printed without errors")

# <--- Main Function to Run all Functions in Correct Order--->
def main():
    import_data()
    calculate_final_score()
    assign_grade()
    grade_count = total_grade_count()
    print_report(grade_count)
    input("\nPress Enter to exit...")

# <--- Run Program or Write Error Log --->
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_message = f"An error occurred: \n{traceback.format_exc()}"
        logging.error(error_message)
        input("An error occurred. Check logging.txt for details.\nPress Enter to exit...")