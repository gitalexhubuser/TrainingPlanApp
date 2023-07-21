import tkinter as tk
from Libs.pycolors import pycolors

colors = pycolors() # Создаем экземпляр класса pycolors

class TrainingPlanApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Program: Percentage in Powerlifting (PiP)")
        self.window.geometry("300x320")
        
        self.label1 = tk.Label(window, text="Введите числа:")
        self.label1.config(font=("Helvetica", 12, "bold"))
        self.label1.place(x=70, y=0)
        self.label1.pack(side="top")

        self.label2 = tk.Label(window, text="Присед:")
        self.label2.place(x=0, y=30)
        self.entry1 = tk.Entry(window, width=38)
        self.entry1.place(x=60, y=32)

        self.label3 = tk.Label(window, text="Жим:")
        self.label3.place(x=0, y=30*2)
        self.entry2 = tk.Entry(window, width=38)
        self.entry2.place(x=60, y=32*2)

        self.label3 = tk.Label(window, text="Тяга:")
        self.label3.place(x=0, y=30*3)
        self.entry2 = tk.Entry(window, width=38)
        self.entry2.place(x=60, y=32*3)

        self.button2 = tk.Button(window, text="Создать таблицу", command=self.create_training_plan)
        self.button2.place(x=90, y=32*4)

        self.output = tk.Text(window)
        self.output.place(x=0, y=32*5)

    def create_training_plan(self):

        # Получение введенного числа из поля ввода
        weight = self.entry1.get()
        
        # Проверка на пустой ввод
        if weight == '':
            return
        
        weight = int(float(weight))
        halfWeight = weight * 0.5 # 50% веса по ТЗ

        # step_percentage = (100 - 50) / 10 # Шаг в процентах # или !!!
        step_percentage = (weight  - halfWeight) / 10 # Шаг в процентах # или !!!
        
        self.output.delete('1.0', tk.END)
        
        for week in range(1, 11):
            # new_weight = int(halfWeight + (week - 1) * 10) # Преобразуем в целое число
            new_weight = int(halfWeight + step_percentage * (week - 1)) # Преобразуем в целое число
            self.output.insert(tk.END, f'{week} неделя {new_weight} кг 4 подхода по 8 раз\n')
            print(f'{colors.BOLD}{week}{colors.ENDC} неделя {colors.YELLOW}{new_weight}{colors.ENDC} кг 4 подхода по 8 раз\n')
