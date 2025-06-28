class MemoryStore:
    def __init__(self):
        self.records = {}

    def store(self, agent, expr, score):
        if agent not in self.records or self.records[agent]['score'] < score:
            self.records[agent] = {'expression': expr, 'score': score}

    def get(self, agent):
        return self.records.get(agent, None)