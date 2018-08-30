# Openssl commands automation demo using python

from cli_handler import CliHandler
from cli_exception import CliException
import sys

openssl_binary = '/usr/bin/openssl'

try:
    cli_handle = CliHandler(openssl_binary)
    print(cli_handle)
    cli_handle.expect_data('OpenSSL>')
    cli_handle.send_data('version') #Cheking version of openssl
    cli_handle.expect_data('OpenSSL 1.1.0g  2 Nov 2018')
    # Generate a random hex string of length 16
    cli_handle.send_data('rand -hex 16')
except CliException as e:
    print(e)
except Exception as exp:
    print(exp)
    sys.exit()