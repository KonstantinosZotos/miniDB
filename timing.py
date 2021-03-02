from database import Database
import time
import timeit


db = Database('smdb', load=False)

#db.table_from_csv('addresses.csv')
db.create_table('classroom', ['building', 'room_number', 'capacity'], [str,str,int])
db.insert('classroom', ['Packard', '101', '500'])
db.insert('classroom', ['Bell', '102', '450'])
db.table_to_csv('classroom')
db.drop_table('classroom')
