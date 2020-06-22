from .member import Member
from src.sessions.slot import Slot
import datetime
from src.exceptions import exceptions

class Interviewer(Member):

    def __init__(self, name, email, phone, address):
        super(Interviewer, self).__init__(name, email, phone, address)
        self.sessions = list()
        self.slots = list()

    def add_slot(self, start_time, end_time):
        slot = Slot(start_time, end_time, self)
        self.slots.append(slot)

    def get_slots(self):
        slots = list()
        for slot in self.slots:
            if slot.created_by >= datetime.datetime.now():
                slots.append(slot)

        return slots

    def add_session(self, session):
        self.sessions.append(session)

    def rate_session(self, session, rating):

        if session not in self.sessions:
            raise exceptions.SessionNotAvailable('Session is not available to be rated')

        if not (1 <= rating <= 5):
            raise exceptions.RatingNotInRange('rating not in range')

        session.rating = rating
