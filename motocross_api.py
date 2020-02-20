import requests
from tkinter import *
from tkinter import ttk
import json

def get_info(*args):
    result_text.delete("1.0", "end")
    try:
        year = year_list.get()
        track_name = track_list.get()
        class_moto = class_list.get()
        #moto_number
        url = f"https://api.promotocrossapi.com/laptimes/{year}/{track_name}/{class_moto}"
        request = requests.get(url)
        result = request.json()
        for item in result["data"]:
            try:
                result_text.insert("end", item["race"])
                result_text.insert("end", "\n")
            except KeyError:
                pass
            for rider in item["riderData"]:
                try:
                    result_text.insert("end", rider["name"])
                    result_text.insert("end", "\n")
                except KeyError:
                    pass
    except ValueError:
        pass


root = Tk()
root.title("Motocross result")

main_window = ttk.Frame(root)
main_window.grid(column = 0, row = 0)

year_list = ttk.Combobox(main_window)
year_list["values"] = (18, 17, 16)
year_list.grid(column = 0, row = 0)

track_list = ttk.Combobox(main_window)
track_list["values"] = ("HANGTOWN", "GLEN-HELEN-RACEWAY", "THUNDER-VALLEY")
track_list.grid(column = 0, row = 1)

class_list = ttk.Combobox(main_window)
class_list["values"] = (250, 450)
class_list.grid(column = 0, row = 2)

ttk.Label(main_window, text="Motocross result").grid(column=0, row=3)
result_text = Text(main_window, width=50, height=10)
result_text.grid(column = 0, row = 4, columnspan=2)

ttk.Button(main_window, text="Get result", command=get_info).grid(column=1, row=0, rowspan=3)

root.mainloop()
