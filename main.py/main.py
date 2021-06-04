import requests
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Chuck Norris Jokes')
root.geometry('300x300')
root.resizable('False', 'False')
root.config(bg='#82db74')

chuck_joke = Message(root, text='', bg='#82db74')
chuck_joke.place(relx=0.2, rely=0.2)


def joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        chuck_joke.config(text=data['value'])

    except requests.exceptions.ConnectionError:
        messagebox.showerror(message='No Internet Connection')


button = Button(root, text='New Joke', command=joke, bg='#72bf65')
button.place(relx=0.3, rely=0.7)

root.mainloop()
