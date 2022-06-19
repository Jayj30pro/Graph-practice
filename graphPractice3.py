# graph from scratch

import re
import matplotlib.pyplot as plt
import pandas as pd


profitInput = []
salesInput = []

report = {
    'profits':profitInput,
    'sales':salesInput
}

print("I need the numnbers for this month's report /nremember I can only accept complete records")

entries = int(input("How many record will you enter?  "))

for i in range(entries):
    prof = int(input("enter profits "))
    sale = int(input("enter sales "))
    profitInput.append(prof)
    salesInput.append(sale)

reprotData = pd.DataFrame(report)

reprotData[['profits', 'sales']].plot(kind='bar')
plt.savefig('graph3.png')



