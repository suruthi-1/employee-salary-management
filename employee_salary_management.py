import tkinter as tk
from tkinter import messagebox


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("Employee Salary Management System")
root.geometry("1000x700")
root.resizable(False, False)

# Colors
BG_COLOR = "#EAF2F8"
HEADER_COLOR = "#163A5F"
BLUE = "#2471A3"
DARK_BLUE = "#154360"
GREEN = "#229954"
RED = "#C0392B"
WHITE = "#FFFFFF"
TEXT = "#1B2631"
LIGHT_BLUE = "#D6EAF8"


# ============================================================
# VARIABLES
# ============================================================

employee_id = tk.StringVar()
employee_name = tk.StringVar()
department = tk.StringVar()
basic_salary = tk.StringVar()

result_employee_id = tk.StringVar()
result_name = tk.StringVar()
result_department = tk.StringVar()
result_basic = tk.StringVar()
result_bonus = tk.StringVar()
result_deduction = tk.StringVar()
result_net = tk.StringVar()


# ============================================================
# PAGE FRAME
# ============================================================

dashboard_page = tk.Frame(root, bg=BG_COLOR)
result_page = tk.Frame(root, bg=BG_COLOR)

dashboard_page.place(x=0, y=0, width=1000, height=700)
result_page.place(x=0, y=0, width=1000, height=700)


# ============================================================
# PAGE SWITCH FUNCTION
# ============================================================

def show_dashboard():
    dashboard_page.tkraise()


def show_result():
    result_page.tkraise()


# ============================================================
# CLEAR FORM
# ============================================================

def clear_form():

    employee_id.set("")
    employee_name.set("")
    department.set("")
    basic_salary.set("")


# ============================================================
# CALCULATE SALARY
# ============================================================

def calculate_salary():

    emp_id = employee_id.get().strip()
    name = employee_name.get().strip()
    dept = department.get().strip()
    salary_text = basic_salary.get().strip()

    # Validation
    if emp_id == "" or name == "" or dept == "" or salary_text == "":
        messagebox.showwarning(
            "Missing Details",
            "Please enter all employee details."
        )
        return

    try:
        salary = float(salary_text)

        if salary <= 0:
            messagebox.showwarning(
                "Invalid Salary",
                "Salary must be greater than zero."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid salary amount."
        )
        return

    # Salary calculation
    bonus = salary * 0.10
    deduction = salary * 0.05
    net_salary = salary + bonus - deduction

    # Send values to result page
    result_employee_id.set(emp_id)
    result_name.set(name)
    result_department.set(dept)
    result_basic.set(f"₹ {salary:,.2f}")
    result_bonus.set(f"₹ {bonus:,.2f}")
    result_deduction.set(f"₹ {deduction:,.2f}")
    result_net.set(f"₹ {net_salary:,.2f}")

    show_result()


# ============================================================
# ===================== DASHBOARD PAGE =======================
# ============================================================

# Header
dashboard_header = tk.Frame(
    dashboard_page,
    bg=HEADER_COLOR,
    height=110
)

dashboard_header.pack(fill="x")

tk.Label(
    dashboard_header,
    text="👨‍💼 EMPLOYEE SALARY",
    font=("Arial", 28, "bold"),
    bg=HEADER_COLOR,
    fg=WHITE
).pack(pady=(20, 0))

tk.Label(
    dashboard_header,
    text="MANAGEMENT SYSTEM",
    font=("Arial", 16),
    bg=HEADER_COLOR,
    fg="#AED6F1"
).pack()


# Dashboard title
tk.Label(
    dashboard_page,
    text="Employee Dashboard",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TEXT
).pack(pady=(35, 20))


# Form card
form_card = tk.Frame(
    dashboard_page,
    bg=WHITE,
    width=700,
    height=400
)

form_card.pack()
form_card.pack_propagate(False)


# Function for labels
def create_input(label_text, variable, row):

    tk.Label(
        form_card,
        text=label_text,
        font=("Arial", 14, "bold"),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=row,
        column=0,
        padx=30,
        pady=15,
        sticky="w"
    )

    entry = tk.Entry(
        form_card,
        textvariable=variable,
        font=("Arial", 14),
        width=38,
        bg="#F4F6F7",
        fg=TEXT,
        relief="solid",
        bd=1
    )

    entry.grid(
        row=row,
        column=1,
        padx=20,
        pady=15
    )


create_input(
    "Employee ID",
    employee_id,
    0
)

create_input(
    "Employee Name",
    employee_name,
    1
)

create_input(
    "Department",
    department,
    2
)

create_input(
    "Basic Salary",
    basic_salary,
    3
)


# Buttons
button_frame = tk.Frame(
    dashboard_page,
    bg=BG_COLOR
)

button_frame.pack(pady=30)


calculate_button = tk.Button(
    button_frame,
    text="💰  CALCULATE SALARY",
    font=("Arial", 15, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#1E8449",
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=calculate_salary
)

calculate_button.grid(
    row=0,
    column=0,
    padx=15
)


clear_button = tk.Button(
    button_frame,
    text="🗑  CLEAR",
    font=("Arial", 15, "bold"),
    bg=RED,
    fg=WHITE,
    activebackground="#922B21",
    activeforeground=WHITE,
    width=15,
    height=2,
    relief="flat",
    cursor="hand2",
    command=clear_form
)

clear_button.grid(
    row=0,
    column=1,
    padx=15
)


# Footer
tk.Label(
    dashboard_page,
    text="Enter employee information and calculate the monthly salary",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg="#566573"
).pack()


# ============================================================
# ======================= RESULT PAGE ========================
# ============================================================

# Header
result_header = tk.Frame(
    result_page,
    bg=HEADER_COLOR,
    height=110
)

result_header.pack(fill="x")

tk.Label(
    result_header,
    text="📊 SALARY RESULT",
    font=("Arial", 28, "bold"),
    bg=HEADER_COLOR,
    fg=WHITE
).pack(pady=(25, 0))

tk.Label(
    result_header,
    text="Employee Salary Summary",
    font=("Arial", 14),
    bg=HEADER_COLOR,
    fg="#AED6F1"
).pack()


# Result title
tk.Label(
    result_page,
    text="Salary Calculation Result",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TEXT
).pack(pady=25)


# Employee information card
info_card = tk.Frame(
    result_page,
    bg=WHITE,
    width=750,
    height=190
)

info_card.pack()
info_card.pack_propagate(False)


def result_row(label, variable, row):

    tk.Label(
        info_card,
        text=label,
        font=("Arial", 13, "bold"),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=row,
        column=0,
        padx=35,
        pady=10,
        sticky="w"
    )

    tk.Label(
        info_card,
        textvariable=variable,
        font=("Arial", 13),
        bg=WHITE,
        fg=DARK_BLUE
    ).grid(
        row=row,
        column=1,
        padx=30,
        pady=10,
        sticky="w"
    )


result_row(
    "Employee ID",
    result_employee_id,
    0
)

result_row(
    "Employee Name",
    result_name,
    1
)

result_row(
    "Department",
    result_department,
    2
)


# Salary card
salary_card = tk.Frame(
    result_page,
    bg=LIGHT_BLUE,
    width=750,
    height=220
)

salary_card.pack(pady=20)
salary_card.pack_propagate(False)


def salary_row(label, variable, row):

    tk.Label(
        salary_card,
        text=label,
        font=("Arial", 13, "bold"),
        bg=LIGHT_BLUE,
        fg=TEXT
    ).grid(
        row=row,
        column=0,
        padx=50,
        pady=8,
        sticky="w"
    )

    tk.Label(
        salary_card,
        textvariable=variable,
        font=("Arial", 13),
        bg=LIGHT_BLUE,
        fg=DARK_BLUE
    ).grid(
        row=row,
        column=1,
        padx=50,
        pady=8,
        sticky="w"
    )


salary_row(
    "Basic Salary",
    result_basic,
    0
)

salary_row(
    "Bonus (10%)",
    result_bonus,
    1
)

salary_row(
    "Deduction (5%)",
    result_deduction,
    2
)


# Net salary
net_frame = tk.Frame(
    result_page,
    bg=GREEN,
    width=750,
    height=70
)

net_frame.pack()
net_frame.pack_propagate(False)

tk.Label(
    net_frame,
    text="NET SALARY",
    font=("Arial", 18, "bold"),
    bg=GREEN,
    fg=WHITE
).pack(side="left", padx=60, pady=18)

tk.Label(
    net_frame,
    textvariable=result_net,
    font=("Arial", 20, "bold"),
    bg=GREEN,
    fg=WHITE
).pack(side="right", padx=60, pady=17)


# Navigation buttons
result_buttons = tk.Frame(
    result_page,
    bg=BG_COLOR
)

result_buttons.pack(pady=25)


back_button = tk.Button(
    result_buttons,
    text="← BACK TO DASHBOARD",
    font=("Arial", 13, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=DARK_BLUE,
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=show_dashboard
)

back_button.grid(
    row=0,
    column=0,
    padx=15
)


new_employee_button = tk.Button(
    result_buttons,
    text="＋ NEW EMPLOYEE",
    font=("Arial", 13, "bold"),
    bg=RED,
    fg=WHITE,
    activebackground="#922B21",
    activeforeground=WHITE,
    width=20,
    height=2,
    relief="flat",
    cursor="hand2",
    command=lambda: [clear_form(), show_dashboard()]
)

new_employee_button.grid(
    row=0,
    column=1,
    padx=15
)


# ============================================================
# START PROGRAM
# ============================================================

dashboard_page.tkraise()

root.mainloop()