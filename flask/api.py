# put and delete -http verbs
# working with api's --json
from flask import Flask,jsonify,request
app=Flask(__name__)

#initial data in my todo list

items = [
    {'id': 1, 'name': 'item one', 'description': 'This is item one.'},
    {'id': 2, 'name': 'item two', 'description': 'This is item two.'}
]
@app.route('/')
def home():
    return "welcome to sample to dolist app"

# get:retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

#get:retrieve a specific type by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item ["id"]==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'}),404
    return jsonify(item)

#post method:if request is in json format and contains the "name "field.
#if not we return the error
# post:create a new task  ->basically an API
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Name is required'}), 400
    new_id = items[-1]['id'] + 1 if items else 1
    new_item = {
        'id': new_id,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201

#put:update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

#DELETE:delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item["id"]!=item_id]
    return jsonify({"result":"item deleted "})

if __name__=='__main__':
    app.run(debug=True)