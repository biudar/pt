import os

from pydub import AudioSegment


def format_2_wav(audioPath='audio.ogg'):
    song = AudioSegment.from_file(audioPath, audioPath[-3:])
    song = song.set_channels(1)
    song.export(audioPath.replace(audioPath[-3:], 'wav'), 'wav')
    return 0


def batach_fromat_2_wav(audioDir='dataset/'):
    for root, dirs, names in os.walk(audioDir):
        for name in names:
            audioPath = os.path.join(root, name)
            if '.ogg' in audioPath or '.mp3' in audioPath:
                format_2_wav(audioPath)
                print audioPath, '.........'

    return 0


def main():
    audioDir = '../data/pyT7/'
    batach_fromat_2_wav(audioDir)
    return 0


if __name__ == '__main__':
    main()
