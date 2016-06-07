# imports:
import time
from socket import gethostname, gethostbyname
from tkinter import *
import tkinter.messagebox as box
import os
import webbrowser

# initialize_system_variables:
username = os.getlogin()
hostname = gethostname()
ipaddress = gethostbyname(gethostname())

# create_interface:
window = Tk()
window.title('IT Assistant | Technology Helping People')

# included_program_functions:
def open_ticket_url():
    webbrowser.open_new('http://yoururlhere/')

def ping_google():
    hostname = 'google.com'
    response = os.system('ping -n 1 ' + hostname)
    
    if response == 0:
        result = 'Connected'
    else:
        result = 'Not Connected'

    return result
    

wan_result = ping_google()




window.geometry('385x175') # static window dimensions
window.resizable(0,0) # disable window resizing option
display_username = Label(window, relief = 'groove', width = 25)
display_hostname = Label(window, relief = 'groove', width = 25)
display_ipaddress = Label(window, relief = 'groove', width = 25)
wan_status = Label(window, relief = 'groove', width = 25)
open_ticket = Button(window, text = 'OPEN TICKET')
exit_window = Button(window, text = 'CLOSE WINDOW')

# interface_layout:
display_username.grid()
display_hostname.grid()
display_ipaddress.grid()
wan_status.grid()
open_ticket.grid()
exit_window.grid()
# display_username.pack(side = 'left') //alternate layout notation to x.grid()
# display_hostname.pack(side = 'left', pady = 20)

# display_output:
display_username.configure(text = 'User: ' +username, font = (32))
display_hostname.configure(text = 'PC Name: ' +hostname, font = (32))
display_ipaddress.configure(text = 'IP Address: ' +ipaddress, font = (32))
wan_status.configure(text = 'WAN Status: ' +wan_result, font = (32))
open_ticket.configure(command = open_ticket_url) # leave () off function
exit_window.configure(command = window.destroy)  

# sustain_window:
window.mainloop()







