import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


"""
Xdf class documentation:
    This class is used to read the xdf file and extract the data from it.
    It has the following methods:
    1. getData() - returns the data from the xdf file
    2. getHeader() - returns the header of the xdf file
    3. getChannelCount() - returns the number of channels in the xdf file
    4. getChannelNames() - returns the names of the channels in the xdf file
    5. getSamplingRate() - returns the sampling rate of the xdf file
    6. getChannelData() - returns the data of a specific channel
    7. toCSV() - converts the data of the xdf file into a csv file
    8. getOriginalTimeStampsList() - returns the original time stamps of the xdf file
    9. getCalibratedTimeStampsList() - returns the calibrated time stamps of the xdf file (Starts from Zero)
    10. getSessionDuration() - returns the duration of the session in seconds
    11. getDataFrame() - returns the data of the xdf file as a dataframe
"""

class Xdf: 
    __channel_names = []
    __eeg_data = []
    __session_time = 0
    __time_stamps = []

    def __init__(self, path):
        self.__path = path
        self.__data, self.__header = pyxdf.load_xdf(self.__path)
        self.__eeg_data = self.__data[0]['time_series']
        self.__noOfChannels = int(self.__data[0]['info']['channel_count'][0])
        self.__samplingRate = self.__data[0]['info']['nominal_srate'][0]
        self._channelsPosition()
        self.__time_stamps = self.__data[0]['time_stamps']
        self.__session_time = self.__time_stamps[-1] - self.__time_stamps[0]
        self.__df = pd.DataFrame(self.__eeg_data, columns=self.__channel_names)

    def getData(self):
        return self.__data
    
    def getHeader(self):
        return self.__header
    
    def getChannelCount(self):
        return self.__noOfChannels
    
    def _channelsPosition(self):
        for channel in range(self.__noOfChannels):
            # self.__channel_names.append(self.__data[0]['info']['desc'][0]['channels'][0]['channel'][channel]['label'][0])
            self.__channel_names.append(self.__data[0]['info']['desc'][0]['channels'][0]['channel'][channel]['label'][0].split("\n")[0])

    def getChannelNames(self):
        return self.__channel_names
    
    def getSamplingRate(self):
        return self.__samplingRate
    
    def getChannelData(self, channelName):
        # channelName = channelName.upper()
        return self.__df[channelName]
    
    def getDataFrame(self, timeStampFlag = True):
        if(timeStampFlag):
            self.__df.insert(0, 'time stamp', self.getCalibratedTimeStampsList())
        return self.__df
        
    def toCSV(self, fileName, timeStampFlag = True):
        self.getDataFrame(timeStampFlag)
        self.__df.to_csv(fileName, index=False)

    def getOriginalTimeStampsList(self):
        return self.__time_stamps
    
    def getCalibratedTimeStampsList(self):
        return self.__time_stamps - self.__time_stamps[0]
    
    def getSessionDuration(self):
        return self.__session_time

#-----------------------------------------------------Testing---------------------------
# Object of Xdf Class  
# file = Xdf('Data/sub-P001_ses-S001_task-Hady_run-001_eeg.xdf')
# file = Xdf('E:\\BCI\\Muse\\Data\\Test\\sub-P001\\ses-S001\\eeg\\sub-P001_ses-S001_task-Default_run-001_eeg.xdf')
# file = Xdf('Data/sub-P001_ses-S001_task-Default_run-001_eeg.xdf)

#---------------------------------Class Testing-----------------------------------------
# print(file.getChannelData('Fp1'))
# print(file.getOriginalTimeStampsList())
# print(file.getChannelNames())
# print(file.getChannelCount())
# print(file.getSessionDuration())
# print(file.getData())
# print(file.getSamplingRate())
# file.toCSV('testClass.csv', False)
# print(header)


#-----------------------------------------------------Plotting---------------------------
# for stream in file.getData():
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