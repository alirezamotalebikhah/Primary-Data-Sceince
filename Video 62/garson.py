class garson:
    all_garson=[]
    def __init__(self , name , is_busy , tables):
        self.username = name
        self.is_busy = is_busy
        self.tables = tables
        garson.all_garson.append(self)
    @classmethod
    def find_free(cls):
        return[g for g in cls.all_garson if not g.is_busy]
    @classmethod
    def find_busy(cls):
        return [g for g in cls.all_garson if g.is_busy]
    def get_order(self , table , order):
        out = f"Table {table} has ordered {order}, served by {self.username}"
        self.is_busy=True
        self.tables.append(table)
        return out
    def check(self, table , cost):
        out = f"table {table} is {cost}"
        return out
    
gar1=garson("maryam" , True , [3,5,9])
gar2=garson("javad" , False , [])
free=garson.find_free()
for g in free:
    out = g.get_order(4 , 'coffee')
    print(out)
print(gar2.username)
print(gar2.tables)
print(gar2.is_busy)

print(gar1.check(3,200))


