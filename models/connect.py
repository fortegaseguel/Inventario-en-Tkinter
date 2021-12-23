import sqlite3

class ConnectDB:
    def __init__(self):
        self.database = 'database/database.db'
        self.connect = sqlite3.connect(self.database)
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.commit()
        self.connect.close()