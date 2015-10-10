from flask import Flask, jsonify, request, abort
from flask.ext.httpauth import HTTPBasicAuth

import _mysql as mdp
import read_db as db
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'admin':
        with open("config.json", "rb") as fp:
            config = json.loads(fp.read())
        return config["api_pass"]
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/api/room/<int:room_id>')
def index(room_id):
    return jsonify(db.by_id(room_id))

@app.route('/api/search/<query>')
def search(query):
    return jsonify(db.search_name(query))

@app.route('/api/room', methods=['POST'])
@auth.login_required
def create_room():
  #  if not request.json: # or not 'name' in request.json:
  #      abort(400)
    print 'made it before vars'
    if request.data:
        print "HAS DATA"
    else:
        print "NO DATA"
    name = request.json['name']
    size = request.json['size']
    room_type = request.json['type']
    htmlref = request.json['htmlref']
    print 'made it before new'
    new = db.add_new(name, size, room_type, htmlref)
    print 'made it after new'
    return jsonify(new), 201
    
    
    
    


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
