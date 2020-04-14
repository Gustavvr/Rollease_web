# Rollease_web
Rollease Acmeda Automate Pulse hub web controler


* /usr/bin/curl http://localhost:8080/close?device=001
* /usr/bin/curl http://localhost:8080/open?device=001
* /usr/bin/curl http://localhost:8080/position?device=001
* /usr/bin/curl http://localhost:8080/percent?device=001&percent=54
* /usr/bin/curl http://localhost:8080/batt?device=001
* /usr/bin/curl http://localhost:8080/toggle?device=001


toggle reads the shade position. iIf the shade position is >=50 the shade is opened otherwise the shade is closed.
