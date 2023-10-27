import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data, header = pyxdf.load_xdf('sub-P001_ses-S001_task-Default_run-001_eeg.xdf')

# print(header)
# print(len(data[0]['time_series'][0]))
# print(type(data[0]['info']['channel_count'][0]))

noOfChannels = int(data[0]['info']['channel_count'][0])  # Number of channels in the dataset
print(noOfChannels)

# print(data[0]['info']['desc'][0]['channels'][0]['channel'][0]['label'])
# print(type(data))

# Extract the EEG data from the loaded XDF data
eeg_data = data[0]['time_series']

# # Extract the channel names from the XDF header
channel_names = []
for channel in range(noOfChannels):
    channel_names.append(data[0]['info']['desc'][0]['channels'][0]['channel'][channel]['label'][0])

print(channel_names)

# # Create a DataFrame from the EEG data with the channel names as column names
df = pd.DataFrame(eeg_data, columns=channel_names)

# # Save the DataFrame to a CSV file
df.to_csv('eeg_data.csv', index=False)

#-----------------------------------------------------Plotting---------------------------

# for stream in data:
#     y = stream['time_series']

#     if isinstance(y, list):
#         # list of strings, draw one vertical line for each marker
#         for timestamp, marker in zip(stream['time_stamps'], y):
#             plt.axvline(x=timestamp)
#             print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
#     elif isinstance(y, np.ndarray):
#         # numeric data, draw as lines
#         plt.plot(stream['time_stamps'], y)
#     else:
#         raise RuntimeError('Unknown stream format')

# plt.show()