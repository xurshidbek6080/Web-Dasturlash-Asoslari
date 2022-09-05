# import sqlite3
#
# conn=sqlite3.connect('xaridor.db')
# # print('success')
# cur=conn.cursor()
# # cur.execute(''' CREATE TABLE xaridor(
# #                 first_name TEXT,
# #                 last_name TEXT,
# #                 email TEXT
# #             )''')
# # cur.execute("INSERT INTO xaridor VALUES('Mastura','Makhamadjanova','mastura@gmail.com')")
# many_xaridor=[
#     ('Ikromjon','Makhamadjanov','ikromjon@gmail.com'),
#     ('Rustamjon','Makhamadjanov','rustamjon@gmail.com'),
#     ('Feruza','Mamutkhanova','mamutkhanova@gmail.com'),
# ]
# # cur.executemany("INSERT INTO xaridor VALUES(?,?,?)",many_xaridor)
# # cur.execute("SELECT rowId,count(*) FROM xaridor")
# cur.execute("SELECT * FROM xaridor WHERE first_name LIKE '%jon' ")
# # print(cur.fetchall())
# # print(cur.fetchone())
# # print(cur.fetchmany(1))
# items=cur.fetchall()
# print("FULLNAME "+"\t\t\t\t\t\tEMAIL")
# print("---------------------"+"\t\t\t\t\t---------------")
# for item in items:
#     # print(item[0]+" "+item[1]+"\t\t"+item[2])
#     print(item)
# conn.commit()
# conn.close()