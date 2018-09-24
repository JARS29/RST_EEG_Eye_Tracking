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


def extracting_index(RST_data):
    index_sent=[]
    index_recall=[]
    [index_sent.append(index) for index, value in enumerate(RST_data['time_series']) if value == [u'Start_sentence']]
    [index_recall.append(index) for index, value in enumerate(RST_data['time_series']) if value == [u'Start_recall']]
    stamps_sent = [RST_data['time_stamps'][index_sent],RST_data['time_stamps'][np.array(index_sent)+1]]
    stamps_recall = [RST_data['time_stamps'][index_recall],RST_data['time_stamps'][np.array(index_recall)+1]]

    return stamps_recall, stamps_sent

def extracting_EEG(EEG_data, stamps):
    size=np.shape(stamps)[1]

def extracting_eye(eye_data, stamps):
    size = np.shape(stamps)[1]
    data={}
    data_sentences={}
    for i in range(size):
        data['raw'] = []
        while (True):
            data['raw'].append(np.transpose())

