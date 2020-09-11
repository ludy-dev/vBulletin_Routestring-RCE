# [CVE-2019-16759]vBulletin_Routestring-RCE-PoC
A vulnerability has been discovered in vBulletin which could allow for remote code execution when a malicious POST request is sent to the vulnerable application. 
The vulnerability is due to an input validation error while parsing a HTTP request in the vulnerable module. 

System Affected : 

vBulletin Version 5.0.0 ~ 5.5.4 
(Updated System affected) vBulletin Version 5.0.0 ~ 5.6.2

[Usage]

(User defined port) python vBulletin_Routestring-RCE.py <dst_ip> <dst_port>

(default Port:80)   python vBulletin_Routestring-RCE.py <dst_ip>

Script based on Python2
Not For attack. just using Vuln Test for your System
