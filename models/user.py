from werkzeug.security import check_password_hash

from config import mysql


class User(object):

    @staticmethod
    def register(login, password, email, regdate, status) -> None:
        connection = mysql.get_db()
        cursor = mysql.get_db().cursor()  # create cursor
        sql_query = """
            insert into users (login, password, email, regdate, status)
            values (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def auth(login, password):
        connection = mysql.get_db()
        cursor = mysql.get_db().cursor()  # create cursor
        sql_query = f"""
            select * from users 
            where login = '{login}';
        """
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        print(result)
        if len(result) > 0:
            client_pass = result[0][2]
            if check_password_hash(client_pass, password):
                return True
            else:
                return False
