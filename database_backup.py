import sqlite3
import shutil

db_path = '/path/to/database.db'
backup_path = '/path/to/backup/database_backup.db'

shutil.copy(db_path, backup_path)
print("Database backup completed.")
