#!/usr/bin/python3

import cherrypy
import serial
import time


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    def runCommand(self,cmd):
        ser = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', baudrate=9600, bytesize=8, parity='N')
        ser.write(bytes(cmd, 'UTF-8'))
        time.sleep(1)
        out=""
        while ser.inWaiting() > 0:
          out += ser.read(1).decode('utf-8')
        ser.close()
        return out

    @cherrypy.expose
    def open(self, hub='001', device=None):
        return self.runCommand('!' + hub + 'D' + device + 'o?;')

    @cherrypy.expose
    def close(self, hub='001', device=None):
        return self.runCommand('!' + hub + 'D' + device + 'c?;')

    @cherrypy.expose
    def percent(self, hub='001', device=None, percent=None):
        cmd='!' + hub + 'D' + device + 'm' + percent + ';'
        print(cmd)
        return self.runCommand(cmd)

    @cherrypy.expose
    def position(self, hub='001', device=None):
      resp = self.runCommand('!' + hub + 'D' + device + 'r?;')
      if resp != '':
        print(resp)
        if resp[12] is not 'b':
          return resp[9:11]
        else:
          return "100"

    @cherrypy.expose
    def batt(self, hub='001', device=None):
      resp = self.runCommand('!' + hub + 'D' + device + 'pVc?;')
      if resp != '':
        return str(int(resp[11:16])/100)

    @cherrypy.expose
    def toggle(self, hub='001', device=None):
      resp = self.runCommand('!' + hub + 'D' + device + 'r?;')
      if resp != '':
        if resp[12] is not 'b':
          if int(resp[9:11]) <= 50:
            return self.runCommand('!' + hub + 'D' + device + 'c?;')
          else:
            return self.runCommand('!' + hub + 'D' + device + 'o?;')
        else:
          return self.runCommand('!' + hub + 'D' + device + 'o?;')


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
    cherrypy.quickstart(StringGenerator())
