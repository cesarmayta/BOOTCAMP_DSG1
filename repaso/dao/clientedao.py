from .dao import DAO

class ClienteDAO(DAO):

    def __init__(self):
        super().__init__()
        query_create = """
        CREATE TABLE IF NOT EXISTS tbl_cliente(
            id INT AUTO_INCREMENT PRIMARY KEY,
            razon_social VARCHAR(255) NOT NULL,
            ruc VARCHAR(20) NOT NULL,
            direccion TEXT,
            linea_credito INT default 0
        );
        """
        self.cursor.execute(query_create)
        self.db.commit()

    def insertar(self,cliente):
        nuevo_cliente = (
            cliente.ruc,
            cliente.razon_social,
            cliente.direccion,
            cliente.linea_credito
        )
        query = "insert into tbl_cliente(ruc,razon_social,direccion,linea_credito) values(%s,%s,%s,%s)"
        self.cursor.execute(query,nuevo_cliente)
        self.db.commit()