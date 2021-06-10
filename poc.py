import math  # import needed modules
import pyaudio  # sudo apt-get install python-pyaudio


def generate_wavedata(frequency, length):
    FREQUENCY = frequency  # Hz, waves per second, 261.63=C4-note.
    LENGTH = length/4  # seconds to play sound

    BITRATE = 16000  # number of frames per second/frameset.

    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY + 100

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''

    # generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)

    return WAVEDATA


def play_song_about_cat():
    PyAudio = pyaudio.PyAudio  # initialize pyaudio

    sound_list = [(784, 1), (659, 1), (659, 1), (699, 1), (587, 1), (587, 1), (523, 0.5), (659, 0.5), (784, 2)]
    BITRATE = 16000  # number of frames per second/frameset.

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)

    for sound in sound_list:
        frequency, length = sound
        wavedata = generate_wavedata(frequency, length)
        stream.write(wavedata)
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    play_song_about_cat()
