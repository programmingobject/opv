# This file is placed in the Public Domain.
#
# pylint: disable=C0114,C0115,C0116,W0703,E1101,C0413,C2801,R0904,W0401,W0614
# pylama: ignore=E402


import sys
import unittest


sys.path.insert(0, "..")


from opv.objects import *



VALIDJSON = '{"test": "bla"}'
VALIDJSON2 = '{"test": "bla", "__kind__": "opv.objects.Object"}'

attrs2 = (
          '__class__',
          '__delattr__',
          '__dict__',
          '__dir__',
          '__doc__',
          '__eq__',
          '__format__',
          '__ge__',
          '__getattribute__',
          '__gt__',
          '__hash__',
          '__init__',
          '__init_subclass__',
          '__iter__',
          '__le__',
          '__len__',
          '__lt__',
          '__module__',
          '__ne__',
          '__new__',
          '__oid__',
          '__reduce__',
          '__reduce_ex__',
          '__repr__',
          '__setattr__',
          '__sizeof__',
          '__slots__',
          '__str__',
          '__subclasshook__'
         )


class TestObject(unittest.TestCase):

    def test_constructor(self):
        obj = Object()
        self.assertTrue(type(obj), Object)

    def test_class(self):
        obj = Object()
        clz = obj.__class__()
        self.assertTrue("Object" in str(type(clz)))

    def test_contains(self):
        obj = Object()
        obj.key = "value"
        self.assertTrue("key" in obj)

    def test_delattr(self):
        obj = Object()
        obj.key = "value"
        del obj.key
        self.assertTrue("key" not in obj)

    def test_dict(self):
        obj = Object()
        self.assertEqual(obj.__dict__, {})

    def test_doc(self):
        obj = Object()
        self.assertEqual(obj.__doc__, "doesn't have any methods, just dunders")

    def test_format(self):
        obj = Object()
        self.assertEqual(obj.__format__(""), '{"__kind__": "opv.objects.Object"}')

    def test_getattribute(self):
        obj = Object()
        obj.key = "value"
        self.assertEqual(obj.__getattribute__("key"), "value")

    def test_hash(self):
        obj = Object()
        hsj = hash(obj)
        self.assertTrue(isinstance(hsj, int))

    def test_init(self):
        obj = Object()
        self.assertTrue(type(Object.__init__(obj)), Object)

    def test_iter(self):
        obj = Object()
        obj.key = "value"
        self.assertTrue(
            list(obj.__iter__()),
            [
                "key",
            ],
        )

    def test_len(self):
        obj = Object()
        self.assertEqual(len(obj), 0)

    def test_module(self):
        self.assertEqual(Object().__module__, "opv.objects")

    def test_kind(self):
        self.assertEqual(kind(Object()), "opv.objects.Object")

    def test_repr(self):
        self.assertTrue(update(Object(),
                               {"key": "value"}).__repr__(), {"key": "value"})

    def test_setattr(self):
        obj = Object()
        obj.__setattr__("key", "value")
        self.assertTrue(obj.key, "value")

    def test_str(self):
        obj = Object()
        self.assertEqual(str(obj), '{"__kind__": "opv.objects.Object"}')

    def test_printable(self):
        obj = Object()
        self.assertEqual(prt(obj), "")

    def test_getattr(self):
        obj = Object()
        obj.key = "value"
        self.assertEqual(getattr(obj, "key"), "value")

    def test_keys(self):
        obj = Object()
        obj.key = "value"
        self.assertEqual(
            list(keys(obj)),
            [
                "key",
            ],
        )

    def test_items(self):
        obj = Object()
        obj.key = "value"
        self.assertEqual(
            list(items(obj)),
            [
                ("key", "value"),
            ],
        )

    def test_register(self):
        obj = Object()
        setattr(obj, "key", "value")
        self.assertEqual(obj.key, "value")

    def test_update(self):
        obj = Object()
        obj.key = "value"
        oobj = Object()
        update(oobj, obj)
        self.assertTrue(oobj.key, "value")

    def test_values(self):
        obj = Object()
        obj.key = "value"
        self.assertEqual(
            list(values(obj)),
            [
                "value",
            ],
        )

    def test_dumps(self):
        ooo = Object()
        ooo.o = Object()
        ooo.o.a = "b"
        res = dumps(ooo)
        self.assertEqual(res, '{"o": {"a": "b", "__kind__": "opv.objects.Object"}, "__kind__": "opv.objects.Object"}')

    def test_loads(self):
        ooo = Object()
        ooo.o = Object()
        ooo.o.a = "b"
        res = dumps(ooo)
        ooo = loads(res)
        self.assertEqual(ooo.o.a, "b")
