from reservations_db_manager import ReservationsDBManager
from datetime import datetime

m = ReservationsDBManager('reservations.db')

m.remove('0000', '123456789')
m.commit()
m.close_connection()
