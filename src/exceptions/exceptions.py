class SessionNotAvailable(Exception):
    def __init__(self, msg):
        super(SessionNotAvailable, self).__init__(msg)


class RatingNotInRange(Exception):
    def __init__(self, msg):
        super(RatingNotInRange, self).__init__(msg)

