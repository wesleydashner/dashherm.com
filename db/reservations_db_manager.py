import sqlite3
from db_path_manager import DBPathManager


class ReservationsDBManager:

    def __init__(self):
        self.db_file = DBPathManager.get_reservations_db_path()
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

    # only necessary when a table hasn't yet been created
    def create_table(self):
        self.cursor.execute('''CREATE TABLE reservations (
                            lot_id text,
                            user_id text,
                            time text
                            )''')

    # call this method when you're done using the manager
    def close_connection(self):
        self.connection.close()

    # call this method after making any changes to the database
    # (create_table, insert, remove, clear)
    def commit(self):
        self.connection.commit()

    def insert(self, lot_id, user_id, time):
        self.cursor.execute('INSERT INTO reservations VALUES (:lot_id, :user_id, :time)',
                            {'lot_id': lot_id, 'user_id': user_id, 'time': time})

    def remove(self, lot_id, user_id):
        self.cursor.execute('DELETE FROM reservations WHERE lot_id=:lot_id AND user_id=:user_id',
                            {'lot_id': lot_id, 'user_id': user_id})

    def clear(self):
        self.cursor.execute('DELETE FROM reservations')

    def get_reservation_count(self, lot_id):
        self.cursor.execute('SELECT * FROM reservations WHERE lot_id=:lot_id', {'lot_id': lot_id})
        return len(self.cursor.fetchall())
