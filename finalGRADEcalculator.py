import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('GRADE CALCULATOR')

# store grade
email = tk.StringVar()


def login_clicked():
    global grade_answer , int_answer
    grade_answer = email.get()
    int_answer = int(grade_answer)


    GRADE = int(grade_answer)
    if GRADE > 100:
        GRADE = "Number Exceeds 100, please try again."
    elif GRADE >= 90:
        GRADE = "A"
    elif 80 <= GRADE <= 89:
        GRADE = "B"
    elif 70 <= GRADE <= 79:
        GRADE = "C"
    elif 60 <= GRADE <= 69:
        GRADE = "D"
    elif 59 >= 0:
        GRADE = "F"
    



    msg = ((f'Your Grade is: ')+ GRADE)
    showinfo(
        title='Grade',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# enters grade box
email_label = ttk.Label(signin, text="GRADE: ")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)

email_entry.pack(fill='x', expand=True)
email_entry.focus()




# confirm button
confirm_button = ttk.Button(signin, text="Confirm", command=login_clicked)
confirm_button.pack(fill='x', expand=True, pady=10)


root.mainloop()