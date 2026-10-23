from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>Device Specifications</title>
</head>
<body>
    <table>
        <caption>Device Specifications</caption>
        <tr>
            <th>s.no</th>
            <th>feature</th>
            <th>specification</th>
        </tr>
         <tr>
            <td>1</td>
                <td>Operating System</td>
                <td>Windows 11 Home</td>
            </tr>
        <tr>
            <td>2</td>
            <td>Processor</td>
            <td>Intel Core 5 </td>
        </tr>
        <tr>
            <td>3</td>
            <td>Memory</td>
            <td>16 GB DDR5</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Storage</td>
            <td>512 GB SSD</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Battery</td>
            <td>55.2 Whr</td>
        </tr>
       
    </table>
</body>
</html>

"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()