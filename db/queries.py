
select_user_by_username = ''' 
    SELECT * 
    FROM users
    WHERE users.username = ?
'''

select_user_by_id = ''' 
    SELECT * 
    FROM users
    WHERE users.id = ?
'''

select_all_users = '''
    SELECT * 
    FROM users
'''


create_users_table = '''
    CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT, 
        password TEXT
    )
'''

drop_users_table = '''
    DROP TABLE users
'''

insert_user = ''' 
    INSERT INTO users(username, password) VALUES (?, ?)
'''

create_items_table = '''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE, 
        price REAL
    )
'''

drop_items_table = ''' 
    DROP TABLE items
'''

insert_item = ''' 
    INSERT INTO items(name, price) VALUES (?, ?)
'''

update_item = '''
    UPDATE items 
    SET price = ? 
    WHERE name = ?
'''

select_all_items = '''
    SELECT * 
    FROM items 
'''

select_item_with_name = '''
    SELECT * 
    FROM items 
    WHERE name = ? 
'''

delete_item = ''' 
    DELETE FROM items 
    WHERE name = ?
'''

