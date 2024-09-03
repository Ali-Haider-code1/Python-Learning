    
from flask import jsonify,request,Flask,abort

app = Flask(__name__)

users = [
    {'id':1, 'name':'Ali Haider'},
    {'id':2, 'name':'Saqib Abbasi'},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user/<int:id>',methods=['GET'])
def get_user(id):
    user = next((user for user in users if user['id']==id),None)
    if user:
        return user
    else:
        return print('User not found')

@app.route('/create_user',methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json:
        return print('Name required')
    new_user ={
        'id':users[-1]['id']+1 if users else 1,
        'name':request.json['name'],
    }
    users.append(new_user)
    return jsonify(new_user),201 #user created

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)
    if not request.json:
        abort(400)
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    return jsonify(user)


@app.route('/delete/<int:id>',methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)
    users.remove(user)
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)