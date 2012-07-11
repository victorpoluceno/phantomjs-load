import SimpleHTTPServer
import SocketServer
import threading

PORT = 8000


def main():
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(('', PORT), Handler)

    print "serving at port", PORT
    threading.Thread(target=httpd.serve_forever).start()


if __name__ == '__main__':
    main()