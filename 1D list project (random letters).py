from tkinter import *

import random 

root=Tk()
root.title("Random AlphaBet")
root.geometry("500x500")

list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def random_alphabet():
    random_alphabet1 = random.randint(1,26)
    random_alphabet2 = random.randint(1,26)
    random_alphabet3 = random.randint(1,26)
    random_alphabet4 = random.randint(1,26)
    random_alphabet5 = random.randint(1,26)
    
    
    random_alpha1 = list1[random_alphabet]
    random_alpha2 = list1[random_alphabet]
    random_alpha3 = list1[random_alphabet]
    random_alpha4 = list1[random_alphabet]
    random_alpha5 = list1[random_alphabet]

    
btn = Button(root)
btn = Button(root, text="Random Alphabet ", command = random_alphabet)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()