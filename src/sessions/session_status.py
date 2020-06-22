import enum

class SessionStatus(enum.Enum):
    scheduled = 1
    completed = 2
    cancelled = 3
    rescheduled = 4