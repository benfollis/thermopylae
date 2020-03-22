# Implementation of a rest interface to the sockets
from http.server import SimpleHTTPRequestHandler
import json


class RestServer(SimpleHTTPRequestHandler):

    # sockets is a hash keyed by socket logical name (a string)
    # wieht each value consisting of a tuple of socket_driver and socket_id

    def do_GET(self):
        path = self.path
        partition = path.partition('/')
        # remove leading / in path
        thermometer_name = partition[2]

        result = self.handle_request(thermometer_name)
        encoded = json.dumps(result)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(encoded.encode("utf-8"))
        return

    def handle_request(self, thermometer_name):
        # if thermometers doesn't exist send a 404
        if self.thermometers is None:
            self.send_error(404, "No thermometers: %s" % thermometer_name)
        # special case discovery
        if thermometer_name == 'discovery':
            return self.do_discovery()
        # if the thermometer doesn't exist, send a 404
        if thermometer_name not in self.thermometers:
            self.send_error(404, "Thermometer not found: %s" % thermometer_name)
            return
        return self.do_read(thermometer_name)

    def do_read(self, thermometer_name):
        thermometer = self.thermometers[thermometer_name]
        reading = thermometer.read()
        return {'temperature': reading,
                'unit': 'C'}

    def do_discovery(self):
        return list(self.thermometers.keys())
