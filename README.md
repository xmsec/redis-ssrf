# redis-ssrf
1. ssrf to write files. eg: webshell and ssh key
2. ssrf to rce 3.x - 5.x

## Requirements
ssrf-redis.py :  python2.x 3.x 

rogue-server.py :  python2.x  (lazy

## Usage
implememt for demo.

plz read generate_payload function and change payload.

for rce usage:

1. change lhost, lport and command, then    
`> python ssrf-redis.py`    
`> gopher://xxxxx`     

2. triger ssrf

3. meanwhile on vps    
`> python rogue-server.py`   
`> Accepted connection from 192.168.x.x`

(Need to compile a module named exp.so at first or download other's and store it with rogue-server.py)
## Reference
Inspired by https://github.com/n0b0dyCN/redis-rogue-server

Also, modified from https://xz.aliyun.com/t/5665

