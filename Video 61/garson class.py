class garson:
    all_garson=[]
    def __init__(self , name , is_busy , tables):
        self.username = name
        self.is_busy = is_busy
        self.tables = tables
        garson.all_garson.append(self)
    @classmethod
    def find_free(cls):
        return[g for g in cls.all_garson if g.is_busy]
    @classmethod
    def find_busy(cls):
        return [g for g in cls.all_garson if not g.is_busy]
gar1=garson("maryam" , True , [3,5,9])
print(f"name of firsat garson is {gar1.username} and service tables is :{gar1.tables}")
gar2=garson("javad" , False , [])
free = garson.find_free()
busy = garson.find_busy()
print("free garsons : \n")
for g in free:
    print(f"name is {g.username} and tables is : {g.tables}\n")
print("busy garsons : \n")
for g in busy:
    print(f"name is {g.username} and tables is : {g.tables}\n")
gar2.new = True
if gar2.new == True:
    print(gar2.username)