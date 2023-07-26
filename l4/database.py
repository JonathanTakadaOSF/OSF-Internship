from peewee import Model, PostgresqlDatabase

app_config = {
    'DATABASE': {
        'name': 'osf_training',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432,
    }
}

db = PostgresqlDatabase(
    app_config['DATABASE']['name'],
    user=app_config['DATABASE']['user'],
    password=app_config['DATABASE']['password'],
    host=app_config['DATABASE']['host'],
    port=app_config['DATABASE']['port'],
)

class BaseModel(Model):
    class Meta:
        database = db

