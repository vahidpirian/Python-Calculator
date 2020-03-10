from tkinter import *
calc = Tk()
calc.geometry('288x430')
calc.resizable(width = False, height = False)
calc.title("Calculator")
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

section_show = Entry (
        section_1,
        bd = 3,
        font = 4,
        fg = "black",
        background = "white",
        ).grid( ipadx = 39, ipady = 48)

result = Entry (
        section_2,
        bd = 3,
        font = 4,
        justify = RIGHT,
        fg = "black",
        background = "white",
        ).grid(ipadx = 39, ipady = 9, row = 4)
   
     ##########
    # BUTTONS #
    ##########

for i in range(6):
    for j in range(4):
        frame = Frame (
                section_3,
                borderwidth = 1,
                width = 20,
                height = 10,
                highlightbackground = "#555753",
                )
        
        frame.grid( row = i, column = j, padx = 5, pady = 5)
        
        if i == 0 and j == 0:
            btn_clear = Button (
                    frame,
                    fg = "blue",
                    text = "C",
                    width = 4,
                    height = 1,
                    relief = RAISED,
                    )
            btn_clear.pack()
 
            
        elif i == 0 and j == 1:
            btn_del = Button (
                    frame,
                    fg = "blue",
                    text = "DEL",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_del.pack()


        elif i == 0 and j == 2:
            btn_obrackets = Button (
                    frame,
                    fg = "blue",
                    text = "(",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_obrackets.pack()
        

        elif i == 0 and j == 3:
            btn_cbrackets = Button (
                    frame,
                    fg = "blue",
                    text = ")",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_cbrackets.pack()


        elif i == 1 and j == 0:
            btn_mul = Button (
                    frame,
                    fg = "blue",
                    text = "X",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_mul.pack()


        elif i == 1 and j == 1:
            btn_div = Button (
                    frame,
                    fg = "blue",
                    text = "÷",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_div.pack()


        elif i == 1 and j == 2:
            btn_sum = Button (
                    frame,
                    fg = "blue",
                    text = "+",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_sum.pack()


        elif i == 1 and j == 3:
            btn_minus = Button (
                    frame,
                    fg = "blue",
                    text = "-",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_minus.pack()


        elif i == 2 and j == 0:
            btn_seven = Button (
                    frame,
                    text = "7",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_seven.pack()


        elif i == 2 and j == 1:
            btn_eight = Button (
                    frame,
                    text = "8",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_eight.pack()


        elif i == 2 and j == 2:
            btn_nine = Button (
                    frame,
                    text = "9",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_nine.pack()


        elif i == 2 and j == 3:
            btn_square_2 = Button (
                    frame,
                    fg = "blue",
                    text = "x²",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_square_2.pack()


        elif i == 3 and j == 0:
            btn_four = Button (
                    frame,
                    text = "4",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_four.pack()


        elif i == 3 and j == 1:
            btn_five = Button (
                    frame,
                    text = "5",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_five.pack()


        elif i == 3 and j == 2:
            btn_six = Button (
                    frame,
                    text = "6",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_six.pack()


        elif i == 3 and j == 3:
            btn_square_3 = Button (
                    frame,
                    fg = "blue",
                    text = "x³",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_square_3.pack()


        elif i == 4 and j == 0:
            btn_one = Button (
                    frame,
                    text = "1",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_one.pack()


        elif i == 4 and j == 1:
            btn_two = Button (
                    frame,
                    text = "2",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_two.pack()


        elif i == 4 and j == 2:
            btn_three = Button (
                    frame,
                    text = "3",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_three.pack()


        elif i == 4 and j == 3:
            btn_s = Button (
                    frame,
                    fg = "blue",
                    text = "ᜯ",
                    width = 4,
                    height = 1,
                    relief = RAISED
                    )
            btn_s.pack()


        elif i == 5 and j == 0:
            btn_persent = Button (
                    frame,
                    text = "%",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_persent.pack()


        elif i == 5 and j == 1:
            btn_zero = Button (
                    frame,
                    text = "0",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_zero.pack()


        elif i == 5 and j == 2:
            btn_dot = Button (
                    frame,
                    text = ".",
                    width = 4,
                    height = 1,
                    highlightbackground = "white",
                    background = "white",
                    relief = RAISED
                    )
            btn_dot.pack()


        elif i == 5 and j == 3:
            btn_equal = Button (
                    frame,
                    text = "=",
                    width = 4,
                    height = 1,
                    highlightbackground = "#555753",
                    background = "blue",
                    relief = RAISED
                    )
            btn_equal.pack()


calc.mainloop()
