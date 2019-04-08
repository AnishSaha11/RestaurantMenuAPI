import sqlite3
class db:
	def __init__(self, db_file):
		self.db_file = db_file
		self.init_tables()

	# RETURN CONNECTION OBJECT
	def getConnection(self):
		try:
			conn = sqlite3.connect(self.db_file)
			return conn
		except Error as e:
			print (e)
		return None

	# CREATE TABLES IF THEY DONT EXIST
	def init_tables(self):
		create_sqls = open("create_tables.sql").read()
		conn = self.getConnection()
		if conn:
			with conn:
				try:
					statement = conn.cursor()
					statement.executescript(create_sqls)
				except Error as e:
					print (e)
		else:
			print ("Connection ERROR: Could not create tables")
		conn.close()

	# INSERT MENU SECTION
	def insert_menu(self, data):
		insert_sql = "INSERT INTO menu(name) VALUES ('"+ data['name']+"')"
		inserted_id = -1
		conn = self.getConnection()
		if conn:
			with conn:
				statement = conn.cursor()
				statement.execute(insert_sql)
				inserted_id = statement.lastrowid
				return inserted_id
		else:
			print ("Connection ERROR: Could not connect to database")
			return inserted_id

	# RETURN ALL MENU SECTIONS
	def get_menu(self):
		fetch_sql = "SELECT * FROM menu"
		conn = self.getConnection()
		if conn:
			with conn:
				statement = conn.cursor()
				statement.execute(fetch_sql)
				fetched_data = statement.fetchall()
				return fetched_data
		else:
			print ("Connection ERROR: Could not connect to database")
			return None

	# RETURN MENU SECTIONS WITH GIVEN ID
	def get_menu_by_id(self, menuid):
		fetch_sql = "SELECT * FROM menu WHERE id ='"+ menuid +"'"
		conn = self.getConnection()
		if conn:
			with conn:
				statement = conn.cursor()
				statement.execute(fetch_sql)
				fetched_data = statement.fetchall()
				return fetched_data
		else:
			print ("Connection ERROR: Could not connect to database")
			return None

	# DELETE MENU SECTION OF GIVEN ID
	def delete_menu_by_id(self, menuid):
		del_sql = "DELETE from menu WHERE id ='"+ menuid +"'"
		count_sql = "SELECT COUNT (*) FROM menu"
		conn = self.getConnection()
		if conn:
			with conn:
				statement = conn.cursor()
				statement.execute(count_sql)
				initial_row_count = statement.fetchone()[0]
				statement.execute(del_sql)
				statement.execute(count_sql)
				final_row_count = statement.fetchone()[0]
				if final_row_count - initial_row_count == 0:
					return False
				else:
					return True
		else:
			print ("Connection ERROR: Could not connect to database")
			return False

	# UPDATE MENU SECTION WITH GIVEN ID
	def update_menu_by_id(self, menuid, data):
		update_sql = "UPDATE menu SET name = '"+ data['name']+"' WHERE id='"+menuid+"'"
		conn = self.getConnection()
		rows_affected = -1
		if conn:
			with conn:
				statement = conn.cursor()
				statement.execute(update_sql)
				rows_affected = statement.rowcount
				return rows_affected
		else:
			print ("Connection ERROR: Could not connect to database")
			return rows_affected
"""
#FOR FILE DEBUG
if __name__ == '__main__':
	store = db("db/database.db")
	data = {}
	data['name'] = "Lunch Menu"
	store.insert(data)
"""