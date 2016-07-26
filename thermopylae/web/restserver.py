# Implementation of a rest interface to the sockets
from http.server import SimpleHTTPRequestHandler

class RestServer(SimpleHTTPRequestHandler): 

    # sockets is a hash keyed by socket logical name (a string)
    # wieht each value consisting of a tuple of socket_driver and socket_id

    def do_GET(self):
        path = self.path
        partition = path.partition('/')
        # remove leading / in path
        thermometer_name = partition[2]
        #if the thermometer doesn't exist, send a 404
        if thermometer_name not in self.thermometers:
            self.send_error(404, "Thermometer not found: %s" % socket_name)
            return
        
        thermometer = self.thermometers[thermometer_name]
        reading = thermometer.read()
        if reading is None:
            temp = "-9999.0" # pysically impossible
        else:
            temp = str(reading)
        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(temp.encode("utf-8"))
        return
    
    
