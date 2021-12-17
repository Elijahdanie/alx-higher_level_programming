import MySQLdb

class FetchPlayer:
    cursor = None
    def __init__(self, host, user, password, database):
        self.conn = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
        self.cursor = self.conn.cursor()
    
    def printplayer(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()

db = FetchPlayer('localhost', 'root', 'eljyz12341187', 'gameserverdb')

result = db.printplayer('select * from playerdbs')

print(f'\n{db} \n')

db.close()

