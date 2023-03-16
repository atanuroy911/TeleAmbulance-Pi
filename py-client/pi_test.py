import serial
from time import sleep
import sys
import requests
import customtkinter
import tkinter
import threading
import random



# ser = serial.Serial("/dev/ttyAMA0")
gpgga_info = "$GPGGA,"
GPGGA_buffer = 0
NMEA_buff = 0

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.set_default_color_theme("theme.json")

tracking = False
latitude = 0
longitude = 0
latitude_label = None

def track():
    try:
        # print("Initializing ...")
        # print(tracking)
        if tracking:
            threading.Timer(2.0, track).start()
            global latitude, longitude, latitude_label
            latitude = random.randint(0, 100)
            longitude = random.randint(0, 100)
            latitude_label.configure(text=f"Latitude: {latitude.__str__()}")

            # received_data = (str)(ser.readline())  # read NMEA string received
            # # print(received_data)
            # GPGGA_data_available = received_data.find(gpgga_info)  # check for NMEA GPGGA string
            # if (GPGGA_data_available > 0):
            #     GPGGA_buffer = received_data.split("$GPGGA,", 1)[1]  # store data coming after "$GPGGA," string
            #     NMEA_buff = (GPGGA_buffer.split(','))
            #     nmea_time = []
            #     nmea_latitude = []
            #     nmea_longitude = []
            #     nmea_time = NMEA_buff[0]  # extract time from GPGGA string
            #     nmea_latitude = NMEA_buff[1]  # extract latitude from GPGGA string
            #     nmea_longitude = NMEA_buff[3]  # extract longitude from GPGGA string
            #     print("NMEA Time: ", nmea_time, '\n')
            #     try:
            #         lat = (float)(nmea_latitude)
            #     except:
            #         lat = 0.0
            #     lat = convert_to_degrees(lat)
            #     try:
            #         longi = (float)(nmea_longitude)
            #     except:
            #         longi = 0.0
            #     longi = convert_to_degrees(longi)
            #     print("NMEA Latitude:", lat, "NMEA Longitude:", longi, '\n')
            #     send_to_url(lat, longi)

    except KeyboardInterrupt:
        sys.exit(0)

def start_tracking():
    print("Tracking Initiating ...")
    global tracking
    tracking = True
    track()

def stop_tracking():
    print("Tracking Stopped  ...")
    global tracking
    tracking = False

def convert_to_degrees(raw_value):
    decimal_value = raw_value / 100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value)) / 0.6
    position = degrees + mm_mmmm
    position = "%.4f" % (position)
    return position


def send_to_url(lat, long):
    url = 'http://172.27.28.47:3000/addgpsdata'
    myobj = {
        'assetnumber': '1234',
        'latitude': lat,
        'longitude': long
    }

    x = requests.post(url, json=myobj)

    print(x.text)


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

        self.geometry(f"{self.width}x{self.height}")

        self.TrackFrame = TrackFrame(master=self)
        self.TrackFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


class TrackFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global latitude, latitude_label
        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, text="Start GPS Tracking", justify=customtkinter.LEFT)
        label_1.pack(pady=10, padx=10)

        button_1 = customtkinter.CTkButton(master=frame_1, text="Start", command=start_tracking)
        button_1.pack(pady=10, padx=10)

        frame_2 = customtkinter.CTkFrame(master=self)
        frame_2.pack(pady=20, padx=60, fill="both", expand=True)

        label_2 = customtkinter.CTkLabel(master=frame_2, text="Stop GPS Tracking", justify=customtkinter.LEFT)
        label_2.pack(pady=10, padx=10)

        button_2 = customtkinter.CTkButton(master=frame_2, text="Stop", command=stop_tracking)
        button_2.pack(pady=10, padx=10)

        frame_3 = customtkinter.CTkFrame(master=self)
        frame_3.pack(pady=20, padx=60, fill="both", expand=True)

        label_3 = customtkinter.CTkLabel(master=frame_3, text="Values", justify=customtkinter.LEFT)
        latitude_label = customtkinter.CTkLabel(master=frame_3, text=f"Latitude: {latitude.__str__()}", justify=customtkinter.LEFT)
        label_3.pack(pady=10, padx=10)
        latitude_label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()