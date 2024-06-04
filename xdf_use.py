from xdf import *

# file = Xdf('BCI Data\sub-Anwar\ses-S001\eeg\sub-Anwar_ses-S001_task-Baseline_run-002_eeg.xdf')
file = Xdf('magdy\sub-magdy\ses-S001\eeg\sub-magdy_ses-S001_task-Right Release_run-003_eeg.xdf')

print(file.getSamplingRate())

print(file.getOriginalTimeStampsList())

file.toCSV('testClass.csv', True)