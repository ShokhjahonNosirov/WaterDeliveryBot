import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            language varchar(3),
            suv varchar(255),
            pompa varchar(255),
            tel varchar(255),
            manzil varchar(300),
            idish varchar(255),
            izoh varchar(300),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, suv: str = None, pompa: str = None,
                 tel: str = None, manzil: str = None, idish: str = None,
                 izoh: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, suv, pompa, tel, manzil, idish, izoh, language) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)                                    
        """
        self.execute(sql, parameters=(id, name, suv, pompa, tel, manzil, idish, izoh, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    # biz qo'shadigan kod

    def add_tel(self, tel, id):

        sql = f"""
        UPDATE Users SET tel=? WHERE id=?
        """
        return self.execute(sql, parameters=(tel, id), commit=True)

    def add_manzil(self, manzil, id):

        sql = f"""
        UPDATE Users SET manzil=? WHERE id=?
        """
        return self.execute(sql, parameters=(manzil, id), commit=True)

    def add_idish(self, idish, id):

        sql = f"""
        UPDATE Users SET idish=? WHERE id=?
        """
        return self.execute(sql, parameters=(idish, id), commit=True)

    def add_izoh(self, izoh, id):

        sql = f"""
        UPDATE Users SET izoh=? WHERE id=?
        """
        return self.execute(sql, parameters=(izoh, id), commit=True)

    def add_savat_suv(self, suv, id):

        sql = f"""
        UPDATE Users SET suv=? WHERE id=?
        """
        return self.execute(sql, parameters=(suv, id), commit=True)

    def add_savat_pompa(self, pompa, id):

        sql = f"""
        UPDATE Users SET pompa=? WHERE id=?
        """
        return self.execute(sql, parameters=(pompa, id), commit=True)

    def get_suv(self, id):
        sql = f"""
        SELECT suv FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def get_pompa(self, id):
        sql = f"""
        SELECT pompa FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def get_tel(self, id):
        sql = f"""
        SELECT tel FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def get_manzil(self, id):
        sql = f"""
        SELECT manzil FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def get_idish(self, id):
        sql = f"""
        SELECT idish FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def get_izoh(self, id):
        sql = f"""
        SELECT izoh FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def delete_suv(self, id):
        self.execute("UPDATE Users SET suv = NULL WHERE id = ?", (id,), commit=True)

    def delete_pompa(self, id):
        self.execute("UPDATE Users SET pompa = NULL WHERE id = ?", (id,), commit=True)

    def delete_user(self, id):
        self.execute("DELETE FROM Users WHERE id = ?", (id,), commit=True)

    def get_all_ids(self):
        sql = """
        SELECT id FROM Users
        """
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")


    # def update_user_email(self, email, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
    #
    #     sql = f"""
    #     UPDATE Users SET email=? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(email, id), commit=True)