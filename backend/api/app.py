from flask import Flask, jsonify
import _mysql as mdp
import read_db as db


app = Flask(__name__)

  

@app.route('/room/<int:building_id>')
def index(room_id):
    return jsonify(by_id(room_id))

@app.route('/search/<query>')
def search(query):
    return jsonify(db.search_name(query))

if __name__ == '__main__':
    app.run()
