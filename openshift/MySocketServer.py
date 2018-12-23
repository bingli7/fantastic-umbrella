from SocketServer import ( TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    # re-write handle()
    def handle(self):
        print 'Connected from: ', self.client_address
        self.wfile.write('[%s]  %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)

print 'Waiting for connecttion...'
tcpServ.serve_forever()