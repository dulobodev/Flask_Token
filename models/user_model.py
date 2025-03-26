import sqlite3
from database.db import get_db_connection
 
class UserModel:
 
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        return user
 
    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return user
 
    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
        return True
 
    @staticmethod
    def update_user(user_id, username=None, password=None):
        conn = get_db_connection()
        if username:
            conn.execute('UPDATE users SET username = ? WHERE id = ?', (username, user_id))
        if password:
            conn.execute('UPDATE users SET password = ? WHERE id = ?', (password, user_id))
        conn.commit()
        conn.close()
 
    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_name_cadastrado(name):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM cadastrados WHERE name = ?', (name,)).fetchone()
        conn.close()
        return user
 
    @staticmethod
    def find_by_id_cadastrado(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM cadastrados WHERE id = ?', (id,)).fetchone()
        conn.close()
        return user
 
    @staticmethod
    def create_cadastro(name, email, data, cpf, genero):
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO cadastrados (name, email, data, cpf, genero) VALUES (?, ?, ?, ?, ?)', (name, email, data, cpf, genero))
            conn.commit()
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
        return True
 
    @staticmethod
    def update_cadastrado(id, name=None, email=None, data=None, cpf=None, genero=None):
        conn = get_db_connection()
        if name:
            conn.execute('UPDATE cadastrados SET name = ? WHERE id = ?', (name, id))
        if email:
            conn.execute('UPDATE cadastrados SET email = ? WHERE id = ?', (email, id))
        if data:
            conn.execute('UPDATE cadastrados SET data = ? WHERE id = ?', (data, id))
        if cpf:
            conn.execute('UPDATE cadastrados SET cpf = ? WHERE id = ?', (cpf, id))
        if genero:
            conn.execute('UPDATE cadastrados SET genero = ? WHERE id = ?', (genero, id))
        conn.commit()
        conn.close()
 
    @staticmethod
    def delete_cadastrado(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM cadastrados WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    