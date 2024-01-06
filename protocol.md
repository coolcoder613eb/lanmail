# Lan Mail Protocol
## Connection
### Request (client)
```
AUTH USER <username>
AUTH PASSWD <password>
```
### Response (server)
Valid:
```
AUTH ACCEPTED
```
Invalid:
```
AUTH REJECTED
```
### Response (server) (If new messages for client)
## Send
### Request (client)
```
SEND <message length in bytes>
<message content>
TO <user>
```
### Response (server)
Success:
```
SEND OK
```
Failure:
```
SEND FAILED
```
## Receive
### If the target is connected to the server:
#### Message (server)
```
NEW
```
### When the client receives NEW:
#### Request (client)
```
GET
```
#### Response (server)
For each message server has for client 
```
HAVE <message id>
```
#### Response (client)
##### If client has a message with that id
```
HAVE YES
```
Server then goes to next message
##### If client does not have a message with that id
```
HAVE NO
```
##### Response (server)
```
MESSAGE <message id>
SIZE <message length in bytes>
<message content>
FROM <user>
TO <user>
TIME <timestamp>
```
