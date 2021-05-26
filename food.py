import tkinter as tk
import speech_recognition
import nltk
from newspaper import Article

my_recipes = {
    'Pancake' : ["flour", "eggs", "milk"],
    'Burger' : ["beef", "buns", "lettuce", "cheese"],
    'HotDog' : ["sausage", "buns", "ketchup", "mustard"],
    'Pizza': ["dough", "tomatoes", "cheese"],
    'Tacos': ["nachos", "beef", "cheese", "avocado", "salsa"],
    'Kebab': ["kebab", "fried", "sallad", "sauce"]
}

my_urls = {
    'Pancake' : ["https://www.arla.se/recept/pannkaka/"],
    'Burger' : ["https://www.arla.se/recept/hamburgare-for-alla/"],
    'HotDog' : ["lääänk"],
    'Pizza': ["liiiink"],
    'Tacos': ["tacoooos"],
    'Kebab': ["priiiint"]
}

root = tk.Tk()

mat_var = tk.StringVar()
k = tk.StringVar()
v = tk.StringVar()

def srtotext():
    mat.delete(0, "end")
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)

            try:
                text = recognizer.recognize_google(audio)
                text = text.lower()

                mat.insert(0, text)

            except:
                mat.insert(0, "Sorry could not hear")

def skrivtext():
    recepten.delete("1.0","end")
    mattext = mat.get()
    ingredients = mattext.split()

    for k, v in my_recipes.items():
        # checks to see if all items in values
        # are in the ingredients list
        if all(i in ingredients for i in v):
            # if they are, print out what can be made
            recepten.insert("1.0", (f"You can make {k}\n"))
            urlen.insert(0, my_urls[k])
            #return my_urls[k]
        elif any(i in ingredients for i in v):
            recepten.insert("1.0", (f"Buy some more ingredients for {k}\n"))
        else:
            continue

def korttext():
    urlis = skrivtext()

    article = Article(urlis)
    article.download()
    article.parse()

    article.nlp()

    samman.insert('1.0', article.summary)

canvas =tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=5)

info = tk.Label(root, text="Enter what you have in your fridge")
info.grid(columnspan=3, column=0, row=0)

mat = tk.Entry(root, textvariable = mat_var)
mat.grid(columnspan=1, column=1, row=1)

prata = tk.Button(root, text="speak", command=srtotext)
prata.grid(columnspan=1, column=0, row=1)

knapp = tk.Button(root, text="enter", command=skrivtext)
knapp.grid(columnspan=1, column=2, row=1)

recepten = tk.Text(root, width=50, height=3)
recepten.grid(column=1, row=2)

urlen = tk.Entry(root, width=50)
urlen.grid(column=1, row=3)

samman = tk.Text(root, width=50, height=3)
samman.grid(column=1, row=4)

root.mainloop()

#Lägg till nytt recept
#k=input("Please input a Recipe: ")
#v=input("Plesse input ingredients: ").split()
#ny_bib={k:v}
#my_recipes.update(ny_bib)
#print(my_recipes)
