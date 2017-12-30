import sqlite3 as sql

conn = sql.connect("myUrlMap.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS urlMap(shortcut TEXT PRIMARY KEY, url TEXT);")

def data_entry(short_ref, url_ref):
    cursor.execute("INSERT INTO urlMap (shortcut, url) VALUES (?, ?)", (str(short_ref), str(url_ref)))
    conn.commit()

def read_url(short_ref):
    query = "SELECT url FROM urlMap WHERE shortcut = (?)";
    cursor.execute(query, (short_ref,))
    data = cursor.fetchall()
    return data

def see_existing_shortcuts():
    query = "SELECT * FROM urlMap"
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print(row[1] + "   --------------- " + row[0])

def suggestion_list(old):
    old = old + '%'
    dummy = "SELECT shortcut FROM urlMap WHERE shortcut LIKE (?)"
    cursor.execute(dummy, (old,))
    data = cursor.fetchall()
    list = []
    for row in data:
        if len(old) < len(row[0]):
            list.append(row[0])
        else:
            list.clear()
            list.append(old)
            break

    return list

def rename_shortcut(old, new):
    query = "UPDATE urlMap SET shortcut = (?) WHERE shortcut = (?)";
    cursor.execute(query, (new, old))
    conn.commit()

def update_shortcut_given_url(url_ref_old, short_ref_new):
    query = "UPDATE urlMap SET shortcut = (?) WHERE url = (?)";
    cursor.execute(query, (short_ref_new, url_ref_old))
    conn.commit()

def delete(name):
    query = "DELETE FROM urlMap WHERE shortcut = (?)";
    cursor.execute(query, (name,))
    conn.commit()

def close():
    cursor.close()
    conn.close()