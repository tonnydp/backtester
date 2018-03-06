import sqlite3
import os

con = sqlite3.connect("data.db")
cur = con.cursor()
create_table = """
	CREATE TABLE IF NOT EXISTS Stock (
		code TEXT,
		date TEXT,
		open REAL,
		high REAL,
		close REAL,
		low REAL,
		volume REAL)
"""
cur.execute(create_table)
for root, dirs, files in os.walk("data"):
	for f in files:
		ff = open("data\\" + f, 'r')
		lines = ff.readlines()
		if len(lines) <= 1:
			print(f + "BAD")
			continue
		sql_list = []
		code = f[0:6]
		for l in lines[1:]:
			l_splits = l.split(",")
			sql_list.append((code, l_splits[0], l_splits[1], l_splits[2], l_splits[3], l_splits[4], l_splits[5]))
		cur.executemany("INSERT INTO Stock VALUES(?,?,?,?,?,?,?)", sql_list)
		con.commit()
		ff.close()
		print(f)

cur.close()
con.close()