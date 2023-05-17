from tkinter import* 

def ubahButton():#ubah warna button dan ubah warna teks dan case entry
        current_color = button["fg"]
        new_color = "red" if current_color == "blue" else "blue"
        button["fg"] = new_color
        ubahEntry()

def ubahCase(event=None) :#ubah case dari entry
        text = entry.get()
        if text.isupper() :
            tempText=text.lower()
        else :
            tempText = text.upper()
        temp.set(tempText)

def ubahEntry():#ubah warna dan case dari entry
        current_color = entry["fg"]
        new_color = "red" if current_color == "blue" else "blue"
        entry["fg"] = new_color 
        ubahCase()
        
                
    
#buat window and bind method ke button 3
window = Tk("Program Ubah Warn")
window.geometry('200x200')
window.title("GUI Test")
button = Button(window, text="Ubah Warna", fg="blue", command=ubahButton)
temp = StringVar()
entry = Entry(window, fg="blue", textvariable=temp)
entry.bind("<Button-3>",ubahCase)
entry.pack()
button.pack()

mainloop()
