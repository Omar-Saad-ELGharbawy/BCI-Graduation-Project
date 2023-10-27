import pylsl
from pylsl import StreamInlet, resolve_stream


print("Detect Stream")

streams = pylsl.resolve_stream()
print(streams)
# streams = pylsl.resolve_stream('type','EEG')
print("#"*50)
inlet = StreamInlet(streams[0])
sample, timestamp = inlet.pull_sample()
print(timestamp, sample)

# pylsl.stream_inlet()

# print(type(streams))
print("#"*50)