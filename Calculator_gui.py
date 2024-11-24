import tkinter as tk

calculation = ""

def add_to_cal(symbol):
    global calculation
    calculation += str(symbol)
    text_results.delete(1.0, "end")
    text_results.insert(1.0, calculation)
    
    
def evaluate_calculation():
    global calculation
    try:
        result =  str(eval(calculation))
        calculation = ""
        text_results.delete(1.0,"end")
        text_results.insert(1.0, result)
    except:
        clear_field()
        text_results.insert(1.0, "error!")

def clear_field():
    global calculation
    calculation=""
    text_results.delete(1.0,"end")
    


root = tk.Tk()
root.geometry("500x400")

text_results= tk.Text(root, height=2, width=24, font=("Arial", 24))
text_results.grid(columnspan=5)


btn_1 = tk.Button(root, text="1", font=("Arial",24),width=5, command= lambda:add_to_cal(1))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", font=("Arial",24),width=5, command= lambda:add_to_cal(2))
btn_2.grid(row=2, column=2)
btn_4 = tk.Button(root, text="4", font=("Arial",24),width=5, command= lambda:add_to_cal(4))
btn_4.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", font=("Arial",24),width=5, command= lambda:add_to_cal(4))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", font=("Arial",24),width=5, command= lambda:add_to_cal(5))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", font=("Arial",24),width=5, command= lambda:add_to_cal(6))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", font=("Arial",24),width=5, command= lambda:add_to_cal(7))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", font=("Arial",24),width=5, command= lambda:add_to_cal(8))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", font=("Arial",24),width=5, command= lambda:add_to_cal(9))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", font=("Arial",24),width=5, command= lambda:add_to_cal(0))
btn_0.grid(row=5, column=2)

#OPERATORS
btn_plus = tk.Button(root, text="+", font=("Arial",24),width=5, command= lambda:add_to_cal("+"))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", font=("Arial",24),width=5, command= lambda:add_to_cal("-"))
btn_minus.grid(row=3, column=4)
btn_mult = tk.Button(root, text="*", font=("Arial",24),width=5, command= lambda:add_to_cal("*"))
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", font=("Arial",24),width=5, command= lambda:add_to_cal("/"))
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", font=("Arial",24),width=5, command= lambda:add_to_cal("("))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", font=("Arial",24),width=5, command= lambda:add_to_cal(")"))
btn_close.grid(row=5, column=3)
btn_equal = tk.Button(root, text="=", font=("Arial",24),width=8, command= evaluate_calculation)
btn_equal.grid(row=6, column=1, columnspan=2)
btn_c = tk.Button(root, text="C", font=("Arial",24),width=8, command=clear_field)
btn_c.grid(row=6, column=3, columnspan=2)
root.mainloop()