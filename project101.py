from tkinter import *

# Set up the window
window = Tk()
window.title("Learn Igbo Language")
window.config(bg="white")  # Set the background color to white

# Function to clear placeholder text on focus
def clear_placeholder(event):
    if entry_text.get() == "Input the English word.":
        entry_text.delete(0, END)
        entry_text.config(fg="black")

# Function to add placeholder text if entry is empty
def add_placeholder(event):
    if entry_text.get() == "":
        entry_text.insert(0, "Input the English word.")
        entry_text.config(fg="gray")

# Entry for user input with placeholder text
entry_text = Entry(window, font=("Times New Roman", 14), bg="white", fg="gray", insertbackground="black")
entry_text.insert(0, "Input the English word.")
entry_text.bind("<FocusIn>", clear_placeholder)
entry_text.bind("<FocusOut>", add_placeholder)
entry_text.pack(pady=10)

# StringVar to display results
result = StringVar()
result_label = Label(window, textvariable=result, font=("Times New Roman", 14, "bold"), fg="blue", bg="white")
result_label.pack()

# Listbox to display suggestions
suggestion_list = Listbox(window, font=("Times New Roman", 12), bg="white", fg="black", selectbackground="lightblue", width=40, height=5)
suggestion_list.pack(pady=10)

# Dictionary with English as keys and Igbo as values
igbo_dictionary = {
    "day": "ụbọchị", "night": "abali", "water": "mmiri", "fire": "ọkụ", "earth": "ụwa",
    "tree": "osisi", "sun": "anwụ", "moon": "ọnwa", "star": "kpakpando", "river": "osimiri",
    "stone": "nkume", "mountain": "ugwu", "cloud": "urukpuru", "rain": "mmiri ozuzo",
    "light": "ụlọ", "darkness": "ọchịchịrị", "sky": "eluigwe", "wind": "ikuku",
    "leaf": "akwụkwọ", "fruit": "mkpọka", "grass": "ahịhịa", "flower": "okooko",
    "forest": "ọhịa", "path": "ụzọ", "house": "ụlọ", "door": "ụlọ ụzọ",
    "child": "nwa", "man": "nwoke", "woman": "nwanyị", "thing": "ihe", "place": "ebe",
    "eye": "anya", "ear": "nti", "mouth": "ọnụ", "side": "akụkụ", "bone": "ọkpụkpụ",
    "leg": "ụkwụ", "hand": "aka", "small": "obere", "of": "nke", "funny": "ihe ọchị",
    "fish": "azụ", "body": "ahụ", "word": "okwu", "school": "ụlọ akwụkwọ",
    "world": "ụwa ọzọ", "community": "ọha", "bank": "ụlọ akụ", "market": "azụmahịa",
    "boat": "ụgbọ", "holy": "nsọ", "blessing": "okwu ọma", "friend": "enyi",
    "training": "ọzụzụ", "work": "ọrụ", "happiness": "obi ụtọ", "new": "ọhụrụ",
    "color": "agba", "good day": "ụbọchị ọma", "children": "ụmụ"
}

# Function to search for a word in the English-to-Igbo dictionary
def search(word):
    word = word.lower()
    if word in igbo_dictionary.keys():
        result.set(igbo_dictionary[word])
    else:
        result.set("Word Not Found")

# Function to suggest words based on the first letter
def suggest(event):
    suggestion_list.delete(0, END)  # Clear the suggestion list
    text = entry_text.get().lower()
    for word in igbo_dictionary.keys():
        if word.startswith(text):
            suggestion_list.insert(END, word)

# Function to handle word selection from the suggestion list
def select_word(event):
    selected_word = suggestion_list.get(suggestion_list.curselection())
    entry_text.delete(0, END)
    entry_text.insert(0, selected_word)
    search(selected_word)  # Automatically search for the selected word

# Refresh function to clear the input and results
def refresh():
    entry_text.delete(0, END)
    entry_text.insert(0, "Input the English word.")
    entry_text.config(fg="gray")
    result.set("")
    suggestion_list.delete(0, END)

# Functions for hover effect
def button_hover_enter(e):
    e.widget.config(bg="lightblue", fg="black")

def button_hover_leave(e):
    e.widget.config(bg="SystemButtonFace", fg="black")

# Functions for suggestion hover effect
def suggestion_hover(event):
    index = suggestion_list.nearest(event.y)
    suggestion_list.selection_clear(0, END)
    suggestion_list.selection_set(index)

# Search button
search_btn = Button(window, text="Search", font=("Times New Roman", 14), command=lambda: search(entry_text.get()))
search_btn.pack(side=LEFT, padx=5)

# Refresh button
refresh_btn = Button(window, text="Refresh", font=("Times New Roman", 14), command=refresh)
refresh_btn.pack(side=LEFT, padx=5)

# Bind hover events for the buttons
search_btn.bind("<Enter>", button_hover_enter)
search_btn.bind("<Leave>", button_hover_leave)
refresh_btn.bind("<Enter>", button_hover_enter)
refresh_btn.bind("<Leave>", button_hover_leave)

# Bind events for suggestions and word selection
entry_text.bind("<KeyRelease>", suggest)  # Suggest words on key release
suggestion_list.bind("<<ListboxSelect>>", select_word)  # Handle selection from the list
suggestion_list.bind("<Motion>", suggestion_hover)  # Hover effect on suggestions

# Start the main loop
window.mainloop()