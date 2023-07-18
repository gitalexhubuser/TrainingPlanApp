import tkinter as tk

def create_training_plan():

     # Получение введенного числа из поля ввода
    weight = entry.get()

    # Проверка на пустой ввод
    if weight == '':
        return
    
    # Получение введенного числа из поля ввода
    weight = int(entry.get())



    # Делаем 50% от введённого числа (по тз)
    halfWeight = weight * 0.5

    # Очистка текстового поля перед выводом новой таблицы
    output.delete('1.0', tk.END)

    # Формирование таблицы тренировочного процесса на 10 недель
    for week in range(1, 11):
        new_weight = halfWeight + (week - 1) * 10
        output.insert(tk.END, f'{week} неделя {new_weight}кг 4 подхода по 8 раз\n')


# Создание графического интерфейса с одной кнопкой и полем ввода
window = tk.Tk()
window.title("Program: Percentage in Powerlifting (PiP)")
window.geometry("300x230")

label = tk.Label(window, text="Введите число:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Создать таблицу", command=create_training_plan)
button.pack()

output = tk.Text(window)
output.pack()

window.mainloop()
