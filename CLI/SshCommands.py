# Example for Automate CLI command over ssh 
from cli_handler import CliHandler
from cli_exception import CliException

hostname = input('Enter the hostname : ')

username = input('Enter the Username : ')

password = input('Enter the password : ')

print(hostname,username,password, sep=" ")

ssh_login_cmd = 'ssh -l {u} {h}'.format(u=username, h=hostname)

cli_handle = CliHandler(ssh_login_cmd)

print(cli_handle)

cli_handle.expect_data('password:')
cli_handle.send_data(password)
cli_handle.expect_data(username+'@')
cli_handle.send_data('touch abc.txt')
cli_handle.expect_data(username+'@')
cli_handle.send_data('ls abc.txt')
cli_handle.expect_data('abc.txt')
