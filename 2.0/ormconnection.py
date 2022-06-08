from sqlalchemy import create_engine,select,MetaData,Table,and_,all_,text
import sqlalchemy as sql
import psycopg2


class OrmConnection():
    def __init__(self):
        self.eng = create_engine("postgresql://postgres:1910@localhost:5432/dvdrental")
        self.conn = self.eng.connect()

    def connect_orm(self,table_name='',columns_=[],filter_data={}):
        # print(self.eng)
        metadata = MetaData(bind=None)
        table = Table(
            table_name,
            metadata,
            autoload=True,
            autoload_with=self.eng
        )
        columns_data =[]
        table_data = []
        filter_data_=[]
        null_data =['',None]
        if table_name in null_data:
            print("table name is missing")
        elif columns_:
            for i in columns_:
                columns_data.append(eval('table.columns.'+str(i)))
            table_data=columns_data
        if filter_data:
            for key,val in filter_data.items():
                pass

        else:
            table_data=table



        stmt = select(table_data
        #     [
        #     table.columns.actor_id,
        #     table.columns.first_name
        # ]
        ).where(and_(
            table.columns.actor_id == eval('197'),
            table.columns.first_name == 'Reese'
        )
        )

        connection = self.eng.connect()
        results = connection.execute(stmt).fetchall()
        # print(results)
        for i in results:
            print(i)

if __name__ == '__main__':
    orm = OrmConnection()
    orm.connect_orm(table_name='actor',columns_=['actor_id','first_name'])