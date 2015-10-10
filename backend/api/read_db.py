
import MySQLdb as mdb
import json

def main():
	
	with open("config.json", "rb") as fp:
		config = json.loads(fp.read())
	
	
	con = mdb.connect(config["ip"], config["username"], config["password"], config["database_name"]);
	
	cur = con.cursor()
	cur.execute("SELECT * FROM rooms")
	
	response = cur.fetchall()
	
	data = {}
	
	for row in response:
		data[row[0]] = {"name":row[1], "size":row[2], "type":row[3]}
	
	return data