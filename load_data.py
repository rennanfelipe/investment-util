#!/usr/bin/env python
import csv

class LoadData:
    def __init__(self):
        with open('investment-data/january.csv') as csv_file:
            reader = csv.reader(csv_file)
            self.monthly_investments = list( map(lambda row: [', '.join(row)] , reader) )
            self.monthly_investments.remove( self.monthly_investments[0] )