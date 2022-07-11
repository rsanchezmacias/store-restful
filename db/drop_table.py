import sqlite3 
import queries as q  

if __name__ == '__main__':
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute(q.drop_items_table)
    
    connection.commit()
    connection.close()

