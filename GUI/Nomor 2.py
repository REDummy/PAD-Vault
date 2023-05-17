# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:11:14 2023
Tugas Pertemuan #9 : Pemrosesan Data Nomor 2

@author: anton
"""

import tkinter as tk
import tkinter.ttk as ttk
import csv

class App:
    def __init__(self, master):
        self.master = master
        master.title("Program Info")

        # GUI stuffs like labels and whatnot
        self.label = tk.Label(master, text="Enter file name:")
        self.label.pack()

        self.filename_entry = tk.Entry(master)
        self.filename_entry.pack()

        self.select_button = ttk.Button(master, text="Select", command=self.read_file)
        self.select_button.pack()

        self.program_label = tk.Label(master, text="Nama Program:")
        self.program_label.pack()

        self.program_combo = ttk.Combobox(master, state="readonly", values=[])
        self.program_combo.pack()
        self.program_combo.bind("<<ComboboxSelected>>", self.update_fakultas_list)

        self.fakultas_label = tk.Label(master, text="Nama Fakultas:")
        self.fakultas_label.pack()

        self.fakultas_combo = ttk.Combobox(master, state="readonly", values=[],width=30)
        self.fakultas_combo.pack()
        self.fakultas_combo.bind("<<ComboboxSelected>>", self.update_prodi_list)

        self.prodi_label = tk.Label(master, text="Nama Prodi:")
        self.prodi_label.pack()

        self.prodi_listbox = tk.Listbox(master, width=50)
        self.prodi_listbox.pack()
        self.prodi_listbox.bind("<Double-Button-1>",self.show_info)

        self.info_label = tk.Label(master, text="Program Info:")
        self.info_label.pack()

        self.info_text = tk.Text(master, height=5)
        self.info_text.pack()

        # initialize variables
        self.data = []
        self.program_list = []
        self.fakultas_dict = {}

    def read_file(self):
        filename = self.filename_entry.get()+".csv"
        with open(filename, "r") as file:
            csv_reader = csv.reader(file, delimiter=";")
            self.data = list(csv_reader)

        # set values for fakultas_list and prodi_dict
        self.program_list = sorted(list(set([row[0] for row in self.data])))
        for program in self.program_list:
            self.fakultas_dict[program] = sorted(list(set([row[1] for row in self.data if row[0] == program])))
        
        # set values for program combo box
        self.program_combo["values"] = self.program_list
        self.program_combo.current(0) 

    def update_fakultas_list(self, event=None):
        selected_program = self.program_combo.get()
        self.fakultas_combo["values"] = self.fakultas_dict[selected_program]
        self.fakultas_combo.current(0)
        

    def update_prodi_list(self, event=None):
        selected_fakultas = self.fakultas_combo.get()
        self.prodi_listbox.delete(0, tk.END)
        self.prodi_listbox.insert(tk.END, *(row[2] for row in self.data if row[1] == selected_fakultas and row[0] == self.program_combo.get()))
        self.prodi_listbox.update()

    def show_info(self, event=None):
        selected_prodi = self.prodi_listbox.get(self.prodi_listbox.curselection())
        selected_row = [row for row in self.data if row[0] == self.program_combo.get() and row[1] == self.fakultas_combo.get() and row[2] == selected_prodi][0]
        info_text = f"Program: {selected_row[0]}\n" + \
                    f"Fakultas: {selected_row[1]}\n" + \
                    f"Prodi: {selected_row[2]}\n" + \
                    f"Jumlah Mahasiswa: {selected_row[3]}"
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, info_text)
        
root = tk.Tk()
app = App(root)
root.mainloop()
