class a():
    def __init__(self):
        print(1)
        self.a0=0
    def pq(self):
        self.pp=12
class b(a):
    def __init__(self):
        pass
    def p(self):
        print(self.pp)


bb=b()
bb.pq()
bb.p()