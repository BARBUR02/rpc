## Project utilizing RPC approach
## First App - gRPC server with gRPC web client in React
gRPC demands client/server to use HTTP2.0 protocol for communication exchange. Due to that, it is mandatory to use proxy in gRPC-Web approach. 
Here I am using envoy proxy to redirect calls between backend and frontend on local server. This process runs in docker container, In order to 
start it run:
```
docker compose up
```
in `client` directory
For backend, run:
```
python server.py
```
in `server` directory
for browser client, run:
```
npm run dev
```
in `client` directory
## Second App - presentation of dynamic invocation utilizing Zeroc Ice
Server is created in python, witch Java client. Working example is with calculator interface, for the other one i was testing node client however it didn't work 
with dynamic invocation in my case. Leaving for reference :).
