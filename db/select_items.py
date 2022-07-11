import sqlite3
import queries as q

if __name__ == '__main__': 
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor() 
    
    cursor.execute(q.select_all_items)
    
    print(cursor.fetchall())
    
    connection.close()
