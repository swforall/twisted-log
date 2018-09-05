import sqlite3 as sql

from twisted.trial import unittest

import very_simple_orm
from settings_log_server import DB_FIELDS, DB_NAME


lo = [{'exc_type': 'AssertionError',
  'filename': '~/slave.py',
  'hostname': 'WorkStation-T3500',
  'line': 25,
  'time': 1535918106.4531238,
  'pid': 2334,
  'pname': 'test_name0'},
 {'exc_type': 'AssertionError',
  'filename': '~/slave.py',
  'hostname': 'WorkStation-T3500',
  'line': 25,
  'time': 1535918106.4533234,
  'pid': 845,
  'pname': 'test_name1'
  }]

class TestDB(unittest.TestCase):
    def setUp(self):
        with open('../init_db.sql') as f:
            sql_file = f.read()  # watch out for built-in `str`
        self.conn = sql.connect(DB_NAME)
        self.cur = self.conn.cursor()
        self.cur.executescript(sql_file)
        self.conn.commit()
        self.conn.close()

    def test_1(self):
        dbobj = very_simple_orm.DBEntry(lo[0])
        dbobj.write()
        dbobj1 = very_simple_orm.DBEntry({})
        dbobj1.read('pid', 2334)
        for f in DB_FIELDS:
            self.assertEqual(getattr(dbobj, f), getattr(dbobj1, f))

    def test_2(self):
        dbobj = very_simple_orm.DBEntry(lo[1])
        dbobj.write()
        dbobj1 = very_simple_orm.DBEntry({})
        dbobj1.read('pid', 845)
        for f in DB_FIELDS:
            self.assertEqual(getattr(dbobj, f), getattr(dbobj1, f))
