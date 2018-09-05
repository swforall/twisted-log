from twisted.trial import unittest
from twisted.test import proto_helpers

from slave import SlaveFactory
from settings_daemons import EXCEPTIONS

class TestSlavesExceptions(unittest.TestCase):
    def setUp(self):
        factory = SlaveFactory()
        self.proto = factory.buildProtocol(('127.0.0.1', 0))
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)

    def _test(self, inp, expected):
        # print(self.tr.value())
        self.proto.dataReceived(bytes('%s'%(inp,), 'utf-8'))
        val = self.tr.value()
        # print(val)
        val = val.decode().split('?')
        # print(val)
        self.assertEqual(val[-1], expected)

    def _send(self, inp):
        self.proto.dataReceived(bytes('%s' % (inp,), 'utf-8'))

    def test_Logger_no_exception(self):
        inp = 'aaa'
        self._test(inp, "You sent: {}, No exception to raise".format(inp))

    def test_Logger_exc_1(self):
        inp = '1'
        self.assertRaises(EXCEPTIONS[int(inp)], self._send, inp)

    def test_Logger_exc_2(self):
        inp = '2'
        self.assertRaises(EXCEPTIONS[int(inp)], self._send, inp)

    def test_Logger_exc_3(self):
        inp = '3'
        self.assertRaises(EXCEPTIONS[int(inp)], self._send, inp)

    def test_Logger_exc_4(self):
        inp = '4'
        self.assertRaises(EXCEPTIONS[int(inp)], self._send, inp)

    def test_Logger_exc_5(self):
        inp = '5'
        self.assertRaises(EXCEPTIONS[int(inp)], self._send, inp)