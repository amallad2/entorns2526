import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


class DaoUser:
    """Simple DAO for the `User` table."""

    def __init__(self, db_config=None):
        self.db_config = db_config or DB_CONFIG

    def _get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def get_user_by_credentials(self, identifier, password):
        """Return user dict if username/email and password match, else None."""
        query = "SELECT id, username, email, token FROM `User` WHERE (username=%s OR email=%s) AND password=%s LIMIT 1"
        try:
            conn = self._get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query, (identifier, identifier, password))
            row = cur.fetchone()
            cur.close()
            conn.close()
            return row
        except Error:
            return None

    def get_user_by_token(self, token):
        """Return user dict if token matches, else None."""
        query = "SELECT id, username, email, token FROM `User` WHERE token=%s LIMIT 1"
        try:
            conn = self._get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query, (token,))
            row = cur.fetchone()
            cur.close()
            conn.close()
            return row
        except Error:
            return None
