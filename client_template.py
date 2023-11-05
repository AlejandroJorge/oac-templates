import socket
import time
# ----------------------------------------------------------------------------

BUFFSIZE = 1024

def send_message(socket: socket.socket, message = "Mensaje default"):
  raw_message = message.encode("utf-8")
  socket.sendall(raw_message)
  print("========================================================")
  print(f"Sent: {message}")

def recv_message(socket: socket.socket) -> str:
  raw_message = socket.recv(BUFFSIZE)
  message = raw_message.decode("utf-8")
  print("========================================================")
  print(f"Received: {message}")
  return message


def handle_connection(client_socket):

  # ----------------------------------------------
  # CODIGO PRINCIPAL
  # ----------------------------------------------
  request = "Message from the client"
  send_message(client_socket,request)
  response = recv_message(client_socket)
  # ----------------------------------------------

# ----------------------------------------------------------------------------

if __name__ == "__main__":
  
  server_address = ("localhost",5000)
  
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)

    handle_connection(client_socket)

    