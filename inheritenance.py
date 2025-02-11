class Dad:
    def football(self):
        print("dad likes watching football")
class Mum :
    def cooking(self):
        print("mum likes cooking")
class Boy(Dad):
    def Boyage(self):
        print("the boy is 15 years old")
class Girl(Mum) :
    def Girlage(self):
        print("the girls is 12 years old")
my_boy=Boy
my_boy.football()
my_boy.Boyage()
my_girl=Girl
my_girl.cooking()
my_girl.Girlage()