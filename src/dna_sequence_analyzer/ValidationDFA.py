def __init__(self):
        self.state = 0

    def process(self, input):
        self.state = 0

        for symbol in input:
            if self.state == 0:
                if symbol in ['A', 'C', 'G', 'T']:
                    self.state = 0
                else:
                    self.state = -1

            elif self.state == -1:
                self.state = -1

        return self.state == 0
