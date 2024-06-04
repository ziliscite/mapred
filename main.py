import csv

from mrjob.job import MRJob
from mrjob.step import MRStep

class MapReduce(MRJob):
    def mapper(self, _, line):
        row = next(csv.reader([line]))
        track_id = row[0]
        try:
            playcount = int(row[2])
        except:
            playcount = 0
        yield track_id, playcount

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield None, (sum(values), key)

    def reducer_sorter(self, key, values):
        for count, key in sorted(values):
            yield count, key

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                combiner=self.combiner,
                reducer=self.reducer
            ),
            MRStep(
                reducer=self.reducer_sorter
            )
        ]

def main():
    MapReduce.run()

if __name__ == "__main__":
    main()
    # Lokal
    # py main.py dataset/User_Listening_History.csv > output/total_listen_id.txt

    # HDFS
    # py main.py -r hadoop User_Listening_History.csv > total_listen_id.txt