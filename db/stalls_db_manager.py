import sqlite3
from db.db_path_manager import DBPathManager


class StallsDBManager:

    def __init__(self):
        self.db_file = DBPathManager.get_stalls_db_path()
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

    # only necessary when a table hasn't yet been created
    def create_table(self):
        self.cursor.execute('''CREATE TABLE stalls (
                            lot_id text,
                            stall_id text,
                            is_available integer
                            )''')

    # call this method when you're done using the manager
    def close_connection(self):
        self.connection.close()

    # call this method after making any changes to the database
    # (create_table, insert, remove, clear, update_availability)
    def commit(self):
        self.connection.commit()

    def insert(self, lot_id, stall_id, is_available):
        is_available = 1 if is_available else 0
        self.cursor.execute('INSERT INTO stalls VALUES (:lot_id, :stall_id, :is_available)',
                            {'lot_id': lot_id, 'stall_id': stall_id, 'is_available': is_available})

    def remove(self, lot_id, stall_id):
        self.cursor.execute('DELETE FROM stalls WHERE lot_id=:lot_id AND stall_id=:stall_id',
                            {'lot_id': lot_id, 'stall_id': stall_id})

    def clear(self):
        self.cursor.execute('DELETE FROM stalls')

    # returns true if lot_id and stall_id combination are found
    def update_availability(self, lot_id, stall_id, is_available):
        is_available = 1 if is_available else 0
        self.cursor.execute('UPDATE stalls SET is_available=:is_available WHERE lot_id=:lot_id AND stall_id=:stall_id',
                            {'lot_id': lot_id, 'stall_id': stall_id, 'is_available': is_available})
        return True if self.cursor.rowcount == 1 else False

    def get_available_count(self, lot_id):
        self.cursor.execute('SELECT * FROM stalls WHERE lot_id=:lot_id AND is_available=1', {'lot_id': lot_id})
        return len(self.cursor.fetchall())
