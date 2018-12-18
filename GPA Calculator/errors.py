import tkinter


def create_window(window):
    window.title("Warning")
    window.geometry("230x80+500+250")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.maxsize(width=230, height=80)
    window.minsize(width=230, height=80)


def input_error(value):
    errorWindow = tkinter.Tk()
    errorWindow["padx"] = 5
    errorWindow["pady"] = 5

    create_window(errorWindow)
    warning_label = tkinter.Label(errorWindow, text="Please input a {}".format(value))
    warning_label.grid(row=0, column=0, sticky="ew")

    cancel_button = tkinter.Button(errorWindow, text="Cancel", command=errorWindow.destroy)
    cancel_button.grid(row=1, column=0, sticky="n")

    errorWindow.mainloop()


def detail_error(value):
    errorWindow = tkinter.Tk()
    errorWindow["padx"] = 5
    errorWindow["pady"] = 5

    create_window(errorWindow)
    warning_label = tkinter.Label(errorWindow, text="The {} field cannot be empty".format(value))
    warning_label.grid(row=0, column=0, sticky="ew")

    cancel_button = tkinter.Button(errorWindow, text="Cancel", command=errorWindow.destroy)
    cancel_button.grid(row=1, column=0, sticky="n")

    errorWindow.mainloop()
