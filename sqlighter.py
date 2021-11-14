import sqlite3


class SQLighter:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users ( 
                id INT,
                nickname TEXT,
                balance INT
                )""")



    def commit(self):
        self.connection.commit()
    


    def add_user(self, id, nickname, balance):
	    with self.connection:
	        return self.cursor.execute('INSERT INTO users VALUES (?,?,?)',(id, nickname, balance))
    

    
    def get_nickname(self, id):
        with self.connection:
            return self.cursor.execute('SELECT nickname FROM `users` WHERE `id` = ?', (id,)).fetchone()

    def get_balance(self, id):
        with self.connection:
            return self.cursor.execute('SELECT balance FROM `users` WHERE `id` = ?', (id,)).fetchone()
    


    def edit_nickname(self, id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `nickname` = ? WHERE `id` = ?", (nickname, id))

    def edit_nickname(self, id, balance):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `balance` = ? WHERE `id` = ?", (balance, id))
    