class Counter:
    current = 0
    start = 0
    stop = 0
    def __init__(self, start=0, stop=0, current=0):
        self.start = start
        self.stop = stop
        self.current = start

    def get(self):
        print(self.current)
        return

    def increment(self):
        self.current = self.current
        if self.current < self.stop:
            self.current += 1
        elif self.start == 0 and self.stop == 0:
            self.current += 1
        elif self.start > 0 and self.stop == 0:
            self.current += 1
        else:
            print( 'Maximal value is reached.' )
        return