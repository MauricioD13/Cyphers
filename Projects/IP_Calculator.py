
from tkinter import *
import IP_address
window0=Tk()    
window0.title("IP Address GUI")
window0.geometry("500x500")
# Function
def clicked():
    result=IP_address.ip_finder(ip_txt.get(),mask_txt.get())
    result_mask.configure(text=result[0])
    result_wildcard.configure(text=result[1])
    result_net_address.configure(text=result[2])
    result_user_available.configure(text=result[3])

# Objects
ip_label=Label(window0, text="IP Address")
mask_label=Label(window0,text="Mask")
btn=Button(window0, text="Calculate", command=clicked)
ip_txt=Entry(window0,width=20)
mask_txt=Entry(window0,width=20)
result_mask=Label(window0,text="---.---.---.---")
result_wildcard=Label(window0, text="---.---.---.---")
result_net_address=Label(window0, text="---.---.---.---")
mask_label_result=Label(window0,text="Mask")
wildcard_label_result=Label(window0,text="Wildcard")
net_address_label_result=Label(window0,text="Net Address")
user_available_label_result=Label(window0,text="Hosts")
result_user_available=Label(window0, text="-")
empty_label=Label(window0,text="      ")
empty0_label=Label(window0,text="    ",width="10")

#Location 
ip_label.grid(row=0, column=0)
ip_txt.grid(row=1, column=0)
empty_label.grid(row=1, column=1)
mask_label.grid(row=0,column=2)
mask_txt.grid(row=1, column=2)
btn.grid(row=1, column=4)
empty0_label.grid(row=2,column=2)
mask_label_result.grid(row=3, column=0)
wildcard_label_result.grid(row=3,column=1)
net_address_label_result.grid(row=3,column=2)
user_available_label_result.grid(row=3,column=3)
result_mask.grid(row=4, column=0)
result_wildcard.grid(row=4, column=1)
result_net_address.grid(row=4, column=2)
result_user_available.grid(row=4, column=3)
window0.mainloop()