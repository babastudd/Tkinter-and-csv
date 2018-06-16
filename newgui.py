import csv
import os
import Tkinter
from Tkinter import *
import Tkinter
from Tkinter import *
import tkFileDialog as filedialog
import os
from os import path
import ttk
import itertools
from itertools import *
import collections
from collections import *


def rowcount():
	filename = file_name.get()
	with open(filename) as f:
		reader = csv.reader(f,delimiter = ",")
		data = list(reader)
		row_count = len(data)-1
		return row_count

def que1():

	filename = file_name.get()
	supplier = supplier_name.get()
	file = open(filename ,'r')
	read = csv.reader(file)
	zipped = zip(*read)
	lis_cust = []
	for i in range(rowcount()):
		if(zipped[8][i] == supplier):
			#print zipped[7][i]
			lis_cust.append(zipped[7][i])

	new = Counter(lis_cust)
	mylis = list(new.most_common(10))
	top_cus = []
	no_tickets = []
	for i in mylis:
		top_cus.append(i[0])
		no_tickets.append(i[1])
	top_cus.insert(0,"Customers")
	no_tickets.insert(0,"Tickets")


	text = Text(window)
	for a,b in zip(top_cus,no_tickets): 
		text.insert( END, str("%-50s %s \n" % (a, b)))
	text.pack(fill=BOTH ,expand=True)


def filepath():
	filename = filedialog.askopenfilename()
	file_name.set(filename)
	return filename

def setfile():
	#read python file
	filename = file_name.get()
	file = open(filename ,'r')
	read = csv.reader(file)


def dropdown():
		#read supplier name
	filename = file_name.get()
	file = open(filename ,'r')
	read = csv.reader(file)
	header = read.next()
	zipped = zip(*read)
	Droplist = list(zipped[8])
	Droplist = set(Droplist)
	Droplist = list(Droplist)
	combo = ttk.Combobox(window ,textvariable = supplier_name)
	combo['values'] = Droplist
	supplier = combo.get()
	supplier_name.set(supplier)
	combo.pack()

window = Tk()
#vbar = Scrollbar(window ,orient = VERTICAL).pack(side=RIGHT ,fill=Y)
#hbar = Scrollbar(window ,orient = HORIZONTAL).pack(side=BOTTOM ,fill=X)
file_name = StringVar()
supplier_name = StringVar()
result = StringVar()

ques = StringVar()
window.title("Help Me !!!!!")
window.geometry('600x400')
lbl_browse =Label(text= "1-Click on Select File to choose file" ,font=("Arial Black",16))
lbl_browse.pack(fill= X)
fname = Entry(window,width = 100,textvariable = file_name)
fname.pack(fill=X)
browse = Button(text="Select file" , command = filepath)
browse.pack()
lbl_ok = Label(text ="2-Click on OK...!!! to confirm ur file",font=("Arial Black",16))
lbl_ok.pack(fill=X)
ok = Button(text="OK...!!!" , command = setfile)
ok.pack()
lbl_sup = Label(text= "3-Click on Supplier to get Supplier List" ,font=("Arial Black",16))
lbl_sup.pack(fill=X)
Supplier= Button(text="Supplier" , command = dropdown)
Supplier.pack()


#def new_winF(): # new window definition
#    newwin = Toplevel(window)
#    display = Label(newwin, text="Humm, see a new window !")
#    display.pack()    

#button1 =Button(window, text ="Continue", command =new_winF) #command linked
#button1.pack()

def clear1():
    list = window.pack_slaves()
    for l in list:
        l.destroy()
    lbl_ques=Label(text= "Select your Queries!!!" ,font=("Arial Black",16)).pack()
    Queries = ttk.Combobox(window,textvariable = ques)
    Queries["values"] = ["Total tickets filed by top 10 customers against a particular supplier" ,"Empty-1","Empty-2","Empty-3"]
    Queries.pack(fill=X)
    query_sel = Queries.get()
    ques.set(query_sel)
    Button(window,text='Continue',command=clear2).pack(side= BOTTOM)

def clear2():
	list = window.pack_slaves()
	for l in list:
		l.destroy()
	lbl_res=Label(text= "Results!!!" ,font=("Arial Black",16)).pack()   
	if(ques.get()=="Total tickets filed by top 10 customers against a particular supplier"):
		que1()
		
	else:
		lbl1= Label(text="No Queries",font=("Arial Black",16)).pack()
    	#lbl1.config( text = que1() )


Button(window,text='Continue',command=clear1).pack(side= BOTTOM)

window.mainloop()
#print file_name.get()
#print supplier_name.get()
#print ques.get()