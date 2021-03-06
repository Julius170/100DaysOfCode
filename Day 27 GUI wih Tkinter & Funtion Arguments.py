# BUILDING A UNIT CONVERTER AS THE FINAL PROJECT FOR THIS DAY USING A GUI


# PIRATES OF SILICON VALLEY 

from tkinter import *
from turtle import width, window_width

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
# ADDING PADDING
window.config(padx=20, pady=20)


# LABELS
# my_label = tkinter.Label(text= "I am a label", font=("Courier", 24, "bold")) 
# my_label.pack()

# ADVANCED ARGUMENTS

# UNLIMITED POSITIONAL ARGUMENTS (using the "*args")
# def  add(*args):

#     print(args[2])

#     sum = 0
#     for n in args:
#         sum+=n
#     return sum

# print(add(1, 2, 3, 4, 5, 56))


# UNLIMITED KWARG ARGUMENTS
# def calculate(n, **kwargs):
#     print(kwargs)

#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n += kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=56)


# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw.get("model")

# my_car = Car(make = "Nissan")


# print(my_car.make)

# my_label =  Label(text="I am a label", font=("Ariel", 24, "bold"))
# my_label.pack()

# my_label["text"] = "New text"
# my_label.config(text= "Another text")

# def button_clicked():
#     print("I got clicked")

#     user_input = input.get()
#     my_label.config(text= user_input)


# button = Button(text="Submit", command=button_clicked)
# button.pack()


# # THE ENTRY COMPONENT

# input = Entry(width=20)
# input.pack()
# user_input = input.get()

# ANGELA'S SUMMERY OF OTHER WIDGET FUNCTIONS
# from tkinter import *

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# #Buttons
# def action():
#     print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


# def button_clicked():
#     print("I got clicked")
#     # new_label.config(text="new_text")


# # LABEL
# my_label = Label(text="I am a Label", font=("Ariel", 24, "bold"))
# my_label.grid(column=0, row=0)

# # BUTTON
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)

# # A NEW BUTTON
# button = Button(text="New Button", command=button_clicked)
# button.grid(column=2, row=0)

# # ENTRY
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)

# PACK, PLACE & GRID (DETERMINES LAYOUTS MANAGEMENT)
# PLACE UNLIKE PACK WORKS WITH PRECISION
# GRID ON THE OTHER HAND ARRANGES THE LAYOUTS IN BLOCKS
# WARNING: GRIDS ARE NEVER TO BE USER WITH PACKS IN THE SAME WIDGET


# EXERCISE: MILE TO KM CONVERTER

def miles_to_kilo():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result.config(text=f"{km}")


# ENTRY
miles_input = Entry(width=10)
print(miles_input.get)
miles_input.grid(column=1, row=0)

# LABELS
mile_label = Label(text="Mile", font=("Courier", 10, "bold"))
mile_label.grid(column=2, row=0)

is_equal = Label(text="is equal to: ", )
is_equal.grid(column=2, row=0)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

# BUTTON
calculate_button = Button(text='Calculate', command=miles_to_kilo)
calculate_button.grid(column=1, row=2)

window.mainloop()

# FINITE
