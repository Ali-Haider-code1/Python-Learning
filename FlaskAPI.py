    
from flask import jsonify,request,Flask

app = Flask(__name__)

users = [
    {'id':1, 'name':'Ali Haider'},
    {'id':2, 'name':'Saqib Abbasi'},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/getById',methods=['GET'])
def get_user(id):
    user = next((user for user in users if user['id']==id),None)
    if user:
        return user
    else:
        return print('User not found')

@app.route('/create_user',methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)