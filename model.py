from peewee import *

db = PostgresqlDatabase('notes', user='tiramisu',
                        password='cake', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    notes = CharField()
