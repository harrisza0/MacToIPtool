import tkinter as tk
import netmiko
from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass

import sys

def decorator(func):
    def inner(inputStr):
        try:
            textbox.insert(INSERT, inputStr)
            return func(inputStr)
        except:
            return func(inputStr)
    return inner

sys.stdout.write=decorator(sys.stdout.write)
#print=decorator(print)  #you can actually write this but not recommended

window = tk.Tk()

    
def GetIP():

    
    username = e1.get()

    password = e2.get()

    
 
    cisco_router = {
     'device_type': 'cisco_ios',
     'host':   '172.16.3.180',
     'username': username,
     'password': password,
     'port' : 22,          # optional, defaults to 22
     #'secret': 'cisco',     # optional, defaults to ''#
     } 

    net_connect = ConnectHandler(**cisco_router)
    global output
    output = net_connect.send_command('Show arp | i ' + (e3.get()))
    print(output)
    #print('show mac address | i' + (e3.get()))#
    # define new text (you can modify this to your needs!)
    new_text = output
    
        
    def clear_text():
         label.config(text="")
    
    def resultpopup():
        
        
        def leavemini():
            window.destroy()
    label = tk.Label(window, text=output, anchor='center', bg='#858585')
    label.grid(columnspan=3, rowspan=20)
    B1 = tk.Button(window, text="Clear Last Result", command =clear_text)
    B1.grid(row=5, column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
    window.mainloop()
    
    # set connected text variable to new_text
    entry_text.set(new_text)
    resultpopup()
    
    

ipresult = '(test)'


window.title("MACtoIPtool")
window.geometry("500x500")


tk.Label(window, text="Username").grid(row=0)
tk.Label(window, text="Password").grid(row=1)
tk.Label(window, text="Mac Address (xxxx.xxxx.xxxx Format)").grid(row=2)

entry_text = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_text)


e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

e2.config(show="*")


tk.Button(window, 
          text='Quit', background = "#ae5c5c", 
          command=window.quit).grid(row=46, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(window, 
          text='GET IP', command=GetIP).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
                                                       



window.mainloop()