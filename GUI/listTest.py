from tkinter import*
def deleteAndAdd(event=None) :#hapus item yang dipilih dari listbox kiri dan tambah ke listbox kanan
    selection = listbox.get(listbox.curselection())
    listbox.delete(listbox.curselection())
    listbox2.insert(END, selection)

def deleteAndAdd2(event=None) :#sama seperti method atas tpi sebaliknya
    selection = listbox2.get(listbox2.curselection())
    listbox2.delete(listbox2.curselection())
    listbox.insert(END, selection)

window = Tk()
window.geometry('255x200')
window.title("Listbox Test")
listbox = Listbox(window, highlightcolor = "red",highlightthickness="1.5px")
listbox2 = Listbox(window, highlightcolor = "blue",highlightthickness="1.5px")

textList = ["red", "yellow","green","blue"]
i = 1
for j in textList :
    listbox.insert(i,j)
    i=+1

#bind function ke double left click
listbox.bind("<Double-Button-1>",deleteAndAdd)
listbox2.bind("<Double-Button-1>",deleteAndAdd2)

listbox.grid(row=1,column=1) 
listbox2.grid(row=1,column=2) 

mainloop()
