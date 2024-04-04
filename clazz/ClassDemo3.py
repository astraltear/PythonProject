class JustCounter:
    _secretCount =0
    
    def counter(self):
        self._secretCount+=1
        print self._secretCount
        

counter = JustCounter()
counter.counter()
counter.counter()

print counter._secretCount