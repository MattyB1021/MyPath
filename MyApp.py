import Tkinter as tk
from Tkinter import *
import pickle
import os

data = []


class MyPath(tk.Frame):


    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        MyPath.make_widgets(self)

    def make_widgets(self):
        self.parent.title("MyPath")


        # create a prompt, an input box, an output label,
        # and a button to do the saving
        self.prompt = tk.Label(self, text="Enter your Filepath:", anchor="w")
        self.textbox = tk.Text(self)
        self.entry = tk.Entry(self)
        self.open = tk.Button(self, text="Open", command = self.open)
        self.view = tk.Button(self, text="View", command = self.view)
        self.submit = tk.Button(self, text="Save", command = self.save)
        self.output = tk.Label(self, text="")
        self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text)

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.textbox.pack(side="top", fill="x")
        self.view.pack(side="bottom")
        self.submit.pack(side="bottom")
        self.clear_button.pack(side="bottom")
        self.open.pack(side="top")


    def clear_text(self):
        self.entry.delete(0, 'end')
        self.textbox.delete(1.0, 'end')


    def save(self):
        # get the value from the input widget
        try:
            a = self.entry.get()
            result = data.append(self.entry.get())
            scribe = open('favorites.txt', 'w')
            scribe.writelines(data)

        except ValueError:
            result = "Please enter filepaths only"

        #saves list to pickle file
        #pickle.dump(data, open("save.p", "wb"))
        # set the output widget to have our result
        self.output.configure(text=result)
        print (data)

    def view(self):
        self.textbox.insert("1.0", str(data))
        #pickle.load(open("save.p", "rb"))
        #print pickle.load(open("save.p", "rb"))

    def open(self):
        #src = "/Users/matt/Documents/Python/MyApp.py"
        #dst = data
        #path = pickle.load(open("save.p", "rb"))
        os.system('Explorer "%s"' % favorites.txt)

master = Tk()

variable = StringVar(master)
variable.set("Favorites") # default value

favList = OptionMenu(master, variable, data, command = open)
favList.pack(side="bottom")

if __name__ == "__main__":
    root = tk.Tk()
    MyPath(root).pack(fill="both", expand=True)
    root.mainloop()
