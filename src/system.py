from src.members.student import Student
from src.members.interviewer import Interviewer
from src.sessions.session import Session
from src.sessions.slot import Slot
from src.sessions.session_status import SessionStatus
import random
import datetime

class System:

    def __init__(self):

        self.students = set()
        self.interviewers = set()
        self.sessions = set()

    def add_student(self, name, email, phone, address):
        student = Student(name, email, phone, address)
        self.students.add(student)

    def add_interviewer(self, name, email, phone, address):
        interviewer = Interviewer(name, email, phone, address)
        self.students.add(interviewer)

    def add_slot(self, interviewer, start_time, end_time):
        interviewer.add_slot(start_time, end_time)

    def schedule_session(self, student, start_time, end_time):

        if student not in self.students:
            return False

        session_available, msg = student.is_session_available()
        if not session_available:
            print (msg)
            return False

        interviewer_not_allowed = (session.interviewer for session in student.get_session_by_status(SessionStatus.completed))

        for interviewer in self.interviewers:
            if interviewer not in interviewer_not_allowed:
                for slot in interviewer.get_slots():
                    if slot.start_time == start_time  and slot.end_time == end_time:
                        interviewer = slot.created_by()
                        session = Session(slot, student, interviewer)
                        student.add_session(session)
                        interviewer.add_session(session)

                        break