from http.server import BaseHTTPRequestHandler, HTTPServer
import pika


# HTTP server host and port
hostName = 'localhost'
serverPort = 8080


# Pika connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='views')


# Create the HTTP server
class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Nexiona</title><link rel="shortcut icon" href="data:image/x-icon;,''" type="image/x-icon"></head>', "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<div><h1>Menu</h1></div>", "utf-8"))
        self.wfile.write(bytes('<ul><li><a href="http://localhost:8080/page1">Page 1</a></li>', "utf-8"))
        self.wfile.write(bytes('<li><a href="http://localhost:8080/page2">Page 2</a></li>', 'utf-8'))
        self.wfile.write(bytes('<li><a href="http://localhost:8080/page3">Page 3</a></li>', 'utf-8'))
        self.wfile.write(bytes('<li><a href="http://localhost:8000/views">Views by url</a></li>', 'utf-8'))
        self.wfile.write(bytes('<li><a href="http://localhost:8000/total_views">Total Views</a></li>', 'utf-8'))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        # Send the url and id to Rabbit MQ
        body = self.client_address[0] + self.path
        channel.basic_publish(exchange='', routing_key='views', body=body)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")