import requests
from tkinter import *
from tkinter import ttk
import json

def get_info(*args):
    """Get information from API and make riders_listbox"""
    riders_listbox.delete("0", "end")
    riders_list.clear()
    riders_result.clear()
    try:
        year = year_list.get()
        track_name = track_list.get()
        class_moto = class_list.get()
        moto_number = int(moto_list.get())
        url = f"https://api.promotocrossapi.com/laptimes/{year}/{track_name}/{class_moto}/{moto_number}"
        request = requests.get(url)
        result = request.json()
        for rider in result["data"]["riderData"]:
            try:
                riders_listbox.insert("end", rider["name"])
                riders_list.append(rider["name"])
                riders_result.append(rider)
            except KeyError:
                pass
    except ValueError:
        pass

def get_time(*args):
    """Sets the result in textbox when you select rider in rider_listbox"""
    rider_cursor = riders_listbox.curselection()
    if len(rider_cursor)==1:
        result_text.delete("1.0", "end")
        rider_number = int(rider_cursor[0])
        try:
            for item in riders_result:
                if item["name"] == riders_list[rider_number]:
                    for key, value in item.items():
                        result_text.insert("end", key)
                        if len(key) == 1:
                            result_text.insert("end", "  ")
                        else:
                            result_text.insert("end", " ")
                        result_text.insert("end", value)
                        result_text.insert("end", "\n")
        except ValueError:
            pass

root = Tk()
root.title("Motocross result")

riders_result = []
riders_list = []

main_window = ttk.Frame(root)
main_window.grid(column = 0, row = 0)

year_list = ttk.Combobox(main_window)
year_list["values"] = (18, 17, 16)
year_list.grid(column = 0, row = 0)

track_list = ttk.Combobox(main_window)
track_list["values"] = ("HANGTOWN", "GLEN-HELEN-RACEWAY", "THUNDER-VALLEY", "HIGH-POINT-RACEWAY",
                        " MUDDY-CREEK-RACEWAY", "REDBUD", "WICK-338", "SPRING-CREEK-MX-PARK",
                        "WASHOUGAL-MX-PARK", "BUDDS-CREEK-MOTOCROSS", "IRONMAN-RACEWAY")
track_list.grid(column = 0, row = 1)

class_list = ttk.Combobox(main_window)
class_list["values"] = (250, 450)
class_list.grid(column = 0, row = 2)

moto_list = ttk.Combobox(main_window)
moto_list["values"] = (1, 2)
moto_list.grid(column = 0, row = 3)

ttk.Label(main_window, text="Riders").grid(column=0, row=4)
riders_listbox = Listbox(main_window, height=10)
riders_listbox.grid(column = 0, row = 5, sticky=(N,E,S,W))

scroll_bar_listbox = ttk.Scrollbar(main_window, orient=VERTICAL, command=riders_listbox.yview)
scroll_bar_listbox.grid(column=0, row=5, sticky=(N,E,S))
riders_listbox.configure(yscrollcommand=scroll_bar_listbox.set)

ttk.Label(main_window, text="Result").grid(column=1, row=4)
result_text = Text(main_window, width=30, height=10)
result_text.grid(column = 1, row = 5)

scroll_bar_textbox = ttk.Scrollbar(main_window, orient=VERTICAL, command=result_text.yview)
scroll_bar_textbox.grid(column=1, row=5, sticky=(N,E,S))
result_text.configure(yscrollcommand=scroll_bar_textbox.set)

ttk.Button(main_window, text="Get result", command=get_info).grid(column=1, row=0, rowspan=4, sticky=(N,E,S,W))

riders_listbox.bind('<<ListboxSelect>>', get_time)

root.mainloop()
