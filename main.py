import tkinter as tk

def create_training_table():
    weight = int(entry.get())
    training_table = ""
    
    for week in range(1, 11):
        training_weight = weight + (week - 1) * 10
        training_table += f"{week} неделя {training_weight} кг 4 подхода по 8 раз\n"
    
    result_label.config(text=training_table)

root = tk.Tk()
root.title("Percentage in Powerlifting (PiP) ver 0.1")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Посчитать", command=create_training_table)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

