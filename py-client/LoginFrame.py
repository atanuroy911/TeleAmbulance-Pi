import os

import customtkinter
from PIL import Image
from functools import partial


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.logo_frame = LogoFrame(self, fg_color=["gray90", "gray13"], command=None)
        self.logo_frame.grid(row=0, column=1, padx=0, pady=0, sticky='ew')

        self.login_form = LoginForm(self, command=None)
        self.login_form.grid(row=1, column=1, padx=0, pady=0, sticky='n')

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.tata_logo_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "tata-communications.png")),
            dark_image=Image.open(os.path.join(image_path, "tata-communications.png")),
            size=(100, 50))
        self.tata_logo_image_label = customtkinter.CTkLabel(self, text="", image=self.tata_logo_image)
        self.tata_logo_image_label.grid(row=2, column=1, padx=20, pady=10, sticky='s')


class LogoFrame(customtkinter.CTkFrame):
    def __init__(self, master=LoginFrame, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "IIT_Kanpur_logo.png")),
            dark_image=Image.open(os.path.join(image_path, "IIT_Kanpur_logo_dark.png")),
            size=(200, 200))
        self.logo_image_label = customtkinter.CTkLabel(self, text="", image=self.logo_image)
        self.logo_image_label.grid(row=0, column=0, padx=20, pady=10, sticky='e')
        self.iot_logo_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "iot_light.png")),
            dark_image=Image.open(os.path.join(image_path, "iot_dark.png")),
            size=(300, 150))
        self.iot_logo_image_label = customtkinter.CTkLabel(self, text="", image=self.iot_logo_image)
        self.iot_logo_image_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')

class LoginForm(customtkinter.CTkFrame):
    def __init__(self, master=LoginFrame, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        username = customtkinter.StringVar()
        self.username_label = customtkinter.CTkLabel(self, text='Username:')
        self.username_label.grid(row=1, column=0, padx=15, pady=(15, 15), sticky='w')
        self.username_entry = customtkinter.CTkEntry(self, width=200, textvariable=username, placeholder_text="username")
        self.username_entry.grid(row=1, column=1, padx=30, pady=(15, 15))
        password = customtkinter.StringVar()
        self.password_label = customtkinter.CTkLabel(self, text='Password:')
        self.password_label.grid(row=2, column=0, padx=15, pady=(15, 15), sticky='w')
        self.password_entry = customtkinter.CTkEntry(self, width=200, textvariable=password, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=1, padx=30, pady=(0, 15))
        validateLogin = partial(self.validateLogin, username, password)
        self.login_button = customtkinter.CTkButton(self, text="Login", command=validateLogin, width=200)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=30, pady=(15, 15))

    def validateLogin(self, username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        return

