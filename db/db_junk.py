from db.stalls_db_manager import StallsDBManager
from db.reservations_db_manager import ReservationsDBManager
from datetime import datetime

m = ReservationsDBManager()
m.commit()
m.close_connection()
