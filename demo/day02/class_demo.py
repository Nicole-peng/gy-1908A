class ClassDemo():
    def aaa(self):
        print("我是aaa")
    def bbb(self):
        print("我是bbb")
        self.aaa()

if __name__ == '__main__':
    c = ClassDemo()
    c.aaa()
    c.bbb()
