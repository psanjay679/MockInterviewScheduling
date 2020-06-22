import datetime

class Slot:

    def __init__(self, start_time, end_time, created_by):

        self.__created_at = datetime.datetime.now()
        self.start_time = start_time
        self.end_time = end_time
        self.__created_by = created_by

    @property
    def created_at(self):
        return self.__created_at

    def get_duration(self):
        time_diff = self.end_time - self.start_time
        return time_diff.seconds // 3600

    def created_by(self):
        return self.__created_by