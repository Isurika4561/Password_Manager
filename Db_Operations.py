import sqlite3


class DbOperations:

    def connect_to_db(self):
        conn = sqlite3.connect('password_record.db')
        return conn

    def create_table(self, table_name="password_info"):
        conn = self.connect_to_db()
        query = f'''
        CREATE TABLE IF NOT EXISTS {table_name}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            web_site TEXT NOT NULL,
            username VARCHAR(200),
            password VARCHAR(50)
        );
        '''
        with conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("Created the Table")

    def create_record(self, data, table_name="password_info"):
        website = data['website']
        username = data['username']
        password = data['password']
        conn = self.connect_to_db()
        query = f'''
        INSERT INTO {table_name}(web_site, username, password) VALUES(?,?,?)
        '''
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password))
            print("Saved the record")

    def show_record(self, table_name="password_info"):
        conn = self.connect_to_db()
        query = f'SELECT * FROM {table_name}'
        with conn:
            cursor = conn.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
        return records
    
    

    def update_record(self, data, record_id, table_name="password_info"):
        # Placeholder function to update a record in the database.
        ID = data['ID']
        website = data['website']
        username = data['username']
        password = data['password']
        conn = self.connect_to_db()
        query = f'''
        UPDATE {table_name} 
        SET web_site = ?, username = ?, password = ?, updated_date = CURRENT_TIMESTAMP
        WHERE ID = ?
        '''
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, (data['website'], data['username'], data['password'], ID))
            print(f"Record ID {ID} updated.")

    def delete_record(self, record_id, table_name="password_info"):
        # Placeholder function to delete a record from the database.
        conn = self.connect_to_db()
        query = f'DELETE FROM {table_name} WHERE ID = ?'
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, (record_id,))
            print(f"Record ID {record_id} deleted.")
