from tkinter import *


def convert_ml_km():
    miles = input.get()
    km = float(miles) * 1.609344
    result_label['text'] = km

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)






#Label
label1 = Label(text = "is equal to", font=("Arial", 14))
label1.grid(row=1, column=0)

result_label = Label(text = 0, font=("Arial", 14))
result_label.grid(row=1,column=1)

miles_label = Label(text = 'Miles', font=("Arial", 14))
miles_label.grid(row=0,column=2)

km_label = Label(text = 'Km', font=("Arial", 14))
km_label.grid(row=1,column=2)


#Entry
input = Entry(width=7)
input.grid(row=0,column=1)




#Create a Button
button = Button(text = "Calculate", command=convert_ml_km)
button.grid(row=1,column=2)










window.mainloop()
