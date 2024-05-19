import tkinter as tk
from Libs.pycolors import pycolors

colors = pycolors() # Создаем экземпляр класса pycolors

class TrainingPlanApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Program: Percentage in Powerlifting (PiP)")
        self.window.geometry("300x620")

        self.create_widgets()
        
    def create_widgets(self):
        self.label1 = tk.Label(self.window, text="Введите числа:")
        self.label1.config(font=("Helvetica", 12, "bold"))
        self.label1.pack(side="top", pady=10)

        self.label2 = tk.Label(self.window, text="Присед:")
        self.label2.pack()
        self.entry1 = tk.Entry(self.window, width=38)
        self.entry1.pack()

        self.label3 = tk.Label(self.window, text="Жим:")
        self.label3.pack()
        self.entry2 = tk.Entry(self.window, width=38)
        self.entry2.pack()

        self.label4 = tk.Label(self.window, text="Тяга:")
        self.label4.pack()
        self.entry3 = tk.Entry(self.window, width=38)
        self.entry3.pack()

        self.button2 = tk.Button(self.window, text="Создать таблицу", command=self.create_training_plan)
        self.button2.pack(pady=10)

        # Добавляем виджет Text и скроллбар
        self.text_frame = tk.Frame(self.window)
        self.text_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output = tk.Text(self.text_frame, width=38, height=40, yscrollcommand=self.scrollbar.set)
        self.output.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.output.yview)

    def create_training_plan(self):
        self.output.delete('1.0', tk.END)
        self.generate_plan("ПРИСЕД", self.entry1)
        self.generate_plan("ЖИМ", self.entry2)
        self.generate_plan_from_file("ПРОГРАММА.txt") # Файл можно заменить на свой!

    def generate_plan(self, exercise_name, entry):

        ######################################################
        weight = entry.get() # Получение введенного числа из поля ввода

        # Проверка на пустой ввод
        if weight == '':
            self.output.insert(tk.END, f'{exercise_name}: Пожалуйста, введите число.\n')
            self.output.insert(tk.END, f'\n')
            return
        
        weight = int(float(weight))
        halfWeight = weight * 0.5 # 50% веса по ТЗ
        step_percentage = (weight  - halfWeight) / 10

        self.output.insert(tk.END, f'{exercise_name}:\n')
        for week in range(1, 11):
            new_weight = int(halfWeight + step_percentage * (week - 1)) # Преобразуем в целое число
            self.output.insert(tk.END, f'{week} неделя {new_weight} кг 4 подхода по 8 раз\n')
            # print(f'{colors.BOLD}{week}{colors.ENDC} неделя {colors.YELLOW}{new_weight}{colors.ENDC} кг 4 подхода по 8 раз\n')
        self.output.insert(tk.END, f'\n')

    def generate_plan_from_file(self, filePath):
        try:
            with open(filePath, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.output.insert(tk.END, 'ТЯГА:\n')
                self.output.insert(tk.END, file_content)
                self.output.insert(tk.END, f'\n')
        except FileNotFoundError:
            self.output.insert(tk.END, 'Ошибка: Файл не найден.\n')
        except Exception as e:
            self.output.insert(tk.END, f'Ошибка при чтении файла: {e}\n')
