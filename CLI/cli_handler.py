# Main class for cli handler operations
from cli_exception import CliException
import pexpect

class CliHandler:
    ''' Cli Handler class '''
    
    timeout = 60

    def __init__(self, command):
        ''' Init Method '''
        self.command = command
        self.process_handle = pexpect.spawn(self.command)
    
    def expect_data(self, expected_data):
        ''' Wrapper function for pexpect.expect method. '''
        self.process_handle.expect(expected_data)

    
    def send_data(self, data_to_send):
        ''' Wrapper function for pexpect.sendline method. '''
        self.process_handle.sendline(data_to_send)
    
    def __str__(self):
        return 'Process to be Spawn : ' + self.command