from stalls_db_manager import StallsDBManager
from reservations_db_manager import ReservationsDBManager

m = StallsDBManager()
m.create_table()
m.commit()
m.close_connection()
