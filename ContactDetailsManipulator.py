import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData
import csv

engine = db.create_engine('sqlite:///contactData.sqlite')
connection = engine.connect()
meta = MetaData()

contactData = Table(
   'contactData', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
   Column('gender', String),
   Column('phoneNumber', String),
)

meta.create_all(engine)

contactDataArray = []

with open('MOCK_DATA.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        contactDataArray.append({'name' : row[1], 'lastname' : row[2], 'gender' : row[3], 'phoneNumber' : row[4]})


result = connection.execute(contactData.insert(), contactDataArray)

cD = contactData.select()
result = connection.execute(cD)

contactDataArray = []

for row in result:
   contactDataArray.append(row)

print(contactDataArray[7:9])

connection.close()
db.dispose()