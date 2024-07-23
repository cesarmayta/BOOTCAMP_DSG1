import mysql.connector
from prefect import task


@task(name='Cargar ofertas en bd')
def task_load_offers(offers):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='db_codigo'
        )
        cursor = conn.cursor()

        query_table = """
        create table if not exists tbl_oferta(
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255),
        ubicacion VARCHAR(255),
        empresa VARCHAR(255),
        fecha DATE,
        url TEXT,
        skill VARCHAR(255)
        )
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_oferta(titulo,ubicacion,empresa,fecha,url,skill)
        values(%s,%s,%s,%s,%s,%s)
        """

        for offer in offers:
            cursor.execute(query_insert,offer)

        conn.commit()
        cursor.close()
        conn.close()
        print("datos guardados en bd...")
    except mysql.connector.Error as err:
        print(err)