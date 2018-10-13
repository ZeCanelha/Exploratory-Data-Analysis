import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

path1 = "/Users/zecanelha/Desktop/1o Semestre/MEI/Datasets/SDSC-SP2.txt"

path2 = "MEI/Datasets/HPC2N.txt"

columns = ["Job Number", "Submit Time","Wait Time","Run Time","Number of Allocated Processors","Average CPU Time Used","Used Memory," \
			"Requested Number of Processors","Requested Time","Requested Memory","Status","UserID","Group ID","Executable Number", \
           	"Queue Number","Partition Number","Preceding Job Number","Think"]

try:
	dataset = pd.read_table(path1, delimiter = ',', header = None, names = columns);
except IOError as e:
	print(e)


# Get number of canceled jobs - 5 - and finished jobs - 1 - 

status = dataset['Status']
plt.hist(status, bins = 'auto', align = 'mid', label = 'Status of the jobs')
plt.show()







