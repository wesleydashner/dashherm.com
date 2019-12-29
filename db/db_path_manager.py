import os.path
from db.db_file_names import stalls_db, reservations_db


class DBPathManager:

    @staticmethod
    def get_stalls_db_path():
        # https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, stalls_db)

    @staticmethod
    def get_reservations_db_path():
        # https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, reservations_db)
