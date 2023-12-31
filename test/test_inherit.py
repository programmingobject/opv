# This file is placed in the Public Domain.
#
# pylint: disable=C0114,C0115,C0116,W0703,C0413,C0103,R0903,C0103
# pylama: ignore=E402,E302,E265


import unittest


from opv.objects import Object


class A(Object):

    pass

class B(Object):

    pass


class C(A, B):

    bla = "mekker"


class D:

    pass


class E(A, D):

    pass


class F(C, D):

    pass


class H(dict):

    pass


#class I(object):

#    pass


#class J(A, I):

#    pass


#class K(J, H):

#    pass


class TestInherit(unittest.TestCase):

    def testinherit1(self):
        c = C()
        self.assertEqual(type(c), C)

    def testinherit2(self):
        e = E()
        self.assertEqual(type(e), E)

    def testinherit3(self):
        f = F()
        self.assertEqual(type(f), F)

    def testinherit4(self):
        f = F()
        self.assertEqual(f.bla, "mekker")

    def testinherit5(self):
        h = H()
        self.assertEqual(type(h), H)
