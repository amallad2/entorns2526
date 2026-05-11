Prototip4 - Login service

Files:
- `config.py` - DB and app configuration (update credentials as needed)
- `dao.py` - Data access object for `User` table
- `app.py` - Flask app exposing `/login` endpoint
- `requirements.txt` - Python dependencies

Run (Windows PowerShell):

1. Create and activate a virtual environment (recommended):

   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2. Install deps:

   pip install -r requirements.txt

3. Edit `config.py` to point to your database.

4. Run the app:

   python app.py

Endpoints:
- POST /login
  - With JSON body: {"username": "mare", "password": "mare"}
  - Or with header `Authorization: <token>` to validate by token.
