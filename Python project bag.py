from tkiner import *
import random 

root=Tk()
root.title("List")
root.geometry("500x500")

label1 = Label(root)
label2 = Label(root)

List1 = ["Bottle", "Tiffin", "ID Card", "Tickets", "Bagpack"]
label1["text"] = "Listed_items :  " + str(List1) 

def bag_contents():
    
    random_list = random.sample(range(0,5),1)
    label2["text"] = "Put Item No   " + str(random_list) + "  in bag"
    
    label1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    btn1 = Button(root)
    btn1 = Button(root, text="Which Item to put in bag?  "  ,command = random_number)
    btn1.place(relx = 0.5, rely = 0.5, anchor=CENTER )

    
    label2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    root.mainloop()