from tkinter import*
def main():
    win=Tk()
    win.title("President")
    
    file = "presidenIndonesia.txt"
    L= displaymenjadiList(file)
    conOFListPresident=StringVar()
    lstPresident=Listbox(win,width=0,height=5,listvariable=conOFListPresident)
    lstPresident.grid(padx=100,pady=35)
    conOFListPresident.set(tuple(L))
    win.mainloop()

def displaymenjadiList(file):
    infile = open(file, 'r')
    listpres = [line.rstrip() for line in infile]
    infile.close()
    return listpres

main()