import enum

class SessionStatus(enum.Enum):
    scheduled = 1
    completed = 2
    cancelled = 3
    rescheduled = 4
    running = 5
    did_not_happen = 6