class Person:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("안녕 내 이름은",self.name)

    def walk(self):
        print("나는 걷는 중")

class Worker(Person):
    def __init__(self,name,mental):
        Person.__init__(self,name)
        self.company=company
        self.mental=50
    def hello(self):
        print("안녕 내 이름은"+self.name+"이고 내가 다니는 회사는"+self.company)
    def work(self):
        if self.mental>=0:
            print("나는 일하는 중 내 멘탈지수 : "+str(self.mental))
        else:
            print("더는 일 못 해")
        self.mental-=10


worker=Worker("임영빈","카카오")
worker.hello()
worker.walk()
worker.work()