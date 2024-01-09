import socket
import time

# Server address and port
SERVER_ADDRESS = "localhost"
SERVER_PORT = 1865

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))


def send_message(message):
    client_socket.sendall((message + "\n").encode())


def receive_response():
    return client_socket.recv(1024).decode()


print("send auth")
# Authentication
send_message("AUTH USER admin")
# response = receive_response()
# print(f"Server Response: {response}")
print("sent")
send_message("AUTH PASSWD password")
response = receive_response()
print(f"Server Response: {response}")

# Sending a message
send_message("SEND 15\nHello, server!\nTO admin")
response = receive_response()
print(f"Server Response: {response}")

# Simulate checking for new messages
time.sleep(1)
send_message("GET")
response = receive_response()
print(response)
if "HAVE" in response:
    # Assume there is a message with ID 0
    send_message("HAVE YES")
    response = receive_response()
    if "MESSAGE" in response:
        # Process the message
        print(response)
    else:
        print("Invalid response when fetching the message.")
elif "NO" in response:
    print("No new messages.")

# Close the connection
client_socket.close()
