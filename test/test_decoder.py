# This file is placed in the Public Domain.
#
# pylint: disable=C0114,C0115,C0116,W0703,C0413
# pylama: ignore=E402


import unittest


from opv.objects import Object, loads, dumps


class A(Object):

    pass

class TestDecoder(unittest.TestCase):

    def test_compose(self):
        ooo = Object()
        ooo.o = A()
        ooo.o.a = "b"
        self.assertEqual(ooo.o.a, "b")

    def test_typed(self):
        ooo = Object()
        ooo.o = A()
        ooo.o.a = "b"
        res = dumps(ooo)
        print(res)
        oooo = loads(res)
        self.assertEqual(type(oooo.o), A)

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")

    def test_doctest(self):
        self.assertTrue(__doc__ is None)
