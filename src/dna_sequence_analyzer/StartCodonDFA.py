class StartCodonDFA:
    def __init__(self):
        self.state = 0

    def process(self, input):
        self.state = 0

        for symbol in input:
            if self.state == 0:
                if symbol == 'A':
                    self.state = 1
                else:
                    self.state = -1

            elif self.state == 1:
                if symbol == 'T':
                    self.state = 2
                else:
                    self.state = -1

            elif self.state == 2:
                if symbol == 'G':
                    self.state = 3
                else:
                    self.state = -1

            elif self.state == 3:
                self.state = -1

            elif self.state == -1:
                self.state = -1

        return self.state == 3
