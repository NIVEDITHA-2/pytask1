import sounddevice as sound
from scipy.io.wavfile import write

freq=44100
second=5
print("recording...")
record_voice=sound.rec(int(second*freq),samplerate=freq,channels=2)
sound.wait()
write("output.wav",freq,record_voice)
print("Finished.....nPlease check your output file")

