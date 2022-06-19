# graph from scratch

import re
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series([18, 42, 9, 32, 81, 64, 3])

report = {
    'profits':[50,100,35,88],
    'sales':[100, 120, 80, 90]
}


reprotData = pd.DataFrame(report)

reprotData[['profits', 'sales']].plot()
plt.savefig('graph2.png')


