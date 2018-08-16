# Custom exception for CLI

class CliException(Exception):
    '''
    Class for CLI Custom exception
    '''

    def __init__(self, msg):
        ''' init function '''
        self.msg = msg
    
    def __str__(self):
        ''' overrding __str__ function for printing error message '''
        return self.msg