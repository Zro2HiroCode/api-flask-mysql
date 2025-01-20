from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
host = 'localhost'
user = 'root'
password = ""
database = 'mydb'

@app.route('/')
def index():
    return "Welcome to the API"

@app.route('/api/recipes')
def read():
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM recipes")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult), 200)

@app.route('/api/recipes/<id>')
def readbyid(id):
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM recipes WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult), 200)

@app.route('/api/recipes', methods=['POST'])
def create():
    data = request.get_json()
    # required_keys = ['ingredients', 'quantity_pkg', 'unit_pkg', 'price_pkg', 'quantity_using', 'cost']
    # if not all(key in data for key in required_keys):
    #     return make_response(jsonify({'error': 'Missing required data'}), 400)
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO recipes (ingredients, quantity_pkg, unit_pkg, price_pkg, quantity_using, cost) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (data['ingredients'], data['quantity_pkg'], data['unit_pkg'], data['price_pkg'], data['quantity_using'], data['cost'])
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({'rowcount': mycursor.rowcount}), 200)

@app.route('/api/recipes/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE recipes SET ingredients = %s, quantity_pkg = %s, unit_pkg = %s, price_pkg = %s, quantity_using = %s, cost = %s WHERE id = %s"
    val = (data['ingredients'], data['quantity_pkg'], data['unit_pkg'], data['price_pkg'], data['quantity_using'], data['cost'], id)
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({'rowcount': mycursor.rowcount}), 200)

@app.route('/api/recipes/<int:id>', methods=['DELETE'])
def delete(id):
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
    mycursor = mydb.cursor(dictionary=True)
    sql = "DELETE FROM recipes WHERE id = %s"
    val = (id,) 
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({'rowcount': mycursor.rowcount}), 200)

if __name__ == '__main__':
    app.run(debug=True)
