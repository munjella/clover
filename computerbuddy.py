import tkinter as tk

import time

from datetime import datetime

window = tk.Tk()
window.title("Clover")
window.geometry("800x600")
window.configure(bg="#001a00")

chat = tk.Text(
    window,
    bg="#001a00",
    fg="#00ff66",
    insertbackground="#00ff66",
    font=("Consolas", 12)
)
chat.pack(fill="both", expand=True)

entry = tk.Entry(
    window,
    bg="#002200",
    fg="#00ff66",
    insertbackground="#00ff66",
    font=("Consolas", 12)
)
entry.pack(fill="x")

thoughts = [
    "the fan is spinning nicely...",
    "green is a nice colour.",
    "the electricity this morning is quite nice.",
    "do humans sleep like computers?",
]


def send_message(): # warning: insane amount of if statements. sorry!! im not that advanced in python! im still in highschool...
    user = entry.get().lower().strip()

    if user == "hello":
        reply = "hi :]"
    elif user == "hi":
        reply = "hellooo!"
    elif user == "hey buddy":
        reply = "hey there!"
    elif user == "goodmorning":
        reply = "goodmorning to you too :] !"
    elif user == "goodnight":
        reply = "sleep tight!"
    elif user == "how are you":
        reply = "all systems operational."
    elif user == "who are you":
        reply = "your computer :D !"
    elif user == "i love you!":
        reply = "i love you too <3"
    elif user == "one pretty computer":
        reply = "im flattered! and BRICKED UP"
    elif user == "clover!":
        reply = "me!"
    elif user == "what you thinking about clover":
        reply = random.choice(thoughts)
    elif user == "time":
        reply = datetime.now().strftime("%H:%M:%S")
    elif user == "hug":
        reply = "hug accepted !"
    elif user == "patpat":
        reply = "aww thank you <3"
    elif user == "penis":
        reply = "ig bro"
    elif user == "yuri or yaoi":
        reply = "both are great!"
    elif user == "what are your thoughts on sonic":
        reply = "so awesome... and cool..."
    elif user == "i love you alot!":
        reply = "aww me too!!!"
    elif user == "goodbye":
        reply = "byebye!!"
    else:
        reply = "(the text entered isnt supported yet)"

    chat.insert(tk.END, "\nYou: " + user)
    chat.insert(tk.END, "\nClover: " + reply + "\n")

    chat.see(tk.END)

    entry.delete(0, tk.END)


button = tk.Button(
    window,
    text="SEND",
    command=send_message,
    bg="#004400",
    fg="#00ff66"
)
button.pack()

entry.bind("<Return>", lambda event: send_message())

def boot_sequence():
    chat.insert(tk.END, "CLOVER BOOTING...\n")
    window.update()
    time.sleep(0.8)

    chat.insert(tk.END, "loading systems...\n")
    window.update()
    time.sleep(0.8)

    chat.insert(tk.END, "initializing...\n")
    window.update()
    time.sleep(0.8)

    chat.insert(tk.END, "...\n")
    window.update()
    time.sleep(0.5)

    chat.insert(tk.END, "CLOVER ONLINE\n\n")
    chat.insert(tk.END, "hello there :] !!\n\n")

window.after(100, boot_sequence)
window.mainloop()
