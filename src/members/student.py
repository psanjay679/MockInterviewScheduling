from .member import Member
from src.constants.constants import Constants
from src.sessions.session_status import SessionStatus
import datetime


class Student(Member):

    def __init__(self, name, email, phone, address):
        super(Student, self).__init__(name, email, phone, address)
        self.sessions = list()

    def is_session_available(self):

        if self.get_session_by_status(SessionStatus.scheduled):
            return False, 'You have already scheduled a session'

        sessions = self.get_session_by_status(SessionStatus.completed)

        if len(sessions) == Constants.MAX_SESSION_PER_STUDENT:
            return False, 'You have already completed maximum interviews'

        if len(sessions) >= 2 and (sessions[-1].rating < 2 or sessions[-2].rating < 2):
            return False, 'Your last 2 ratings didn\' go well'

        return True, 'There are multiple slots available'

    def add_session(self, session):
        self.sessions.append(session)

    def get_all_sessions(self):
        return self.sessions

    def get_session_by_status(self, session_status: SessionStatus):

        sessions = list()
        for session in self.sessions:
            if session.session_status == session_status:
                sessions.append(session)

        return sessions

    def attend_session(self, session):

        current_time = datetime.datetime.now()
        if session.session_status in (SessionStatus.scheduled, SessionStatus.rescheduled) and \
                session.slot.start_time <= current_time < session.slot.end_time:
            session.session_status = SessionStatus.running
