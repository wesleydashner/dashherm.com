from db.reservations_db_manager import ReservationsDBManager
from db.stalls_db_manager import StallsDBManager


class GeneralManager:

    @staticmethod
    def make_reservation(lot_id, user_id, time):
        if GeneralManager.__can_reserve(lot_id):
            rm = ReservationsDBManager()
            rm.insert(lot_id, user_id, time)
            rm.commit()
            rm.close_connection()
            return True
        return False

    @staticmethod
    def __can_reserve(lot_id):
        rm = ReservationsDBManager()
        sm = StallsDBManager()
        available_count = sm.get_available_count(lot_id)
        print('available:')
        print(available_count)
        reservation_count = rm.get_reservation_count(lot_id)
        print('reserved:')
        print(reservation_count)
        rm.close_connection()
        sm.close_connection()
        return available_count - reservation_count > 0

    @staticmethod
    def get_available_stalls_count(lot_id):
        return -1
