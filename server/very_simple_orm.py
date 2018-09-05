'''
Very very simple orm for interaction with the database
'''

import sqlite3 as sql

from settings_log_server import DB_TABLE, DB_FIELDS, DB_NAME

class DBEntry:
    def __init__(self, dict_obj):
        # connect to the database
        # the database is created by the start scripts using the init_db.sql file
        self._dbcon = sql.connect(DB_NAME)
        for k in dict_obj:
            setattr(self, k, dict_obj[k])

    def write(self):
        cursor = self._dbcon.cursor()
        cursor.execute('INSERT INTO {} VALUES ('.format(DB_TABLE)+\
                       '?,?,?,?,?,?,?)',(self.time, self.hostname, self.pid, self.pname, \
                                         self.exc_type, self.filename, self.line))
        self._dbcon.commit()

    def read(self, attr, val):
        cursor = self._dbcon.cursor()
        cursor.execute('SELECT * FROM {} WHERE {} = ?'.format(DB_TABLE, attr), (val,))
        read_vals = cursor.fetchall()[0]
        for i, v in enumerate(read_vals):
            setattr(self, DB_FIELDS[i], v)

