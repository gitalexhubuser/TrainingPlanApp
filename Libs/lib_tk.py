import tkinter as tk
from Libs.pycolors import pycolors

colors = pycolors() # Создаем экземпляр класса pycolors

class TrainingPlanApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Program: Percentage in Powerlifting (PiP)")
        self.window.geometry("300x230")
        
        self.label = tk.Label(window, text="Введите число:")
        self.label.pack()
        
        self.entry = tk.Entry(window)
        self.entry.pack()
        
        self.button = tk.Button(window, text="Создать таблицу", command=self.create_training_plan)
        self.button.pack()
        
        self.output = tk.Text(window)
        self.output.pack()
    
    def create_training_plan(self):

        # Получение введенного числа из поля ввода
        weight = self.entry.get()
        
        # Проверка на пустой ввод
        if weight == '':
            return
        
        weight = int(float(weight))
        halfWeight = weight * 0.5 # 50% веса по ТЗ
        
        self.output.delete('1.0', tk.END)
        
        for week in range(1, 11):
            new_weight = int(halfWeight + (week - 1) * 10) # Преобразуем в целое число
            self.output.insert(tk.END, f'{week} неделя {new_weight} кг 4 подхода по 8 раз\n')
            print(f'{colors.BOLD}{week}{colors.ENDC} неделя {colors.YELLOW}{new_weight}{colors.ENDC} кг 4 подхода по 8 раз\n')
