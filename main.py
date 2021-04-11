import http.server as server
from urllib.parse import urlparse, parse_qs
from search_rows import get_rows
import json


class ApiHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/javascript')
        self.end_headers()
        params = parse_qs(urlparse(self.path).query)
        print(params)
        response = tuple(i.strip().split(',')
                         for i in get_rows(params['sku'][0]))
        response = tuple({'sku': i[0], 'rank': float(i[1])} for i in response if (
            'ge' not in params) or (float(i[1]) >= float(params['ge'][0])))
        response = json.dumps({'sku_recom': response})
        self.wfile.write(bytes(response, 'utf-8'))


def run(server_class=server.HTTPServer, handler_class=ApiHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
