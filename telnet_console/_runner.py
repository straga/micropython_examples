
from .telnet import TelnetServer


class Runner():

    async def _activate(self, port, pswd):

        self.telnet = TelnetServer()
        self.telnet.port = port
        self.telnet.pswd = pswd
        self.telnet.start()
