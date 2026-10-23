# Stack Operations
class MyStack:
    def __init__(self):
        self.stack=[]
    def push(self, x):
        self.stack.append(x)
        pass

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
        pass

    def peek(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1]
        pass

    def getSize(self):
        return len(self.stack)
        pass

    def isEmpty(self):
        return len(self.stack)==0
        pass
