from xdf import *

file = Xdf('E:\\BCI\\Muse\\Data\\Test\\sub-P001\\ses-S001\\eeg\\sub-P001_ses-S001_task-Default_run-001_eeg.xdf')

print(file.getSamplingRate())
file.toCSV('testClass.csv', False)