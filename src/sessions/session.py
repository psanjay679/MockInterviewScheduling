import datetime
from .slot import Slot
from src.members.student import Student
from src.members.interviewer import Interviewer


class Session:

    def __init__(self, slot: Slot, created_by: Student, interviewer: Interviewer):
        self.__occurred_at = datetime.datetime.now()
        self.session_status = None
        self.slot = slot
        self.rating = None
        self.__created_by = created_by
        self.__interviewer = interviewer

    @property
    def created_by(self):
        return self.__created_by

    @property
    def interviewer(self):
        return self.__interviewer

    @property
    def occurred_at(self):
        return self.__occurred_at

    def change_status(self, status):
        self.session_status = status
