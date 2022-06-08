from sqlalchemy.sql.expression import select
from sqlalchemy import create_engine,MetaData,Table,and_,all_


class OrmConnection():
    def __init__(self):
        self.eng = create_engine("postgresql://postgres:1910@localhost:5432/dvdrental")
        self.conn = self.eng.connect()

    def connect_orm(self,table_name='',columns_=[]):
        # print(self.eng)
        metadata = MetaData(bind=None)
        table = Table(
            table_name,
            metadata,
            autoload=True,
            autoload_with=self.eng
        )
        columns_data = []
        table_data = []
        null_data = ['', None]
        if table_name in null_data:
            print("table name is missing")
        elif columns_:
            for i in columns_:
                columns_data.append('table.columns.'+str(i))
            table_data = columns_data
        else:
            table_data = table

        data = select(table=table_data)

