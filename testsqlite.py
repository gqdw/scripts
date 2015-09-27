import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stocks 
		(date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
t1 = ('2006-03-28', 'BUY', 'IBM', 1000, 45.00)
c.execute('insert into stocks values (?,?,?,?,?)',t1)
print c.fetchone()

conn.commit()
conn.close()
