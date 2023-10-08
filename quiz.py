import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import ttk

questions = [
        {
            "question": "What is the output of the following code snippet?\nx = 5\ny = 2\nresult = x % y\nprint(result)",
            "choices": ["a) 2", "b) 3", "c) 2.5", "d) 1"],
            "answer": "d"
        },
        {
            "question": "Which of the following is the correct way to define a function in Python?",
            "choices": ["a) function my_function():", "b) def my_function():", "c) define my_function():", "d) func my_function():"],
            "answer": "b"
        },
        {
            "question": "What will be the output of the following code?\nmy_list = [1, 2, 3, 4]\nnew_list = my_list[1:3]\nprint(new_list)",
            "choices": ["a) [1, 2]", "b) [2, 3]", "c) [2, 3, 4]", "d) [1, 3]"],
            "answer": "b"
        },
        {
            "question": "In Python, which keyword is used to create a loop?",
            "choices": ["a) loop", "b) while", "c) for", "d) iterate"],
            "answer": "c"
        },
        {
            "question": "What does the len() function do in Python?",
            "choices": ["a) Returns the length of a string", "b) Calculates the logarithm of a number", "c) Returns the total number of items in a list", "d) Computes the factorial of a number"],
            "answer": "c"
        },
        {
            "question": "Which data type is used to represent a single character in Python?",
            "choices": ["a) character", "b) char", "c) str", "d) charstr"],
            "answer": "c"
        },
        {
            "question": "What will be the output of the following code snippet?\nx = 10\ny = 5\nresult = x > y\nprint(result)",
            "choices": ["a) True", "b) False", "c) 1", "d) 0"],
            "answer": "a"
        },
        {
            "question": "Which of the following is used to check if a value is present in a list?",
            "choices": ["a) find()", "b) contains()", "c) isin()", "d) in"],
            "answer": "d"
        },
        {
            "question": "What does the append() method do for lists in Python?",
            "choices": ["a) Removes the last element from the list", "b) Adds an element to the beginning of the list", "c) Adds an element to the end of the list", "d) Reverses the order of elements in the list"],
            "answer": "c"
        },
        {
            "question": "How do you comment a single line in Python?",
            "choices": ["a) /* comment */", "b) // comment", "c) # comment", "d) <!-- comment -->"],
            "answer": "c"
        },
    ]

class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to Python Basics Quiz")
        self.geometry("600x450")

        self.custom_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        self.label = tk.Label(self, text="Welcome to Python Basics Quiz!", font=self.custom_font)
        self.label.pack(pady=20)

        self.instructions = """Instructions:
        - You will be presented with multiple-choice questions.
        - Choose the correct option by clicking on the radio buttons.
        - Click the 'Next' button to move to the next question.
        - You can skip a question by clicking the 'Skip' button.
        - When you're done, click the 'Submit' button to see your results.
        - Good luck!"""

        self.instructions_label = tk.Label(self, text=self.instructions, font=("Helvetica", 12), justify=tk.LEFT)
        self.instructions_label.pack(pady=10)

        self.exit_button = tk.Button(self, text="Exit", font=self.custom_font, bg="#FF4500", fg="white", activebackground="#FF6347", command=self.quit)
        self.exit_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.play_button = tk.Button(self, text="Play", font=self.custom_font, bg="#4CAF50", fg="white", activebackground="#45a049", command=self.start_quiz)
        self.play_button.pack(side=tk.RIGHT, padx=20, pady=10)

    def start_quiz(self):
        self.destroy()
        app = PythonBasicsQuizApp()
        app.mainloop()

class PythonBasicsQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Python Basics Quiz")
        self.geometry("600x450")

        self.current_question = 0
        self.score = 0

        self.configure_gui()
        self.create_widgets()
        self.load_question()

    def configure_gui(self):
        # Add a custom font (change 'your_font.ttf' with the path to your font file)
        self.custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

    def create_widgets(self):

        self.question_label = tk.Label(self, text="", wraplength=500, font=self.custom_font, bg="#f0f0f0")
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.choices = []
        for i in range(4):
            choice = ttk.Radiobutton(self, text="", variable=self.radio_var, value="", style="Custom.TRadiobutton", command=self.check_answer)
            self.choices.append(choice)
            choice.pack(anchor='w', padx=20)

        self.submit_button = tk.Button(self, text="Submit", font=self.custom_font, bg="#4CAF50", fg="white", activebackground="#45a049", command=self.show_results)
        self.submit_button.pack(side=tk.BOTTOM,pady=10)

        self.prev_button = tk.Button(self, text="Previous", font=self.custom_font, bg="#1E90FF", fg="white",
                                     activebackground="#4169E1", command=self.previous_question)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.skip_button = tk.Button(self, text="Skip", font=self.custom_font, bg="#FF4500", fg="white", activebackground="#FF6347", command=self.skip_question)
        self.skip_button.pack(side=tk.RIGHT, padx=20)

        self.next_button = tk.Button(self, text="Next", font=self.custom_font, bg="#4CAF50", fg="white", activebackground="#45a049", command=self.load_next_question)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        # Create a custom style for the Radiobuttons
        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#f0f0f0", font=self.custom_font, relief="solid", borderwidth=2)

        # Bind <Enter> and <Leave> events to change color when hovering over the Radiobuttons
        for i in range(4):
            self.choices[i].bind("<Enter>", lambda event, i=i: self.on_enter(event, i))
            self.choices[i].bind("<Leave>", lambda event, i=i: self.on_leave(event, i))

    # Helper functions to change the Radiobutton color on hover
    def on_enter(self, event, index):
        style = ttk.Style()
        style.map("Custom.TRadiobutton",
                  background=[(f"!active", "#f0f0f0"), ("active", "#ADD8E6")])
        self.choices[index].state(["active"])

    def on_leave(self, event, index):
        style = ttk.Style()
        style.map("Custom.TRadiobutton",
                  background=[(f"!active", "#f0f0f0"), ("active", "#ADD8E6")])
        self.choices[index].state(["!active"])

    def load_question(self):
        # Get the current question data
        question_data = questions[self.current_question]

        # Update the question label
        self.question_label.config(text=question_data["question"])

        # Update the choices for each radio button
        choices = question_data["choices"]
        for i in range(4):
            self.choices[i].config(text=choices[i], value=chr(97 + i))  # Set the text and value for each radio button

        # Clear the selected answer
        self.radio_var.set("")

    def skip_question(self):
        self.current_question += 1
        self.load_question()

    def previous_question(self):
        self.current_question -= 1
        self.load_question()

    def load_next_question(self):
        self.current_question += 1
        self.load_question()

    def check_answer(self):
        user_answer = self.radio_var.get()
        correct_answer = questions[self.current_question]["answer"]

        if user_answer == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        percentage_score = (self.score / len(questions)) * 100

        if percentage_score >= 70:
            message = "Congratulations! You did great!"
        elif percentage_score >= 50:
            message = "Not bad, but you can do better!"
        else:
            message = "You might want to brush up on your Python basics!"

        messagebox.showinfo("Quiz Results", f"Your score: {self.score}/{len(questions)}\n{message}")
        self.quit()
        self.destroy()
        welcome_window = WelcomeWindow()
        welcome_window.mainloop()

def main():
    welcome_window = WelcomeWindow()
    welcome_window.mainloop()

if __name__ == "__main__":
    main()
