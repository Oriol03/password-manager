from tkinter import *
from tkinter import messagebox

from random import randint,choice,shuffle
import pyperclip
import json

#Save data 
def p_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[choice(letters) for char in range(randint(8, 10))]
    
    password_list+=[choice(symbols) for char in range(randint(2, 4))]
    password_list+=[choice(numbers) for char in range(randint(2, 4))]
  
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0,END)
    
    password_entry.insert(END,password)

def save():
    
    website=web_entry.get()
    password=password_entry.get()
    email=user_entry.get()
    new_data={website:{"email":email,"password": password}}
    

    if not (website and password):
        messagebox.showerror(title="Ooop",message="Don't let any field empty")
        
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"website: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save ?")
        if is_ok:
            try:
                with open ("data.json","r") as file_data:
                    data=json.load(file_data)
            except FileNotFoundError:
                with open("data.json", "w") as file : 
                    json.dump(new_data,file,indent=5)
            
            else:
                data.update(new_data)
                with open("data.json", "w") as file : 
                        json.dump(data,file,indent=5)
                         
            finally:
                web_entry.delete(0,END)
                password_entry.delete(0,END)
            
                    


def search():
    website=web_entry.get()
    try:
        with open ("data.json","r") as file_data:
            data=json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title="FileNotFound",message="There is no file created !!! ")
    
    else:    
        if website in data :
            messagebox.showinfo(title=website, message=f"email:   {data[website]["email"]} \nPassword:   {data[website]["password"]} ")
        else:
            messagebox.showerror(title="Ooops",message=f"There is no  data of {website} ")


new_data={}



window = Tk()
window.config(padx=50, pady=50)






canvas=Canvas(width=200, height=200)
image_logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(column=1, row=0)


#Labels

web_label=Label(text="Website")
web_label.grid(column=0, row=1)

user_label=Label(text="Username/Email")
user_label.grid(column=0,row=2)

password_label=Label(text="Password")
password_label.grid(column=0, row=3)

#Entry

web_entry=Entry(width=32)
web_entry.focus()
web_entry.grid(column=1,row=1)

user_entry=Entry(width=51)
user_entry.insert(END, "owenorioln@gmail.com")
user_entry.grid(column=1,row=2, columnspan=2)

password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)

#Button

generate_button=Button(text="Password Generate",command=p_generator)
generate_button.grid(column=2, row=3)

add_button=Button(text="Add",width=43,command=save)
add_button.grid(column=1, row=4,columnspan=2)

search_button=Button(text="Search", width=15,command=search)
search_button.grid(row=1,column=2)

window.mainloop()