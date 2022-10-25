# https://www.py4e.com/tools/sql-intro/?PHPSESSID=89cb3b96c3cae7622b2a91c505aa07f6

import sqlite3
import re

conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox.txt'

fname = 'mbox.txt'

fh = open(fname)
for line in fh:
    line.strip()
    if not re.search('From: ', line): continue
    org = re.findall('@(\S+)', line)[0]
    # (org,) is a singleton tuple
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) 
    row = cur.fetchone()    # fetch the first one
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

conn.commit()
cur.close()