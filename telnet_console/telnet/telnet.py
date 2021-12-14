# Copyright (c) 2020 Viktor Vorobjov

try:
    import uos as os
    import uasyncio as asyncio
except ImportError:
    import os
    import asyncio


from .telnetio import TelnetIO


class TelnetServer:

    def __init__(self, pswd="micro"):

        self.pswd = pswd
        self.port = 23
        self.sw_client = None
        self.run = False



    async def server(self, reader, writer):

        addr = writer.get_extra_info('peername')
        print("+ from {}".format(addr))

        if self.sw_client:
            print("Close previous connection ...")
            self.close_dupterm()

        self.sw_client = TelnetIO(writer.s, self.pswd)
        self.sw_client.socket.setblocking(False)
        self.sw_client.socket.sendall(bytes([255, 252, 34]))  # dont allow line mode
        self.sw_client.socket.sendall(bytes([255, 251, 1]))  # turn off local echo
        os.dupterm(self.sw_client)

        print("Client connection ...")
        loop = asyncio.get_event_loop()
        loop.create_task(self.client_rx())

        await asyncio.sleep(1)




    # # On receiving client data
    async def client_rx(self):

        while True:
            if self.sw_client is not None:
                try:
                    asyncio.StreamReader(self.sw_client.socket)
                    os.dupterm_notify(True)  # dupterm_notify will somehow make a copy of sw_client
                except Exception as e:
                    print("Telnet client disconnected ... {}".format(e))
                    self.close_dupterm()
                await asyncio.sleep(0.5)
            else:
                await asyncio.sleep(1)

    def close_dupterm(self):

        if self.sw_client:
            self.sw_client.close()
            os.dupterm_notify(self.sw_client.socket)  # deactivate dupterm
            os.dupterm(None)
            self.sw_client = None


    def start(self, addr="0.0.0.0"):

        loop = asyncio.get_event_loop()
        if not self.run:
            loop.create_task(asyncio.start_server(self.server, addr, self.port))
            print("Telnet server started on {}:{}".format(addr, self.port))
            self.run = "{};{}".format(addr, self.port)
        else:
            print("Telnet server already on {}:{}".format(addr, self.port))

        return True



