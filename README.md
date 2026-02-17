# SQLAlchemy CRUD sample

Small demo app showing basic CRUD operations for a `User` using SQLAlchemy and SQLite.

Files added:

- `models.py` - SQLAlchemy `User` model
- `db.py` - Engine and `init_db()`
- `crud.py` - Create/read/update/delete helper functions
- `main.py` - CLI and `demo` runner showing operations
- `requirements.txt` - minimal dependency list

Quick start:

1. (Optional) create a venv and activate it.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run the demo sequence:

```bash
python main.py demo
```

Or use the CLI to create/list/get/update/delete users:

```bash
python main.py create alice alice@example.com "Alice"
python main.py list
python main.py get 1
python main.py update 1 full_name "Alice Smith"
python main.py delete 1
```

The database file `users.db` will be created in the workspace by default.
# SQLAlchemy-CRUD
