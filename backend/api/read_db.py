
import MySQLdb as mdb
import json

def search_name(query):
	
	cur = connect().cursor()
	cur.execute('SELECT * FROM rooms WHERE name LIKE "%{}%"'.format(query))
	
	response = cur.fetchall()

	return [row for row in response]	

#		data[row[0]] = {"name":row[1], "size":row[2], "type":row[3]}
		# if we want to return a dictionary of mulitple results instead of a list	


def by_id(id_num):
	
	cur = connect().cursor()
	cur.execute('SELECT * FROM rooms WHERE id=%s' %id_num)
	
	response = cur.fetchall()
	return [row for row in response]
	
	
def connect():
	
	with open("config.json", "rb") as fp:
		config = json.loads(fp.read())
	
	con = mdb.connect(config["ip"], config["username"], config["password"], config["database_name"]);
	
	return con
