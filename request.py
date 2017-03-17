class Request:
    def __init__(self, connection, operation):
        self.connection = connection
        self.operation = operation

    def setAnswer(self, answer):
        self.answer = answer
    def getAnswer(self):
        return self.answer

class Queen:
    def __init__(self):
        self.queen = []
        self.maxLength = 10000
    def add(self, request):
        if len(self.queen) >= self.maxLength:
            return 0
        else:
            self.queen.append(request)
            return 1
    def pop(self):
        if len(self.queen) == 0:
            return 0
        else:
            temp = self.queen[0]
            self.queen.pop(0)
            return temp
    def length(self):
        return len(self.queen)
