import os
import tkinter
import requests
import customtkinter
import tkintermapview
from PIL import Image
from GradientFrame import GradientFrame
from LoginFrame import LoginFrame

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("theme.json")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Tele Ambulance Client App [Beta Testing]")
        # setting attribute

        # getting screen width and height of display
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        # self.attributes('-fullscreen', True)
        self.geometry(f"{self.width}x{self.height}")

        gf = GradientFrame(self, colors=("pink", "white"), width=self.width, height=self.height)
        gf.config(direction=gf.top2bottom)
        gf.grid(row=0, column=0, columnspan=99, rowspan=99, padx=0, pady=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Login_Frame = LoginFrame(master=self, command=None)
        self.Login_Frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
