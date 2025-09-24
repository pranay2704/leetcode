class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.lis=[]

    
    def enqueue(self, x):
        # Insert element into the queue
        self.lis.insert(0,x)

    
    def dequeue(self):
        # Remove element from the queue
        self.lis=self.lis[:-1]

    
    def getFront(self):
        # Get front element
        return self.lis[-1]

    
    def getMin(self):
        # Get minimum element
        return min(self.lis)

    
    def getMax(self):
        # Get maximum element
        return max(self.lis)
