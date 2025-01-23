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

#Adding an element
@app.route('/add',methods=["POST"])
def add_menu_item():
    menu_items=load_menu()
    new_item={
        "id": len(menu_items)+1,
        "name":request.form["name"],
        "description":request.form["description"],
        "price":float(request.form["price"])
        
    }
    menu_items.append(new_item)
    save_menu(menu_items)
    return redirect('/')

#Editing an element
@app.route('/edit/<int:item_id>', methods=["GET"])
def edit_menu_page(item_id):
    menu_items = load_menu()
    item_to_edit = next((item for item in menu_items if item["id"] == item_id), None)
    if not item_to_edit:
        return "Element Not Found", 404
    return render_template("edit_menu.html", item=item_to_edit)

#Visualizing the edit page
@app.route('/update/<int:item_id>', methods=["POST"])
def update_menu_item(item_id):
    menu_items = load_menu()
    for item in menu_items:
         if item["id"] == item_id:
            item["name"] = request.form["name"]
            item["description"] = request.form["description"]
            item["price"] = float(request.form["price"])
            break
    save_menu(menu_items)
    return redirect('/')

#Deleting an item
@app.route('/delete/<int:item_id>', methods=["POST"])
def delete_menu_item(item_id):
    menu_items = load_menu()
    menu_items = [item for item in menu_items if item["id"] != item_id]
    save_menu(menu_items)
    return redirect('/')

#Flask debug
if __name__ == '__main__':
    app.run(debug=True)