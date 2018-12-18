import errors

try:
    import tkinter  # Python 3
except ImportError:
    import Tkinter as tkinter  # Python 2

name = ""
faculty = ""
department = ""
matric_num = ""
course_codes = []
course_grades = []
course_units = []
course_results = []
num_of_courses = 0
grades = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

# Initialization of the variables so they can be used in a for-loop by the function create_entry
cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10, cc11, cc12 = (" " * 12)
g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12 = (" " * 12)
u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12 = (" " * 12)

# Placing the variables in a list so that they can be iterated over
course_code_variables = [cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10, cc11, cc12]
course_grade_variables = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
course_unit_variables = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12]

# Geometries based on how many courses are being offered
geo_key = 0
geo = {"2": "250x180+450+200",
       "3": "250x200+450+200",
       "4": "250x220+450+200",
       "5": "250x240+450+200",
       "6": "250x260+450+200",
       "7": "250x280+450+200",
       "8": "250x300+450+200",
       "9": "250x320+450+200",
       "10": "250x340+450+200",
       "11": "250x360+450+200",
       "12": "250x380+450+200"
       }


def create_entry(variables_list, window, result_list, column):
    for i in range(num_of_courses):
        variables_list[i] = tkinter.Entry(window, width=10)
        position_entry(variables_list[i], i + 1, column, result_list)


def position_entry(entry_variable, row, column, result_list):
    entry_variable.grid(row=row, column=column, sticky='ew')
    result_list.append(entry_variable)


def get_results():
    global course_results

    course_results.clear()  # Clearing the list to avoid remnant details from the previous call of get_results()
    for i in range(len(course_codes)):
        course_code = course_codes[i].get()
        course_grade = course_grades[i].get()
        course_unit = course_units[i].get()

        # Error handling of the result details gotten from the user
        if course_code.isalnum():
            if course_grade in grades:
                if course_unit.isdigit() and int(course_unit) in range(2, 7):
                    result = (course_code, course_grade, int(course_unit))
                    course_results.append(result)
                    # Checking to make sure this is the last result i.e the last iteration through the loop
                    if i == range(len(course_codes))[-1]:
                        mainWindow.destroy()
                else:
                    errors.input_error("a valid unit between 2 and 6!")
            else:
                errors.input_error("a valid grade!")
        else:
            errors.input_error("valid course code!")


def display_results(result_list, frame):
    for result in result_list:
        location = result_list.index(result)
        for i in range(len(result)):
            detail = tkinter.StringVar()
            detail.set(result[i])
            tkinter.Label(frame, textvariable=detail).grid(row=location + 1, column=i)


def calculate_gp(result_list):
    total_quality_points = 0
    total_units = 0
    for result in result_list:
        total_quality_points += grades[result[1]] * result[2]
        total_units += result[2]
    gpa = total_quality_points / total_units
    gpa = round(gpa, 2)
    return gpa


def create_input_window():
    def get_course_number():
        nonlocal answer
        global num_of_courses
        global geo_key

        num_of_courses = int(answer.get())  # Handle the error of the user not inputting anything
        if num_of_courses in range(2, 13):
            geo_key = answer.get()
            input_window.destroy()
        else:
            errors.input_error("value between 2 and 12")

    input_window = tkinter.Tk()
    input_window.title("")
    input_window.geometry("200x80+550+300")

    question_label = tkinter.Label(input_window, text="How many courses are you offering?")
    question_label.grid(row=0, column=0)

    answer = tkinter.Entry(input_window)
    answer.grid(row=1, column=0)

    submit_button = tkinter.Button(input_window, text="Submit", command=get_course_number)
    submit_button.grid(row=3, column=0)

    input_window.minsize(width=200, height=80)
    input_window.maxsize(width=200, height=80)

    input_window.mainloop()


def submit():
    global name
    global faculty
    global department
    global matric_num

    name = name_entry.get()
    faculty = faculty_entry.get()
    department = department_entry.get()
    matric_num = matric_num_entry.get()
    if not name:
        errors.detail_error("name")
    elif not faculty:
        errors.detail_error("faculty")
    elif not department:
        errors.detail_error("department")
    elif not matric_num:
        errors.detail_error("matric no.")
    else:
        get_results()


# Prompt the user for how many courses they are offering
create_input_window()

# =======================================================
mainWindow = tkinter.Tk()
mainWindow.title("GPA Calculator")
mainWindow.geometry(geo[geo_key])
mainWindow["padx"] = 15

# Frame for the details
details_frame = tkinter.Frame(mainWindow)
details_frame.grid(row=0, column=0, sticky="ew")

entry_frame = tkinter.Frame(details_frame)
entry_frame.grid(row=0, column=1, rowspan=4, sticky='ew')

# Detail labels and entries
name_label = tkinter.Label(details_frame, text="Name:")
name_label.grid(row=0, column=0, sticky='w')

name_entry = tkinter.Entry(entry_frame, width=20)
name_entry.grid(row=0, column=0)

faculty_label = tkinter.Label(details_frame, text="Faculty:")
faculty_label.grid(row=1, column=0, sticky='w')

faculty_entry = tkinter.Entry(entry_frame)
faculty_entry.grid(row=1, column=0, sticky='ew')

department_label = tkinter.Label(details_frame, text="Department:")
department_label.grid(row=2, column=0, sticky='w')

department_entry = tkinter.Entry(entry_frame)
department_entry.grid(row=2, column=0, sticky='ew')

matric_num_label = tkinter.Label(details_frame, text="Matric Number:")
matric_num_label.grid(row=3, column=0, sticky='w')

matric_num_entry = tkinter.Entry(entry_frame)
matric_num_entry.grid(row=3, column=0, sticky='ew')

# Entry box frame
entry_box_frame = tkinter.Frame(mainWindow)
entry_box_frame.grid(row=1, column=0, sticky='ew')

course_code_label = tkinter.Label(entry_box_frame, text="Course Code")
course_code_label.grid(row=0, column=0)

course_grade_label = tkinter.Label(entry_box_frame, text="Grade")
course_grade_label.grid(row=0, column=1)

course_unit_label = tkinter.Label(entry_box_frame, text="Unit")
course_unit_label.grid(row=0, column=2)

# Course Code entry boxes
create_entry(course_code_variables, entry_box_frame, course_codes, 0)

# Grade entry boxes
create_entry(course_grade_variables, entry_box_frame, course_grades, 1)

# Unit entry boxes
create_entry(course_unit_variables, entry_box_frame, course_units, 2)

# Submit Button
calculate = tkinter.Button(mainWindow, text="Submit", command=submit)
calculate.grid(row=2, column=0, sticky='ew')

mainWindow.maxsize(width=int(geo[geo_key][:3]), height=int(geo[geo_key][4:7]))
mainWindow.minsize(width=int(geo[geo_key][:3]), height=int(geo[geo_key][4:7]))
mainWindow.mainloop()

print(course_results)
# ==========================================================================================

# Display Window

displayWindow = tkinter.Tk()
displayWindow.title("My GPA Calculator")
displayWindow.geometry(geo[geo_key])
displayWindow["padx"] = 15
displayWindow["pady"] = 15

# Frame for detail labels
details_frame2 = tkinter.Frame(displayWindow)
details_frame2.grid(row=0, column=0)
details_frame2.config(relief="sunken", borderwidth=1)

# User Details and labels
name_var = tkinter.StringVar()
name_var.set(name)

name_label = tkinter.Label(details_frame2, text="Name:")
name_label.grid(row=0, column=0, sticky='w')

name_label_display = tkinter.Label(details_frame2, textvariable=name_var)
name_label_display.grid(row=0, column=1, sticky='w')

faculty_var = tkinter.StringVar()
faculty_var.set(faculty)

faculty_label = tkinter.Label(details_frame2, text="Faculty:")
faculty_label.grid(row=1, column=0, sticky='w')

faculty_label_display = tkinter.Label(details_frame2, textvariable=faculty_var)
faculty_label_display.grid(row=1, column=1, sticky='w')

department_var = tkinter.StringVar()
department_var.set(department)

department_label = tkinter.Label(details_frame2, text="Department:")
department_label.grid(row=2, column=0, sticky='w')

department_label_display = tkinter.Label(details_frame2, textvariable=department_var)
department_label_display.grid(row=2, column=1, sticky='w')

matric_num_var = tkinter.StringVar()
matric_num_var.set(matric_num)

matric_num_label = tkinter.Label(details_frame2, text="Matric Number:")
matric_num_label.grid(row=3, column=0, sticky='w')

matric_num_label_display = tkinter.Label(details_frame2, textvariable=matric_num_var)
matric_num_label_display.grid(row=3, column=1, sticky='w')

# Entry box frame
entry_box_frame = tkinter.Frame(displayWindow)
entry_box_frame.grid(row=1, column=0, sticky='eW')
entry_box_frame.config(relief="sunken", borderwidth=1)

course_code_label = tkinter.Label(entry_box_frame, text="Course Code")
course_code_label.grid(row=0, column=0)

course_grade_label = tkinter.Label(entry_box_frame, text="Grade")
course_grade_label.grid(row=0, column=1)

course_unit_label = tkinter.Label(entry_box_frame, text="Unit")
course_unit_label.grid(row=0, column=2)

# Result labels
display_results(course_results, entry_box_frame)

# GPA label frame
gp_frame = tkinter.Frame(displayWindow)
gp_frame.grid(row=2, column=0)
gp_frame.config(relief="raised", borderwidth=1)

gp = tkinter.IntVar()
gp.set(calculate_gp(course_results))

gp_label = tkinter.Label(gp_frame, text="GPA:")
gp_label.grid(row=0, column=0)

gp_display = tkinter.Label(gp_frame, textvariable=gp)
gp_display.grid(row=0, column=1)

displayWindow.update()
displayWindow.minsize(width=details_frame2.winfo_width() + 30, height=entry_box_frame.winfo_height() + details_frame2.winfo_height() + 40)
displayWindow.maxsize(width=details_frame2.winfo_width() + 30, height=entry_box_frame.winfo_height() + details_frame2.winfo_height() + 40)

displayWindow.mainloop()
