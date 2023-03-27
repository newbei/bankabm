import sqlite3

file = r'D:\workspace\DAT_ABM\bankabm\banksim\result.sqlite'
mydb = sqlite3.connect(file)

cursor = mydb.cursor()
cols = ['bankequity', 'bankdeposit', 'bankloan', 'bankinterestincome', 'bankdepositrate', 'bankreserve', 'bankasset',
        'bankprovision', 'bankriskwgtasset']
','.join(cols)

cursor.execute("SELECT  " + ','.join(cols) + " FROM AgtBank where BankId = 1")
tables = cursor.fetchall()
print(tables)
