
import MySQLdb as mdb
import json

def search_name(query):
	
	cur = connect().cursor()
	cur.execute('SELECT * FROM rooms WHERE name LIKE "%{}%"'.format(query))
	
	response = cur.fetchall()

	data = {}
	for row in response:
		data[row[0]] = {"name":row[1], "size":row[2], "type":row[3]}

def by_id(id_num):
	cur = connect().cursor()
	cur.execute('SELECT * FROM rooms WHERE id={}'.format(id_num))
	response = cur.fetchall()
	return {row[0]:[row[1], row[2], row[3], row[4]] for row in response}
	
def add_new(name, size, room_type, htmlref):
	
	con = connect()
	cur = con.cursor()
	string = 'INSERT INTO rooms (id, name, size, type, htmlref) VALUES (NULL, "{}", {}, "{}", "{}");'.format(name, size, room_type, htmlref)
	print string
	cur.execute(string)
	cur.execute('SELECT * FROM rooms WHERE name="{}"'.format(name))
	con.commit()
	confirm = cur.fetchall()
	confirm_data = {confirm[0][0]:[i for i in confirm[0]]}
	return confirm_data



def connect():
	
	with open("config.json", "rb") as fp:
		config = json.loads(fp.read())
	
	con = mdb.connect(config["ip"], config["username"], config["password"], config["database_name"]);
	
	return con
