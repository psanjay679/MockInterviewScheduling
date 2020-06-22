from .member import Member
from src.constants.constants import Constants
from src.sessions.session_status import SessionStatus


class Student(Member):

    def __init__(self, name, email, phone, address):
        super(Student, self).__init__(name, email, phone, address)
        self.sessions = list()

    def is_session_available(self):

        sessions = self.get_session_by_status(SessionStatus.completed)

        if len(sessions) == Constants.MAX_SESSION_PER_STUDENT:
            return False

        if len(sessions) >= 2 and (sessions[-1].rating < 2 or sessions[-2].rating < 2):
            return False

        return True

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

