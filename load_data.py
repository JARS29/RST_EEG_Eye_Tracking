from common.xdf import load_xdf
import numpy as np

def importing_data(filename):
    raw=load_xdf(filename)
    for i in range(len(raw[0])):
        if raw[0][i]['info']['name']==['Tobii']:
            eye_data=raw[0][i]
        elif raw[0][i]['info']['name']==['openbci_eeg']:
            EEG_data=raw[0][i]
        elif raw[0][i]['info']['name'] == ['Reading_Span_Test']:
            RST_data=raw[0][i]
        elif raw[0][i]['info']['name'] == ['Keyboard']:
            key_data=raw[0][i]

    return RST_data,EEG_data,eye_data,key_data

def extracting_index(RST_data, data, type ):   # RST data for the ts of the sentences+recall, data for the indexes (either EEG or Eye-tracking), type= 'sentences' or 'recall'
    index_sent=[]
    index_recall=[]
    [index_sent.append(index) for index, value in enumerate(RST_data['time_series']) if value == [u'Start_sentence']]
    [index_recall.append(index) for index, value in enumerate(RST_data['time_series']) if value == [u'Start_recall']]
    stamps_sent = [RST_data['time_stamps'][index_sent],RST_data['time_stamps'][np.array(index_sent)+1]]         # Start sentence, Final Sentence (indexes)
    stamps_recall = [RST_data['time_stamps'][index_recall],RST_data['time_stamps'][np.array(index_recall)+1]]   # Start recall, Final recall (indexes)
    index_beg = []
    index_end = []
    if type == 'sentences':
        for i in range(np.shape(stamps_sent)[1]):
            temp_1 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_sent[0][i]))
            temp_2 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_sent[1][i]))
            index_beg.append(temp_1[0][1])  #First item for beginning
            index_end.append(temp_2[0][-1]) #Last item for ending
        return index_beg, index_end

    if type == 'recall':
        for i in range(np.shape(stamps_recall)[1]):
            temp_1 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_recall[0][i]))
            temp_2 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_recall[1][i]))
            index_beg.append(temp_1[0][1])  #First item for beginning
            index_end.append(temp_2[0][-1]) #Last item for ending
        return index_beg, index_end



def extracting_data(data,beg,end):  # data (either EEG or Eye_data)
    raw_data = {}
    temp = {}
    for i in range(len(end)):
        temp['raw'] = data['time_series'][beg[i]:end[i]]
        temp['ts'] = data['time_stamps'][beg[i]:end[i]]
        raw_data[i + 1] = temp.copy()
    return raw_data


