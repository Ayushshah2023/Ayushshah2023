import sqlite3
import time
import datetime
#import script

conn =sqlite3.connect('data1.db')
cur = conn.cursor()

def create_table():
	cur.execute('CREATE TABLE IF NOT EXISTS stufftoplot(id INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Genre TEXT,Price REAL,ISBN REAL,Publication TEXT,Rating REAL,Year TEXT)')


def data_entry():
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'Wimpy Kid','Jeff Kinney','Fiction-Humor',400,9797976979794,'Penguin',4.5,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'Sapiens','Yual Noah Harari','NonFiction-Documentary',369,97979979786794,'Penguin',5.0,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'The ABC Murders','Agatha Cristie','Fiction-Mystery',230,97456979979794,'Penguin',4.1,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'Angels and Demons','Dan Brown','Fiction-Mystery',318,9797569979794,'Penguin',4.5,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'The Acciddental Prime Mimister','Sanjay Baru','NonFiction-Political',290,9797976979794,'Penguin',4.0,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'Inferno','Dan Brown','Fiction-Mystery',309,97979979794,'Penguin',4.9,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'The Da Vinci Code','Dan Brown','Fiction-Mystery',314,9797997948794,'Penguin',3.5,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'Hippie','Paulo Coelho','NonFiction-SelfHelp',309,9797996579794,'Penguin',4.3,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'The Monk who sold his Ferrari','Robin Sharma','NonFiction-SelfHelp',126,9797997129794,'Jaico Publishing House',4.4,2018)")
	conn.commit()
	cur.execute("INSERT INTO stufftoplot VALUES(NULL,'The Immortals of Meluha','Amish Tripathi','Fiction-Mythological',234,97898380658742,'WestLand',4.1,2017)")
	conn.commit()


def insert():
##        Title=str(input("Enter the Title "))
##        Author=str(input("Enter the Author of the book"))
##        Genre=str(input("Enter the Genre of the book"))
##        Price=int(input("Enter the price of the book"))
##        ISBN=input("Enter the ISBN Number")
##        Publication=str(input("Enter the Publication of the book"))
##        Rating=float(input("Enter the rating of the book (less than 5)"))
##        unix=time.time()
##        Year=str(datetime.datetime.fromtimestamp(unix).strftime('%Y'))
        conn=sqlite3.connect("data1.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO stufftoplot VALUES (NULL,?,?,?,?,?,?,?,?) ",(Title,Author,Genre,Price,ISBN,Publication,Rating,Year))
        conn.commit()

#(Title,Author,Genre,Price,ISBN,Publication,Rating,Year)
##def insert(title,author,year,isbn):
##    conn=sqlite3.connect("data.db")
##    cur=conn.cursor()
##    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
##    conn.commit()
##    conn.close()
##    view()

def view():
    conn=sqlite3.connect("data1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM stufftoplot")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Title="",Author="",Genre="",Price="",ISBN="",Publication="",Rating="",Year=""):
    conn=sqlite3.connect("data1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM stufftoplot WHERE Title=? OR Author=? OR Genre=? OR Price=? OR ISBN=? OR Publication=? OR Rating=? OR Year=? ", (Title,Author,Genre,Price,ISBN,Publication,Rating,Year))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("data1.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM stufftoplot WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,Title,Author,Genre,Price,ISBN,Publication,Rating,Year):
    conn=sqlite3.connect("data1.db")
    cur=conn.cursor()
    cur.execute("UPDATE stufftoplot SET Title=?, Author=?,Genre=?,Price=?, ISBN=?, Publication=?, Rating=?, Year=? WHERE id=?",(Title,Author,Genre,Price,ISBN,Publication,Rating,Year,id))
    conn.commit()
    conn.close()

create_table()
data_entry()
##for i in range(2):
##        dynamic_data_entry()

cur.close()
conn.close()
	#best book under 350 rs
	#non fiction books
	#dan brown ki books
