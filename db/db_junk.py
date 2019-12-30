from db.stalls_db_manager import StallsDBManager
from db.reservations_db_manager import ReservationsDBManager

m = ReservationsDBManager()
m.clear()
m.commit()
m.close_connection()
