from stalls_db_manager import StallsDBManager

m = StallsDBManager()
# m.update_availability('0000', 'A1', True)
m.commit()
m.close_connection()
