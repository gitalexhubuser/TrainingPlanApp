import tkinter as tk

class PowerliftingApp: 
    def init(self): 
        self.root = tk.Tk() 
        self.root.title("Percentage in Powerlifting (PiP) ver 0.1")

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        self.button = tk.Button(self.root, text="Посчитать", command=self.create_training_table)
        self.button.pack()
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        
    def create_training_table(self):
        # Ваш код для создания таблицы тренировок
    
        self.result_label.config(text="Таблица тренировок создана")  # Пример вывода результата
    
    def run(self):
        self.root.mainloop()

# Использование:
# app = PowerliftingApp() app.run() 
