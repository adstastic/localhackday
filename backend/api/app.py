from flask import Flask, jsonify
import _mysql as mdp
import read_db as db


app = Flask(__name__)

  

@app.route('/building/<int:building_id>')
def index(building_id):
    return jsonify(by_id(building_id))

@app.route('/search/<query>')
def search(query):
    return jsonify(db.search_name(query))

if __name__ == '__main__':
    app.run(debug=True)
