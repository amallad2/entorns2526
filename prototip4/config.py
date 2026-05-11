"""
Configuration for the Prototip4 DAO and Flask app.

Update these values for your MySQL/MariaDB instance if needed.
"""

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "tapatapp",
    "port": 3306,
}

APP_CONFIG = {
    "HOST": "0.0.0.0",
    "PORT": 5000,
    "DEBUG": True,
}
