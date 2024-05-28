from tkinter import*
from app_settings import*
from PIL import ImageTk, Image # type: ignore #Import ImageTk and Image from PIL

class App():
    
    def __init__(self):
        #Creating the main window
        self.window=Tk()
        self.window.title("Cash Control")

        #size of window
        self.window.geometry("1440x1024")

        # Load and stretch the background image
        image = Image.open("Images/background.png")
        photo = ImageTk.PhotoImage(image.resize((1440, 1024)))

        # Create a label for the background image
        bg_label = Label(self.window, image=photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
         
        #Logo   
        logo_image = PhotoImage(file="Images/Logo.png")
        self.logo_label = Label(self.window, image=logo_image, bg="white")
        self.logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        #Username
        self.username_label = Label(self.window, text="Username: ")
        self.username_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.username_entry = Entry(self.window)
        self.username_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        #Password
        self.password_label = Label(self.window, text="Password: ")
        self.password_label.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.password_entry = Entry(self.window, show="*")
        self.password_entry.place(relx=0.5, rely=0.65, anchor=CENTER)

        #Login Button
        self.login_button = Button(self.window,text="ENTER", command=self.login, bg="#CB997E")
        self.login_button.place(relx=0.5, rely=0.75, anchor=CENTER)

        self.window.mainloop()
    #Function to print username and password
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Username: ", username)
        print("Password: ", password)

        #Hide login widgets
        self.username_label.place_forget()
        self.username_entry.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()
    
        ####### MAIN PAGE #######

        

#instance of my app
app = App()