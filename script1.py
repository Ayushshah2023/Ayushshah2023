"""
A program that stors this book information
title,Author,Year,ISBn<Price,Ratings,Publications,Genre

User can view all records 
Search any entry
Add any entry
Update an entry
Delete
CLose
add a rating to any book
Scroll bar

"""

import data_py
from tkinter import *
from PIL import ImageTk,Image
#window=Tk()
#canvas=Canvas(window,width=300,height=160)
#canvas.grid(row=12,column=3)
#image1 =ImageTk.PhotoImage(Image.open("layout.png"))
#canvas.create_image(anchor=NW,image=image1)
#canvas.grid(row=0,column=0)
#x=Label(image=image1)
#x.grid(row=0,column=0)
# = Label(top, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

def get_selected_row(event):
    try:
        global selected_tuple
        index1=list1.curselection()
        print(index1)
        index = int(''.join(map(str,index1)))
        print(index)
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
        e7.delete(0,END)
        e7.insert(END,selected_tuple[7])
        e8.delete(0,END)
        e8.insert(END,selected_tuple[8])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in data_py.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in data_py.search(title_text.get(),author_text.get(),genre_text.get(),price_text.get(),ISBN_text.get(),Publn_text.get(),ratings_text.get(),Year_text.get()):
        list1.insert(END,row)

def add_command():
    data_py.insert(title_text.get(),author_text.get(),genre_text.get(),price_text.get(),ISBN_text.get(),Publn_text.get(),ratings_text.get(),Year_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),genre_text.get(),price_text.get(),ISBN_text.get(),Publn_text.get(),ratings_text.get(),Year_text.get()))

def delete_command():
    data_py.delete(selected_tuple[0])

def update_command():
    data_py.update(selected_tuple[0],title_text.get(),author_text.get(),genre_text.get(),price_text.get(),ISBN_text.get(),Publn_text.get(),ratings_text.get(),Year_text.get())

window=Tk()

l1=Label(window,text="Welcome to my BookStore")
l1.grid(row=0, column=0, columnspan=4, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

l2=Label(window,text="Title")
l2.grid(row=2, column=0,columnspan=2, padx=5, pady=5)

l3=Label(window,text="Author")
l3.grid(row=2, column=3,columnspan=2, padx=5, pady=5)

l4=Label(window,text="Genre")
l4.grid(row=3, column=0,columnspan=2, padx=5, pady=5)

l5=Label(window,text="Price")
l5.grid(row=3, column=3,columnspan=2, padx=5, pady=5)

l6=Label(window,text="ISBN Number")
l6.grid(row=4, column=0,columnspan=2, padx=5, pady=5)

l7=Label(window,text="Publications")
l7.grid(row=4, column=3,columnspan=2, padx=5, pady=5)

l8=Label(window,text="Ratings(out of 5")
l8.grid(row=5, column=0,columnspan=2, padx=5, pady=5)

l9=Label(window,text="Year of Publn")
l9.grid(row=5, column=3,columnspan=2, padx=5, pady=5)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=2, column=2, padx=5, pady=5)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=2, column=5, padx=5, pady=5)

genre_text=StringVar()
e3=Entry(window,textvariable=genre_text)
e3.grid(row=3, column=2, padx=5, pady=5)

price_text=StringVar()
e4=Entry(window,textvariable=price_text)
e4.grid(row=3, column=5, padx=5, pady=5)

ISBN_text=StringVar()
e5=Entry(window,textvariable=ISBN_text)
e5.grid(row=4, column=2, padx=5, pady=5)

Publn_text=StringVar()
e6=Entry(window,textvariable=Publn_text)
e6.grid(row=4, column=5, padx=5, pady=5)

ratings_text=StringVar()
e7=Entry(window,textvariable=ratings_text)
e7.grid(row=5, column=2, padx=5, pady=5)

Year_text=StringVar()
e8=Entry(window,textvariable=Year_text)
e8.grid(row=5, column=5, padx=5, pady=5)


list1=Listbox(window,height=6,width=100)
list1.grid(row=6,column=0, rowspan=5 ,columnspan=5, padx=5, pady=5)

sb1=Scrollbar(window)
sb1.grid(row=6,column=5,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command,padx=5)
b1.grid(row=11,column=0)

b2=Button(window,text="Search entry", width=12,command=search_command,padx=5)
b2.grid(row=11,column=1)

b3=Button(window,text="Add entry", width=12,command=add_command,padx=5)
b3.grid(row=11,column=2)

b4=Button(window,text="Update selected", width=12,command=update_command,padx=5)
b4.grid(row=11,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command,padx=5)
b5.grid(row=11,column=4)

b6=Button(window,text="Close", width=12,command=window.destroy,padx=5)
b6.grid(row=11,column=5)
#canvas.pack()
window.mainloop()
