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



reprotData = pd.DataFrame(report)

reprotData[['profits', 'sales']].plot()
plt.savefig('graph2.png')



