from com.leikr.core import LeikrEngine

class JythonTest(LeikrEngine):
    
    def __init__(self):
        super(JythonTest, self).__init__()
        self.x = 0
    #
    
    def create(self):
        print("hey")
        
    #
        
    def render(self, delta=None):
                
        if(self.key("right")):
            self.x = self.x + 5
            
            
        if(self.key("left")):
            self.x = self.x - 5
            
            
        self.sprite(8, self.x, 20)
    #
