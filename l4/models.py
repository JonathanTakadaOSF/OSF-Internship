from peewee import IntegerField, TextField
from database import BaseModel

class User(BaseModel):
    id = IntegerField()
    name = TextField(null=True)
    age = IntegerField()

    class Meta:
        schema = 'training'
        table_name = 'user'

class Purchases(BaseModel):
    user_id = IntegerField()
    name = TextField(null=True)

    class Meta:
        schema = 'training'
        table_name = 'purchases'
