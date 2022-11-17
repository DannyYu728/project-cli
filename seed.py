from model import *

db.connect()
db.drop_tables([Note])
db.create_tables([Note])

Note(title='Monday', notes='Go to GA').save()
Note(title='Tuesday', notes='Go to GA again').save()