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