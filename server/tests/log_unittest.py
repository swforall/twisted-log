import json
import sqlite3 as sql

from twisted.trial import unittest
from twisted.test import proto_helpers

from log_server import LoggerFactory
from very_simple_orm import DBEntry
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

class TestLogServer(unittest.TestCase):
    def setUp(self):
        with open('../init_db.sql') as f:
            sql_file = f.read()  # watch out for built-in `str`
        self.conn = sql.connect(DB_NAME)
        self.cur = self.conn.cursor()
        self.cur.executescript(sql_file)
        self.conn.commit()
        self.conn.close()
        factory = LoggerFactory()
        self.proto = factory.buildProtocol(('127.0.0.1', 0))
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)

    def _test(self, inp):
        # print(self.tr.value())
        inpjson = json.dumps(inp)
        self._send(inpjson)
        dbobj = DBEntry({})
        dbobj.read('pid', inp['pid'])
        for f in DB_FIELDS:
            self.assertEqual(getattr(dbobj, f), inp[f])

    def _send(self, inp):
        self.proto.dataReceived(bytes('%s' % (inp,), 'utf-8'))

    def test_log_0(self):
        self._test(lo[0])

    def test_log_1(self):
        self._test(lo[1])