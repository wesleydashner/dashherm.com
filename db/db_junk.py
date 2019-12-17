import sqlite3
from db_manager import DBManager

m = DBManager('stalls.db')
# m.insert('0000', 'A1')
# m.insert('0000', 'A2')
# m.insert('0000', 'A3')
# m.remove('0000', 'A3')
m.update_availability('0000', 'A1', False)
print(m.get_available_count('0000'))
m.commit()
m.close_connection()
