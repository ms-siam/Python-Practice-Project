'''import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #instead of (r'Batman | Batmobile | Batcopter | Batbat')
matchObject = batRegex.search('Batman lost his bat while driving Batmobile')
print(matchObject.group())
print(matchObject.group(1)) #group(1) will return the first group of the matched string

batRegex1 = re.compile(r'Bat(wo)?man') # ? means optional 
matchObject1 = batRegex1.search('The adventures of Batman')  
print(matchObject1.group()) # Batman
matchObject2 = batRegex1.search('The adventures of Batwoman')
print(matchObject2.group()) # Batwoman

from pathlib import Path
import os
print(Path.cwd())
os.chdir('C:\\Windows')
print(Path.cwd())
print(Path.home())
print(Path.cwd().is_absolute())
print(Path('Spam/bacon/eggs').is_absolute())

import send2trash
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not siam')
baconFile.close()
send2trash.send2trash('bacon.txt')

import os
for folderName, subFolders, filenames in os.walk('C:\\Users\\Mobarok Siam\\Desktop'):
    print(f"The folder name is: {folderName}")
    for subFolder in subFolders:
        print(f"Subfolder of {folderName}: {subFolder}")
    for filename in filenames:
        print(f"File inside of {folderName} : {filename}")
        
    print('')
    
from colorama import Fore, Style

print(Fore.RED + "This is red text!" + Style.RESET_ALL)
print(Fore.GREEN + "This is green text!" + Style.RESET_ALL)
print(Fore.YELLOW + "Warning: Something went wrong!" + Style.RESET_ALL)

from tabulate import tabulate

users = [
    (1, "Alice", 25, "Python, C++"),
    (2, "Bob", 22, "Java, SQL"),
    (3, "Charlie", 28, "JavaScript, Go")
]

# Define headers
headers = ["ID", "Name", "Age", "Skills"]

# Print table
print(tabulate(users, headers=headers, tablefmt="fancy_grid"))


import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("400x300")  # Width x Height

# Run the app
root.mainloop()



import tkinter as tk

def show_name():
    user_input = entry.get()
    label_result.config(text=f"Hello, {user_input}!")

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry field
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Submit", command=show_name)
button.pack(pady=10)

# Label to display result
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()
import tkinter as tk
import sqlite3

# Database setup
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")
conn.commit()

def add_task():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        task_id = listbox.get(selected_task).split(".")[0]
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        load_tasks()

def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for task in cursor.fetchall():
        listbox.insert(tk.END, f"{task[0]}. {task[1]}")

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

load_tasks()
root.mainloop()

conn.close()

ages = [12, 78, 23, 34,34,21,43, 45, 43, 95, 28, 19, 38, 18, 48, 56, 32, 27]
ages.reverse()
print(ages)
assert ages[0] <= ages[-1]

#Downloading a webpage with requests.get()

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
print(type(res))
print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:50])


#SAving downloaded files to hARD DRIVE

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)


# Creating a BeautifulSoup object from HTML

import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

print(type(noStarchSoup))

# loading an HTML file from hard drive
import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)

pElems = exampleSoup.select('p')

print(str(pElems[0]))

print(pElems[0].getText())

print(str(pElems[1]))

print(pElems[1].getText())

print(str(pElems[2]))

print(pElems[2].getText())


#Getting  data from an element's attributes

import bs4

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]

print(str(spanElem))

print(spanElem.get('id'))

print(spanElem.attrs)

# Controlling the browser with the selenium module

#Starting a selenium-controlled browser
from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com/')
try:
    elem = browser.find_element('class name', 'jumbotron')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name')


#Clicking the page

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element("link text", "Read Online for Free")
print(type(linkElem))

linkElem.click()

'''

#FIlinig out and submitting forms

from selenium import webdriver
browser = webdriver.Firefox()
