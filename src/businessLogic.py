from dbHandler import db
import collections
import json
class business:
	def __init__(self):
		self.read_config()
		self.dataStore = db("db/"+self.config['DB_NAME:'])

	def read_config(self):
		self.config = {}
		valid_config_params = ['DB_NAME:','PORT:']
		file = open("config/config.txt","r")
		if not file:
			print ("Error reading config file")
			return
		else:
			count = 0
			line = file.readline()
			while line:
				tokens = line.split()
				if tokens[0] in valid_config_params:
					self.config[tokens[0]] = tokens[1]
					count+=1
				line = file.readline()
			print ("{} configurations read".format(count))

	def get_port(self):
		return int(self.config['PORT:'])

	def get_menu(self):
		data = self.dataStore.get_menu()
		package = collections.defaultdict(list)
		for d in data:
			menuObject = {}
			menuObject["id"] = d[0]
			menuObject["name"] = d[1]
			package["MenuSection"].append(menuObject)
		return json.dumps(package, indent=4)

	def get_menu_by_id(self, menuid):
		data = self.dataStore.get_menu_by_id(menuid)
		if len(data) == 0:
			return None
		package = collections.defaultdict(list)
		for d in data:
			menuObject = {}
			menuObject["id"] = d[0]
			menuObject["name"] = d[1]
			package["MenuSection"].append(menuObject)
		return json.dumps(package, indent=4)

	def delete_menu_by_id(self, menuid):
		success = self.dataStore.delete_menu_by_id(menuid)
		if success:
			return json.dumps({'success':True}, indent=4)
		else:
			return None
	def add_menu_section(self, content):
		if len(content) == 1 and "name" in content.keys():
			res = self.dataStore.insert_menu(content)
			if res > 0:
				package = collections.defaultdict(list)
				menuObject = {}
				menuObject["id"] = res
				menuObject["name"] = content['name']
				package["success"] = True
				package["MenuSection"].append(menuObject)
				
				return json.dumps(package, indent=4), 200
			else:
				return None, 400
		else:
			print ("JSON format error")
			return None, 400
"""
# FOR FILE DEBUG
if __name__ == '__main__':
	ob = business()
"""