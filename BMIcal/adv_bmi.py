from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import statistics

# List to store BMI history
bmi_history = []

def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height

def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi(a=""):
# "a" is there because the bind function gives an argument to the function.
    print(a)
    '''
      This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
        bmi_history.append(bmi)  # Store the BMI in history
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)

def show_bmi_statistics():
    '''
    This function shows the BMI statistics
    '''
    if not bmi_history:
        messagebox.showinfo("BMI Statistics", "No BMI data to display!")
        return

    # Calculate statistics
    mean_bmi = statistics.mean(bmi_history)
    median_bmi = statistics.median(bmi_history)
    stddev_bmi = statistics.stdev(bmi_history) if len(bmi_history) > 1 else 0

    # Show statistics in a message box
    stats_message = (f"BMI Statistics:\n\n"
                     f"Mean: {mean_bmi:.2f}\n"
                     f"Median: {median_bmi:.2f}\n"
                     f"Standard Deviation: {stddev_bmi:.2f}")
    messagebox.showinfo("BMI Statistics", stats_message)

def show_bmi_graph():
    '''
    This function plots the BMI history with trend analysis
    '''
    if not bmi_history:
        messagebox.showinfo("BMI History", "No BMI data to display!")
        return

    # Prepare the plot
    plt.figure(figsize=(10, 5))
    plt.plot(bmi_history, marker='o', linestyle='-', color='b', label='BMI')
    
    if len(bmi_history) > 1:
        # Trend line
        x = np.arange(len(bmi_history))
        try:
            z = np.polyfit(x, bmi_history, 1)
            p = np.poly1d(z)
            plt.plot(x, p(x), "r--", label='Trend Line')
        except np.linalg.LinAlgError:
            messagebox.showinfo("BMI History", "Could not fit a trend line. Insufficient or poorly conditioned data.")

    # Annotate statistics
    plt.title('BMI History with Trend Analysis')
    plt.xlabel('Entry Number')
    plt.ylabel('BMI')
    plt.grid(True)
    plt.legend()
    plt.show()

def reset_entries():
    '''
    This function resets the input fields and BMI history
    '''
    ENTRY1.delete(0, END)
    ENTRY2.delete(0, END)
    bmi_history.clear()
    messagebox.showinfo("Reset", "Entries and BMI history have been reset.")

def exit_application():
    '''
    This function exits the application
    '''
    TOP.destroy()

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x400")
    TOP.configure(background="#2c3e50")   
    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)

    LABLE =Label(TOP, bg="#2c3e50", text="BMI Calculator", font=("Helvetica", 20), pady=10, fg="white")  # Title text in white
    LABLE.place(x=100, y=0)
    LABLE1 = Label(TOP, bg="#2c3e50", text="Enter Weight (in kg):", font=("Helvetica", 10), pady=5, fg="#ecf0f1")  # Normal style
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#2c3e50", text="Enter Height (in cm):", font=("Helvetica", 10), pady=5, fg="#ecf0f1")  # Normal style
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)

    BUTTON = Button(bg="#2980b9", text="Calculate BMI", padx=20, pady=10, command=calculate_bmi, font=("Helvetica", 15, "bold"), fg="white")
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=100, y=190)

    # Button to show BMI statistics
    BUTTON_STATISTICS = Button(bg="#27ae60", text="Statistics", padx=5, pady=10, command=show_bmi_statistics, font=("Helvetica", 10, "bold"), fg="white")
    BUTTON_STATISTICS.grid(row=4, column=0, sticky=W)
    BUTTON_STATISTICS.place(x=10, y=320)

    # Button to show BMI history graph
    BUTTON_HISTORY = Button(bg="#8e44ad", text="Graphs", padx=10, pady=10, command=show_bmi_graph, font=("Helvetica", 10, "bold"), fg="white")
    BUTTON_HISTORY.grid(row=4, column=1, sticky=W)
    BUTTON_HISTORY.place(x=110, y=320)

    # Button to reset entries and BMI history
    BUTTON_RESET = Button(bg="#c0392b", text="Reset", padx=10, pady=10, command=reset_entries, font=("Helvetica", 10, "bold"), fg="white")
    BUTTON_RESET.grid(row=5, column=0, sticky=W)
    BUTTON_RESET.place(x=200, y=320)

    # Button to exit the application
    BUTTON_EXIT = Button(bg="#7f8c8d", text="Exit", padx=10, pady=10, command=exit_application, font=("Helvetica", 10, "bold"), fg="white")
    BUTTON_EXIT.grid(row=5, column=1, sticky=W)
    BUTTON_EXIT.place(x=290, y=320)

    TOP.mainloop()
