#import necessary modules
import csv
with open('MOCK_DATA.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)


