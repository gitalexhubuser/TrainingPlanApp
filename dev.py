import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        label1 = Label(text="Введите числа:")
        layout.add_widget(label1)
        entry1 = TextInput(width=38)
        layout.add_widget(entry1)
        label2 = Label(text="Присед:")
        layout.add_widget(label2)
        entry2 = TextInput(width=38)
        layout.add_widget(entry2)
        label3 = Label(text="Жим:")
        layout.add_widget(label3)
        entry3 = TextInput(width=38)
        layout.add_widget(entry3)
        button2 = Button(text="Создать таблицу", on_press=self.create_training_plan)
        layout.add_widget(button2)
        output = Label()
        layout.add_widget(output)
        return layout

    def create_training_plan(self, instance):
        weight = float(entry1.text)
        halfWeight = weight * 0.5
        step_percentage = (weight - halfWeight) / 10
        output.text = ""
        for week in range(1, 11):
            new_weight = int(halfWeight + step_percentage * (week - 1))
            output.text += f"{week} неделя {new_weight} кг 4 подхода по 8 раз\n"

if __name__ == "__main__":
    MyApp().run()

