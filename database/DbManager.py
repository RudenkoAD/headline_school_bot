import sqlite3
from .schemas import State
class StateDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS states (
                state_id INTEGER PRIMARY KEY,
                text TEXT,
                next_id_no INTEGER,
                next_id_yes INTEGER,
                next_id_silence INTEGER
            )
        ''')
        self.conn.commit()

    def insert_state(self, state):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO states (state_id, text, next_id_no, next_id_yes, next_id_silence)
            VALUES (?, ?, ?, ?, ?)
        ''', (state.state_id, state.text, state.next_id_no, state.next_id_yes, state.next_id_silence))
        self.conn.commit()

    def get_state_by_id(self, state_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM states WHERE state_id = ?', (state_id,))
        row = cursor.fetchone()
        if row:
            return State(*row)
        return None

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db = StateDatabase("states.db")

    state1 = State(1, "Text 1", 2, 3, 4)
    state2 = State(2, "Text 2", 5, 6, 7)

    db.insert_state(state1)
    db.insert_state(state2)

    retrieved_state = db.get_state_by_id(1)
    print(retrieved_state)

    db.close()
