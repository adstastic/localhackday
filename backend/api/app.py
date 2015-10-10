from flask import Flask, jsonify
import _mysql as mdp
import read_db as db


app = Flask(__name__)

   

data_library = db.main()


@app.route('/building/<int:building_id>')
def index(building_id):
    return jsonify({building_id:data_library[building_id]})


if __name__ == '__main__':
    app.run(debug=True)
