import tkinter as tk
from Libs.lib_tk import TrainingPlanApp

if __name__ == "__main__":
    # window = tk.Tk()
    # window.resizable(False, False)
    # app = TrainingPlanApp(window) # Экземпляр класса
    # window.mainloop()

    root = tk.Tk()
    app = TrainingPlanApp(root)
    root.mainloop()
