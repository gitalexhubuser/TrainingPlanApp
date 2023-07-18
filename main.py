import tkinter as tk
from Libs.lib_tk import TrainingPlanApp

if __name__ == "__main__":
    window = tk.Tk()
    app = TrainingPlanApp(window) # Экземпляр класса
    window.mainloop()
