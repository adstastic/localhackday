from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/building/<int:building_id>')
def index(building_id):
    return "Hello, World! " + str(building_id)


if __name__ == '__main__':
    app.run(debug=True)
