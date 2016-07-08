#     t k P h o n e . p y
#       updated with save phone list changes
#       and made functional as originally intended
from Tkinter import *
from phones import *
import pickle


# Set selection target
def whichSelected():
    print "At %s of %d" % (select. curselection(), len(phonelist))
    return int(select.curselection()[0])
    
# Add to Phone List
def addEntry():
    phonelist.append([nameVar.get(), phoneVar.get()])
    setSelect()
    
# Update Selected Entry with Changes
def updateEntry():
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect()

# Delete Selected Entry
def deleteEntry():
    del phonelist[whichSelected()]
    setSelect()

# Load Selected Entry
def loadEntry():
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

# Save Changes to File for next form load
def saveEntry():
    print ''
    #pickle.dump(phonelist, 'phones.py')
    
# Create GUI Window
def makeWindow():
    global nameVar, phoneVar, select
    win = Tk()
    win.title("Phone List")
    win.resizable(False, False)

    # Labels Frame
    frame1 = Frame(win)
    frame1.pack(pady=1)

    # Name Label
    Label(frame1, text="Name").grid(row=0, column=0, sticky='w', padx=1)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar, width=30)
    name.grid(row=0, column=1, sticky='w', padx=1)

    # Phone Label
    Label(frame1, text="Phone").grid(row=1, column=0, sticky='w', padx=1)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar, width=30)
    phone.grid(row=1, column=1, sticky='w', padx=1)

    # Buttons Frame
    frame2 = Frame(win)
    frame2.pack(pady=1)
    b1 = Button(frame2, text=" Add  ", command=addEntry)
    b2 = Button(frame2, text="Update", command=updateEntry)
    b3 = Button(frame2, text="Delete", command=deleteEntry)
    b4 = Button(frame2, text=" Load ", command=loadEntry)
    b5 = Button(frame2, text=" Save ", command=saveEntry)
    b1.pack(side=LEFT, padx=1); b2.pack(side=LEFT, padx=1)
    b3.pack(side=LEFT, padx=1); b4.pack(side=LEFT, padx=1)
    b5.pack(side=RIGHT, padx=1)

    #Name List Frame
    frame3 = Frame(win)
    frame3.pack(padx=1, pady=1)
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6, width = 35)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y, pady=1)
    select.pack(side=LEFT, fill=BOTH, expand=1, padx=1, pady=1)

    return win


# Populate Selection List box
def setSelect():
    phonelist.sort()
    select.delete(0, END)
    for name, phone in phonelist:
        select.insert(END, name)


win = makeWindow()
setSelect()
win.mainloop()
