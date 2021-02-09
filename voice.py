import sys
import librosa
import warnings
import numpy as np

from datetime import datetime
from scipy.spatial import distance


warnings.filterwarnings('ignore')
x_none = ['0'] # ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def analysis_voice(data_one, data_two):
    exodus = distance.euclidean(data_one, data_two)
    if exodus <= 1.0:
        percent = '100%'
    elif exodus <= 5.9:
        percent = '90%'
    else:
        percent = '1-3%'
    return exodus, percent


def voice_file(file, sr=44100, simp=1):
    data_voice, sr = librosa.load(file, sr)
    original_voice = data_voice.copy()
    sec=str(data_voice.shape[0] / sr)
    print("Author: t.me/antichristone")
    print(f"Length: {sec[:sec.rfind('.')]}-sec")
    print(f"Data: [{data_voice.shape[0]},{sr}]")

    data_voice=data_voice.astype('str')
    for index, data in enumerate(data_voice):
        if data == '0.0':
            pass
        else:
            if data_voice[index][0] == '-':
                pass
            else:
                if data_voice[index][0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    data_voice[index]=data_voice[index].replace(data_voice[index][2], f'009', 1)
                else:
                    data_voice[index]=data_voice[index].replace(data_voice[index][0], '-0', 1)


    data_voice=data_voice.astype(original_voice.dtype)
    return data_voice, np.sin(data_voice*simp), sr, simp, original_voice


def start_programm():
    args = sys.argv
    try:
        args[2]
    except Exception:
        args.append('2')

    start_time=datetime.now()
    result=voice_file(file=args[1], simp=int(args[2]))
    end_time=datetime.now()

    analisys=analysis_voice(result[0], result[4])
    https_t_me_antichristone = args[1][:args[1].rfind('.')]

    librosa.output.write_wav(f'data/{https_t_me_antichristone}_new_voice.mp3', result[0], result[2])
    librosa.output.write_wav(f'data/{https_t_me_antichristone}_new_voice_simp({result[3]}).mp3', result[1], result[2])

    print(f'Speed: {end_time-start_time}')
    print(f'Similarity({analisys[1]}): {analisys[0]}')
    print(f'File: data/{https_t_me_antichristone}_new_voice_simp({result[3]}).mp3\nFile: data/{https_t_me_antichristone}_new_voice.mp3')


try:
    start_programm()
except Exception:
    print(f"Using: python3 voice.py test.mp3")
