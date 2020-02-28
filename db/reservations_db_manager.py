import sqlite3
from db.db_path_manager import DBPathManager


class ReservationsDBManager:

    def __init__(self):
        self.db_file = DBPathManager.get_reservations_db_path()
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

    # only necessary when a table hasn't yet been created
    # status can be: created, parking, parked
    def create_table(self):
        self.cursor.execute('''CREATE TABLE reservations (
                            lot_id text,
                            user_id text,
                            time text,
                            status text
                            )''')

    # call this method when you're done using the manager
    def close_connection(self):
        self.connection.close()

    # call this method after making any changes to the database
    # (create_table, insert, remove, clear)
    def commit(self):
        self.connection.commit()

    def insert(self, lot_id, user_id, time):
        self.cursor.execute('INSERT INTO reservations VALUES (:lot_id, :user_id, :time, :status)',
                            {'lot_id': lot_id, 'user_id': user_id, 'time': time, 'status': 'created'})

    # returns True if lot_id and user_id combination are found
    def update_status(self, lot_id, user_id, status):
        self.cursor.execute('UPDATE reservations SET status=:status WHERE lot_id=:lot_id AND user_id=:user_id',
                            {'status': status, 'lot_id': lot_id, 'user_id': user_id})
        return True if self.cursor.rowcount == 1 else False

    def remove(self, lot_id, user_id):
        self.cursor.execute('DELETE FROM reservations WHERE lot_id=:lot_id AND user_id=:user_id',
                            {'lot_id': lot_id, 'user_id': user_id})

    def clear(self):
        self.cursor.execute('DELETE FROM reservations')

    def get_reservation_count(self, lot_id):
        self.cursor.execute('SELECT * FROM reservations WHERE lot_id=:lot_id AND (status=:created OR status=:parking)', {'lot_id': lot_id, 'created': 'created', 'parking': 'parking'})
        return len(self.cursor.fetchall())
