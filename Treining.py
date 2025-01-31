# import tkinter as tk
#
# window = tk.Tk()
# window.title("Okno")
#
# def validate(new_value):
#     try:
#         if new_value == "" or new_value == "-" or new_value == "+":
#             return True
#         _str = str(float(new_value))
#         return True
#     except:
#         return False
#
#
# que = tk.Label(window, text="Введите цифры")
#
# vcmd = (window.register(validate), '%P')
# ans = tk.Entry(window, validate='key', validatecommand=vcmd)
#
# que.grid(row=0, column=0, sticky="e")
# ans.grid(row=0, column=1)
# ans.focus()
#
# window.mainloop()
import random
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    tickets.remove(win2)
    win3 = random.choice(tickets)
    tickets.remove(win3)
    return win1, win2, win3
win = lottery()
print(win)