from tkinter import *
import random

root=Tk()
root.title("Testing random functions")
root.geometry("400x400")

input_pw = Entry(root)

guess_pw_label=Label(root)
generate_pw_label=Label(root)

array_3d = [[["head", "tail"], ["A", "B", "C", "D", "E", "F", "G", "H"], ["!", "@", "#", "$", "%"]]]
print(array_3d[0][2][3])


def new_password():
    
    guess_pw_label["text"]="Guessed password : "+ input_pw.get()
    
    random_no1 = random.randint(0, 1)
    random_no2 = random.randint(0, 7)
    random_no3 = random.randint(0, 4)

    letter1 = str(array_3d[0][0][random_no1])
    letter2 = str(array_3d[0][1][random_no2])
    letter3 = str(array_3d[0][2][random_no3])
    
    generate_pw_label["text"]="Generated password : "+ letter1 + "" + letter2 + "" + letter3 

input_pw.place(relx=0.5,rely=0.3,anchor=CENTER)
guess_pw_label.place(relx=0.5,rely=0.4,anchor=CENTER)

btn = Button(root, text = "New Password", command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

generate_pw_label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()