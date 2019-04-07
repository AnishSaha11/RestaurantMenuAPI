import sqlite3
class db:
	def __init__(self, db_file):
		self.db_file = db_file
		self.init_tables()

	def getConnection(self):
		try:
			conn = sqlite3.connect(self.db_file)
			return conn
		except Error as e:
			print (e)
		return None

	def create_table(self, conn, create_sql):
		try:
			statement = conn.cursor()
			statement.execute(create_sql)
		except Error as e:
			print (e)

	def init_tables(self):
		create_menu_table = """CREATE TABLE IF NOT EXISTS menu (
									id integer PRIMARY KEY,
									name text NOT NULL);"""
		create_item_table = """CREATE TABLE IF NOT EXISTS item (
									id integer PRIMARY KEY,
									name text NOT NULL);"""

		conn = self.getConnection()
		if conn:
			self.create_table(conn, create_menu_table)
			self.create_table(conn, create_item_table)
			print ("Tables created")
		else:
			print ("Connection ERROR: Could not create tables")
		conn.close()

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
			print ("Connection ERROR: Could not create tables")
			return inserted_id

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
			print ("Connection ERROR: Could not create tables")
			return None

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
			print ("Connection ERROR: Could not create tables")
			return None

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
			print ("Connection ERROR: Could not create tables")
			return False


"""
#FOR FILE DEBUG
if __name__ == '__main__':
	store = db("db/database.db")
	data = {}
	data['name'] = "Lunch Menu"
	store.insert(data)
"""