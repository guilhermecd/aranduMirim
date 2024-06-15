import peewee
import os
from playhouse.migrate import *

if __name__ == '__main__':

    DB_NAME = 'src/database/arandum_mirim_temp.db'
else:
    DB_NAME = '../database/arandum_mirim.db'
DB = peewee.SqliteDatabase(DB_NAME)


class BaseModel(peewee.Model):
    class Meta:
        database = DB


class Ranking(BaseModel):
    name = peewee.CharField()
    score = peewee.IntegerField()


def start_model():
    # verifica se o arquivo do banco de dados existe (e é um arquivo)
    if not os.path.isfile(DB_NAME):
        # especifica as tabelas
        tables = [
            Ranking,
        ]
        # gera as tabelas
        DB.create_tables(tables)

if __name__ == '__main__':
    start_model()