import subprocess as sub
import os
from tkinter import *

window = Tk()
window.title("Changing IPv4 address")
window.attributes('-topmost',True)
window.geometry('+950+680')

def clicked(arg):
  if arg == 1:
    lbl.configure(text="Button DHCP clicked")
    conf_ip.config(state="readonly")
    conf_sb.config(state="readonly")
    conf_gt.config(state="readonly")
    sub.getoutput('netsh int ip set address name = LAN source = dhcp')
    sub.getoutput('ipconfig /renew')
    ip()
    conf_ip.config(textvariable=out_ip)
    conf_sb.config(textvariable=out_sb)
    conf_gt.config(textvariable=out_gt)

  if arg == 2:
    lbl.configure(text="Set STATIC IP")
    conf_ip.config(state="normal"); out_ip.set("0.0.0.0")
    conf_sb.config(state="normal"); out_sb.set("255.0.0.0")
    conf_gt.config(state="normal"); out_gt.set("0.0.0.0")
    btn_enter = Button(window, text="Enter", command=lambda: static())
    btn_enter.config(width=15, height=1)
    btn_enter.grid(row=4, column=1)

  if arg == 3:
    lbl.configure(text="Button EXIT clicked")
    quit()

def static():
    conf_ip.config(state="readonly")
    conf_sb.config(state="readonly")
    conf_gt.config(state="readonly")
    sub.getoutput('netsh interface ip set address LAN static %s %s %s 1' % (conf_ip.get(), conf_sb.get(), conf_gt.get()))

def print_to_gui(text_string):
  conf_ip.config(text=text_string)
  window.update()

def ip ():
  global out_ip, out_sb, out_gt
  command1= 'netsh int ip show config LAN | findstr IP'
  comm1= sub.getoutput(command1).split( )
  out_ip= StringVar()
  command2= 'netsh int ip show config LAN | findstr Subnet'
  comm2_one= sub.getoutput(command2).split( )
  out_sb= StringVar()
  command3= 'netsh int ip show config LAN | findstr Default'
  comm3= sub.getoutput(command3).split( )
  out_gt= StringVar()
  try:
    out_ip.set(comm1[2])
  except:
    out_ip.set("Media disconnected")
  try:
    comm2=comm2_one[4].split(')')
    out_sb.set(comm2[0])
  except:
    out_sb.set("Media disconnected")
  try:
    out_gt.set(comm3[2])
  except:
    out_gt.set("Media disconnected")

lbl = Label(window, text="Select an option")
lbl.grid(row=0, columnspan=3)

ip()

conf_ip_text= Label(window, text="IP Address:")
conf_ip_text.grid(row=1, column=0, sticky=E)
conf_ip = Entry(state="readonly", textvariable=out_ip)
conf_ip.grid(row=1, column=1, columnspan=2)

conf_sb_text= Label(window, text="Mask Address:")
conf_sb_text.grid(row=2, column=0, sticky=E)
conf_sb = Entry(state="readonly", textvariable=out_sb)
conf_sb.grid(row=2, column=1, columnspan=2)

conf_gt_text= Label(window, text="Gateway Address:")
conf_gt_text.grid(row=3, column=0, sticky=E)
conf_gt = Entry(state="readonly", textvariable=out_gt)
conf_gt.grid(row=3, column=1, columnspan=2)

btn_DHCP = Button(window, text= "DHCP", command=lambda: clicked(1))
btn_DHCP.config(width=15, height=1)
btn_DHCP.grid(row=4, column=0)
btn_IP= Button(window, text='STATIC', command=lambda: clicked(2))
btn_IP.config(width=15, height=1)
btn_IP.grid(row=4, column=2)
btn_EXIT = Button(window, text="Exit", command=lambda: clicked(3))
btn_EXIT.config(width=15, height=1)
btn_EXIT.grid(row=5, column=1)

window.mainloop()

