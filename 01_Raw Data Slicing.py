import pandas as pd
from os import listdir, path, makedirs
from os.path import isfile, join

class FileSlicer:
    """
    This class is responsible for slicing the CSV-files containing the taxi ride records
    into smaller elements
    """
    def __init__(self):
        """

        """
        self.filesList = []
        self.get_files()
        self.split_data()

    def get_files(self):
        filesList = [f for f in listdir('C:/Users/Luis/Desktop/Uni/_Master/WS 2017/M-DB-PR/Project/Data')
                     if isfile(join('C:/Users/Luis/Desktop/Uni/_Master/WS 2017/M-DB-PR/Project/Data', f)) and
                          '.csv' in f]

        for i in filesList:
            splitString = i.split('_')
            splitDate = splitString[2].split('-')
            self.filesList.append(['C:/Users/Luis/Desktop/Uni/_Master/WS 2017/M-DB-PR/Project/Data/' + i,
                                   splitString[0], splitDate[0], splitDate[1][:2]])

    def split_data(self):
        for i in self.filesList:
            size = 0
            """
            The yellow cab taxi service has a higher ride frequency and therefore needs to be adjusted
            for in the slicing of records to achieve a similar pick up time frame per slice.
            """
            if i[1]  == "yellow":
                size = 1000
            elif i[1] == "green":
                size = 100
            rows = pd.read_csv(i[0], header = 'infer', chunksize = size)
            self.slice_output(rows, i[1], i[2], i[3])

    def slice_output(self, data, color, year, month):
        counter = 0
        newpath = 'C:/Users/Luis/Desktop/Uni/_Master/WS 2017/M-DB-PR/Project/Data/Chunks/' \
                  + color + "_" + year + "_" + month
        if not path.exists(newpath):
            makedirs(newpath)
        for chunk in data:
            if counter < 10:
                chunk.to_csv(newpath + '/_' + str(counter) + ".csv", sep = '\t')
                counter += 1
            else:
                break


class Streamer:
    """
    Pushing of CSV-chunks to Apache Kafka via a Apache Kafka "Producer"
    """
    def __init__(self):
       """

       """


if __name__ == "__main__":
    slicer = FileSlicer()