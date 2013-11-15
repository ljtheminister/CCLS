import pickle, sys, re
import datetime as dt


def loadPickledFile(filename):
    return pickle.load(open(filename))


pickle.load(open('temp_list_2009.p'))

dict_index = sorted(list(set([table[12:20] for table in table_list])))
d = dict()



for index in dict_index:
    regexp = '[A-Z]{4}98_[A-Z]{4}_%s\d{4}'%(str(index))
    ts_search = re.compile(regexp) 
    result = filter(ts_search.match, table_list) 
     


if __name__ == '__main__':
    table_list = loadPickledFile(sys.arg[2])
    dict_index = [table[12:20] for table in table_list]
