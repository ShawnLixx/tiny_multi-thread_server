class Operation:
    def __init__(self, urlString):
        self.string = urlString
        if urlString.find('+') != -1:
            self.operation = '+'
        elif urlString.find('-') != -1:
            self.operation = '-'
        elif urlString.find('*') != -1:
            self.operation = '*'
        self.a = int(urlString[0: urlString.find(self.operation)])
        self.b = int(urlString[urlString.find(self.operation) + 1: ])
