# Rollease_web
Rollease Acmeda Automate Pulse hub web controler


* /usr/bin/curl http://localhost:8080/close?device=001
* /usr/bin/curl http://localhost:8080/open?device=001
* /usr/bin/curl http://localhost:8080/position?device=001
* /usr/bin/curl http://localhost:8080/percent?device=001&percent=54
* /usr/bin/curl http://localhost:8080/batt?device=001
* /usr/bin/curl http://localhost:8080/toggle?device=001


toggle reads the shade position. iIf the shade position is >=50 the shade is opened otherwise the shade is closed.

hub can be set but defaults to 001

* /usr/bin/curl http://localhost:8080/close?hub=001&device=001

Hardware hookup directions for this code is the same as this project's: https://github.com/quentinsf/rollease2mqtt/tree/master/rollease2mqtt

This is a very basic implimentatin you should probably use somthing like this instead: https://github.com/quentinsf/rollease2mqtt

