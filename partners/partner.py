'''
defines the interface for partners
'''
class Partner():
    def __init__(self):
        pass

    def bootstrap(self):
        #TODO: Add documentation
        NotImplementedError("Every partner has to implement it's own bootstrap")
    
    #TODO: Add other partner must implement methods here