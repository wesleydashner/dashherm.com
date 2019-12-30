from db.reservations_db_manager import ReservationsDBManager
from db.stalls_db_manager import StallsDBManager
from datetime import datetime


class GeneralManager:

    @staticmethod
    def make_reservation(lot_id, user_id):
        time = datetime.utcnow()
        if GeneralManager.__can_reserve(lot_id):
            rm = ReservationsDBManager()
            rm.insert(lot_id, user_id, time)
            rm.commit()
            rm.close_connection()
            return True
        return False

    @staticmethod
    def __can_reserve(lot_id):
        return GeneralManager.__get_available_count_after_reservations(lot_id) > 0

    @staticmethod
    def __get_available_count_after_reservations(lot_id):
        rm = ReservationsDBManager()
        sm = StallsDBManager()
        available_count = sm.get_available_count(lot_id)
        reservation_count = rm.get_reservation_count(lot_id)
        rm.close_connection()
        sm.close_connection()
        return available_count - reservation_count

    @staticmethod
    def get_available_stalls_count(lot_id):
        return GeneralManager.__get_available_count_after_reservations(lot_id)
