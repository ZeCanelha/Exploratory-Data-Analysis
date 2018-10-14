import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import time, os


# Notes:
# SDSC-SP2
# Duration:	May 1998 thru April 2000
# TimeZoneString is a standard UNIX string indicating the time zone in which the log was generated
# UnixStartTime: 893466664
# TimeZone: -28800
# TimeZoneString: US/Pacific
# StartTime: Fri Apr 24 18:11:04 PDT 1998
# EndTime:   Sat Apr 29 21:08:32 PDT 2000

UnixStartTime = 893466664
os.environ['TZ'] = 'US/Pacific'
time.tzset()


path1 = "/Users/zecanelha/Desktop/1o Semestre/MEI/Datasets/SDSC-SP2.txt"

path2 = "MEI/Datasets/HPC2N.txt"

columns = ["Job Number", "Submit Time","Wait Time","Run Time","Number of Allocated Processors","Average CPU Time Used","Used Memory", \
			"Requested Number of Processors","Requested Time","Requested Memory","Status","UserID","Group ID","Executable Number", \
           	"Queue Number","Partition Number","Preceding Job Number","Think"]


try:
	dataset = pd.read_table(path1, delimiter = ',', header = None, names = columns, index_col = False);
except IOError as e:
	print(e)


# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(UnixStartTime)))
# logStartTime = dataset.loc[dataset.index[0],'Submit Time']


# Get number of canceled jobs - 5 - and finished jobs - 1 -

status = dataset['Status']
plt.hist(status, bins = 'auto', align = 'mid', label = 'Status of the jobs')
plt.xlabel('Status')
plt.ylabel('Number of jobs')
plt.legend()
plt.show()


# Get number of jobs per user

#Get unique users -> set unordered colection of distinct objects

users = set(dataset['UserID'])
jobsPerUser = []

for i in users:
	df = dataset.loc[dataset['UserID'] == i]
	jobsPerUser.append(len(df.index))

plt.plot(jobsPerUser)
plt.xlabel('UserID')
plt.ylabel('Number of jobs')
plt.legend()
plt.grid()
plt.show()

# Get number of jobs per weak

# Get Number of complete jobs per weak

# Number of processors per jobs

plt.plot(dataset['Job Number'],dataset['Number of Allocated Processors'],label = "Number of allocated processors per job")
plt.xlabel('Jobs')
plt.ylabel('Allocated processors')
plt.legend()
plt.grid()
plt.show()

# Comparisation between requested processors and number of processors allocated

plt.subplot(2,1,1)
plt.plot(dataset['Requested Number of Processors'], label = 'Requested Number of processors')
plt.xlabel("Jobs")
plt.ylabel("Requested processors")
plt.grid()

plt.subplot(2,1,2)
plt.plot(dataset['Number of Allocated Processors'], label = 'Number of Allocated Processors')
plt.xlabel("Jobs")
plt.ylabel("Allocated proccessors")
plt.grid()

plt.show()
