# Main class for cli handler operations
from cli_exception import CliException
import pexpect
import sys, os

class CliHandler:
    ''' Cli Handler class '''
    
    timeout = 60

    def __init__(self, command):
        ''' Init Method '''
        self.command = command
        self.process_handle = pexpect.spawn(self.command)
        #self.process_handle.logfile = sys.stdout
        #self.process_handle.logfile = os.fdopen(sys.stdout.fileno(), 'w', 0)
    
    def expect_data(self, expected_data):
        ''' Wrapper function for pexpect.expect method. '''
        print('Expected Data : ', expected_data)
        index = self.process_handle.expect([expected_data, pexpect.EOF, pexpect.TIMEOUT])
        if index == 2:
            raise CliException('Timeout Occured')
        elif index == 1:
            raise CliException('EOF reached')
        else:
            print('Expected data exists in the output')
            print(self.process_handle.match.group())
            #print(self.process_handle.before)
            #print(self.process_handle.after)
    
    def send_data(self, data_to_send):
        ''' Wrapper function for pexpect.sendline method. '''
        print('Comamnd to be executed : ', data_to_send)
        self.process_handle.sendline(data_to_send)
    
    def __str__(self):
        return 'Process to be Spawn : ' + self.command
    
    def __del__(self):
        pass