class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sequence = ""
        while self.n > 0:
            self.even(self.printNumber)
            self.odd(self.printNumber)
            self.zero(self.printNumber)
            self.n -= 1
            
        print(self.sequence)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        self.sequence = str(0) + self.sequence
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        if self.n <= 0:
            return
        else:
            if self.n % 2 == 0:
                self.sequence = str(self.n) + self.sequence
                
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        if self.n <= 0:
            return
        else:
            if self.n % 2 == 1:
                self.sequence = str(self.n) + self.sequence
            
            
    def printNumber(self):
        return self.n
    
    
if __name__ == "__main__":
  n = 5
  zeroConst = ZeroEvenOdd(n)