from common.xdf import load_xdf
import numpy as np

def importing_data(filename, data):
    raw=load_xdf(filename)
    if data=='eye_data':
        eye_data=raw[0][0]
        return eye_data
    elif data=='EEG':
        EEG_data=raw[0][1]
        return EEG_data
    elif data=='RST':
        RST_data=raw[0][2]
        return RST_data
    elif data=='key_board':
        key_data=raw[0][3]
        return key_data


def extracting_data(eye_data, EEG_data, RST_data):