from tkinter import *

window = Tk()

window.title("My First GUI  Program")
window.minsize(width=500, height = 300)
window.config(padx=100, pady=200)


#Label
my_label = Label(text='I am a label',font =('Arial',24,'bold'))
# my_label.pack(side = 'left')
# my_label.pack(expand = True)
# my_label.pack()


my_label['text'] = "New Text"
my_label.config(text= 'New Text')
my_label.grid(column=0,row=0)


#Button
def button_clicked():
    print('Button Clicked!!!')
    new_text = input.get()
    # my_label.config(text = 'Button Got Clicked!!!!!!!')
    my_label.config(text = new_text)
button = Button(text='Click Me!!!',command = button_clicked)
button.grid(column=1,row=1)
# button.pack()

#Entry
input= Entry(width = 10)
# input.pack()
print(input.get())
input.grid(column=3,row=2)






window.mainloop()