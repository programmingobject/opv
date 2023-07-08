# This file is placed in the Public Domain.


"clean namespace"


import sys


from opv import Object, files, find, parse, prt, write


class Handler:

    """commands binded to a function"""

    cmds = {}

    @staticmethod
    def add(func):
        """add a function"""
        Handler.cmds[func.__name__] = func

    @staticmethod
    def handle(com):
        # pylint: disable=W0718
        """handle an command"""
        func = Handler.cmds.get(com.cmd, None)
        if func:
            try:
                func(com)
            except Exception as ex:
                print(ex.with_traceback(ex.__traceback__))


class Log(Object):

    "log objects"

    def __init__(self):
        super().__init__()
        self.txt = ""

    def gettxt(self):
        """get log text"""
        return self.txt

    def settxt(self, txt):
        """set log txt"""
        self.txt = txt


def cmd(event):
    """list commands"""
    if event:
        print(",".join(Handler.cmds))


def fnd(event):
    """locate objects"""
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in files()])
        if res:
            print(",".join(res))
        return
    otype = event.args[0]
    nmr = 0
    for obj in find(otype):
        print(f"{nmr} {prt(obj)}")
        nmr += 1


def log(event):
    """log text"""
    if not event.rest:
        nmr = 0
        for obj in find('log'):
            print(f"{nmr} {prt(obj)}")
            nmr += 1
        return
    obj = Log()
    obj.txt = event.rest
    write(obj)
    print('ok')


def main():
    """runtime"""
    hdl = Handler()
    hdl.add(cmd)
    hdl.add(fnd)
    hdl.add(log)
    com = Object()
    parse(com, " ".join(sys.argv[1:]))
    hdl.handle(com)


if __name__ == "__main__":
    main()