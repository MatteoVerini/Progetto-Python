from flask import Flask, request, render_template, redirect
import os, json

template_dir = os.path.abspath("./templates")
app = Flask(__name__, template_folder=template_dir)

class MenuItem:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def GetID(self):
        return self.id
    
    def GetName(self):
        return self.name

    def GetDescription(self):
        return self.description
    
    def GetPrice(self):
        return self.price
    
menu_file = "db/menu.json"

def load_menu():
    with open(menu_file, 'r') as file:
        return json.load(file)

def save_menu(menu_items):
    with open(menu_file, 'w') as file:
        json.dump(menu_items, file, indent=4)

@app.route('/',methods=["GET"])
def index():
    menu_items=load_menu()
    menu_list=[MenuItem(m["id"],m["name"],m["description"], m["price"])for m in menu_items]
    return render_template("index.html",menu=menu_list)

@app.route('/add',methods=["POST"])
def add_menu_item():
    menu_items=load_menu()
    new_item={
        "id": len(menu_items)+1,
        "name":request.form["name"],
        "description":request.form
        
    }