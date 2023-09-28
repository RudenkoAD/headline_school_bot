import os
from pathlib import Path
import sqlite3

if __name__ == "__main__":
  #os.remove("database.db")#delete the database
  conn = sqlite3.connect(Path("database.sqlite"))#create a new
  cursor = conn.cursor()#create a new table
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS states (
          state_id INTEGER PRIMARY KEY,
          text TEXT,
          next_id_no INTEGER,
          next_id_yes INTEGER,
          next_id_silence INTEGER
      )
  ''')
  conn.commit()
  for path in os.listdir("data"):
    if path.endswith(".txt"):
      with open(os.path.join("data", path), 'r', encoding='utf-16-le') as f:
        cursor.execute('''
            INSERT INTO states (state_id, text, next_id_no, next_id_yes, next_id_silence)
            VALUES (?, ?, ?, ?, ?)
        ''', (path[:-4],f.read(), None, None, None))
        print(path[:-4],f.read()[:5])
  conn.commit()
  