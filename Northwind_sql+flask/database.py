import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d =  dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts

def get_all_facts():
    return query('''SELECT * FROM Supplier 
        ORDER BY CompanyName''')

def get_products(supplier_id):
    return query('''
        SELECT * FROM Product
        WHERE SupplierId = ?''', supplier_id)
    