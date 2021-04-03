import tkinter as tk


class FirstPyGUI:

    def __init__(self):
        self.e1_value = None
        self.t1 = None

    def km_to_miles(self):
        print("Success!")
        print(self.e1_value.get())
        miles = float(self.e1_value.get()) * 1.6
        self.t1.insert(tk.END, miles)

    def converter_gui(self):
        window = tk.Tk()

        b1 = tk.Button(window, text="Execute", command=self.km_to_miles)
        b1.grid(row=0, column=0)
        b2 = tk.Button(window, text="QUIT", fg="red",
                       command=window.destroy)
        b2.grid(row=1, column=2)

        self.e1_value = tk.StringVar()
        e1 = tk.Entry(window, textvariable=self.e1_value)
        e1.grid(row=0, column=1)

        self.t1 = tk.Text(window, height=1, width=25, background='green')
        self.t1.grid(row=0, column=2)

        window.geometry("300x200")
        window.mainloop()


class KGConverter(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.e1_value = None
        self.t1, self.t2, self.t3 = None, None, None
        self.create_widgets()

    def create_widgets(self):
        l1 = tk.Label(self.master, text="Kg", justify="center")
        l1.grid(row=0, column=0)

        self.e1_value = tk.StringVar()
        e1 = tk.Entry(self.master, textvariable=self.e1_value)
        e1.grid(row=0, column=1)

        b1 = tk.Button(self.master, text="Convert", justify="center", command=self.convert_values)
        b1.grid(row=0, column=2)

        self.t1 = tk.Text(self.master, height=1, width=25, background='green')
        self.t1.grid(row=1, column=0)

        self.t2 = tk.Text(self.master, height=1, width=25, background='yellow')
        self.t2.grid(row=1, column=1)

        self.t3 = tk.Text(self.master, height=1, width=25, background='blue', foreground='white')
        self.t3.grid(row=1, column=2)

        b2 = tk.Button(self.master, text="QUIT", fg="red", command=self.master.destroy)
        b2.grid(row=2, column=2)

    def convert_values(self):
        print("Success!!")
        kg_value = float(self.e1_value.get())
        print("KG value =>", kg_value)
        # grams
        self.t1.delete("1.0", tk.END)
        self.t1.insert(tk.END, kg_value * 1000)

        # pounds
        self.t2.delete("1.0", tk.END)
        self.t2.insert(tk.END, kg_value * 2.20462)

        # ounces
        self.t3.delete("1.0", tk.END)
        self.t3.insert(tk.END, kg_value * 35.274)

    @staticmethod
    def run():
        root = tk.Tk()
        root.geometry('600x250')
        app = KGConverter(master=root)
        app.mainloop()


if __name__ == '__main__':
    FirstPyGUI().converter_gui()
    # KGConverter.run()
