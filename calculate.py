from tkinter import *
calc = Tk()
calc.geometry('288x430')
calc.resizable(width = False, height = False)
calc.title("calculator")
calc.configure(bg = "black")

     ############ 
    # FORMATTING #
    ############

section_1 = Frame (
        calc,
        width = 290,
        height = 100,
        ) 
section_1.pack(side = TOP)

section_2 = Frame (
        calc,
        width = 290,
        height = 50,
        )
section_2.pack(side = TOP)

section_3 = Frame (
        calc,
        width = 290,
        height = 350,
        bg = "#555753"
        )
section_3.pack(side = TOP)

     #########################
    # Output display section #
    #########################

section_show = Text (
        section_1,
        bd = 3,
        width = 50,
        font = 4,
        height = 5.5,
        fg = "black",
       background = "white"
        )
section_show.pack(side = TOP)

result = Text (
        section_2,
        bd = 3,
        font = 4,
        width = 50,
        height = 2.25,
        fg = "black",
        background = "white"
        )
result.pack(side = TOP)

calc.mainloop()
