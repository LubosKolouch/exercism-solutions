class Clock:

    def to_clock(self):
        self.hours = self.in_minutes // 60 % 24
        self.minutes = self.in_minutes % 60

        self.clock = "{:0>2d}".format(self.hours) + ':' \
                     + "{:0>2d}".format(self.minutes)

    def __init__(self, hour, minute):
        self.in_minutes = hour*60+minute
        self.to_clock()

    def __repr__(self):
        return self.clock

    def __eq__(self, other):
        return self.clock == other

    def __add__(self, minutes):
        self.in_minutes += minutes
        self.to_clock()
        return self.clock

    def __sub__(self, minutes):
        self.in_minutes -= minutes
        self.to_clock()
        return self.clock
