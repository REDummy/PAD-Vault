import tkinter as tk
from tkinter import ttk 
import csv
import numpy as np
import matplotlib.pyplot as plt

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

        self.fakultas_label = tk.Label(master, text="Nama Fakultas:")
        self.fakultas_label.pack()

        self.fakultas_combo = ttk.Combobox(master, state="readonly", values=[])
        self.fakultas_combo.pack()
        self.fakultas_combo.bind("<<ComboboxSelected>>", self.update_prodi_list)


        self.prodi_label = tk.Label(master, text="Nama Prodi:")
        self.prodi_label.pack()

        self.prodi_listbox = tk.Listbox(master)
        self.prodi_listbox.pack()
        self.prodi_listbox.bind("<Double-Button-1>",self.show_info)


        self.info_label = tk.Label(master, text="Program Info:")
        self.info_label.pack()

        self.info_text = tk.Text(master, height=5)
        self.info_text.pack()

        self.data = []
        self.fakultas_list = []
        self.prodi_dict = {}
        
        jumlah_mhs_button = ttk.Button(self.master, text="Jumlah Mahasiswa per Fakultas", command=self.show_jumlah_mhs_per_fakultas)
        jumlah_mhs_button.pack()

        prodi_per_fakultas_button = ttk.Button(self.master, text="Jumlah Prodi per Fakultas", command=self.show_prodi_per_fakultas)
        prodi_per_fakultas_button.pack()

        prodi_per_program_button = ttk.Button(self.master, text="Jumlah Prodi per Program", command=self.show_prodi_per_program)
        prodi_per_program_button.pack()

    def read_file(self):
        filename = self.filename_entry.get()+".csv"
        with open(filename, "r") as file:
            csv_reader = csv.reader(file, delimiter=";")
            self.data = list(csv_reader)

        # set values for fakultas_list and prodi_dict
        self.fakultas_list = sorted(list(set([row[1] for row in self.data])))
        for fakultas in self.fakultas_list:
            self.prodi_dict[fakultas] = sorted(list(set([row[2] for row in self.data if row[1] == fakultas])))

        # set values for fakultas combo box
        self.fakultas_combo["values"] = self.fakultas_list
        self.fakultas_combo.current(0)

        # set values for prodi list box
        self.update_prodi_list()

    def update_prodi_list(self, event=None):
        selected_fakultas = self.fakultas_combo.get()
        self.prodi_listbox.delete(0, tk.END)
        self.prodi_listbox.insert(tk.END, *self.prodi_dict[selected_fakultas])
        self.prodi_listbox.update()


    def show_info(self, event=None):
        selected_prodi = self.prodi_listbox.get(self.prodi_listbox.curselection())
        selected_row = [row for row in self.data if row[1] == self.fakultas_combo.get() and row[2] == selected_prodi][0]
        info_text = f"Program: {selected_row[0]}\n" + \
                    f"Fakultas: {selected_row[1]}\n" + \
                    f"Prodi: {selected_row[2]}\n" + \
                    f"Jumlah Mahasiswa: {selected_row[3]}"
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, info_text)

    def show_jumlah_mhs_per_fakultas(self):
        fakultas_list = sorted(list(set([row[1] for row in self.data])))
        jumlah_mhs = np.array([sum([int(row[3]) for row in self.data if row[1] == fakultas]) for fakultas in fakultas_list])
        plt.bar(fakultas_list, jumlah_mhs)
        plt.title("Jumlah Mahasiswa per Fakultas")
        plt.xlabel("Nama Fakultas")
        plt.ylabel("Jumlah Mahasiswa")
        plt.show()

    def show_prodi_per_fakultas(self):
        fakultas_list = sorted(list(set([row[1] for row in self.data])))
        jumlah_prodi = np.array([len(set([row[2] for row in self.data if row[1] == fakultas])) for fakultas in fakultas_list])
        plt.bar(fakultas_list, jumlah_prodi)
        plt.title("Jumlah Prodi per Fakultas")
        plt.xlabel("Nama Fakultas")
        plt.ylabel("Jumlah Prodi")
        plt.show()

    def show_prodi_per_program(self):
        program_list = sorted(list(set([row[0] for row in self.data])))
        jumlah_prodi = np.array([len(set([row[2] for row in self.data if row[0] == program])) for program in program_list])
        plt.bar(program_list, jumlah_prodi)
        plt.title("Jumlah Prodi per Program")
        plt.xlabel("Nama Program")
        plt.ylabel("Jumlah Prodi")
        plt.show()   


root = tk.Tk()
app = App(root)
root.mainloop()