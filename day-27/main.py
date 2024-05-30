import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Aerial",24,"bold"))
my_label.pack(expand=True)

window.mainloop()