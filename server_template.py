import socket

# ----------------------------------------------------------------------------

BUFFSIZE = 1024

def send_message(socket: socket.socket, message = "Mensaje default"):
  raw_message = message.encode("utf-8")
  socket.sendall(raw_message)
  address = socket.getsockname()
  print("========================================================")
  print(f"Sent: '{message}' to {address[0]}:{address[1]}")

def recv_message(socket: socket.socket) -> str:
  raw_message = socket.recv(BUFFSIZE)
  message = raw_message.decode("utf-8")
  address = socket.getpeername()
  print("========================================================")
  print(f"Received: '{message}' from {address[0]}:{address[1]}")
  return message

def handle_client(client_socket,client_address):
  print("========================================================")
  print(f"Connection accepted from {client_address[0]}:{client_address[1]}")
  with client_socket:
    # ----------------------------------------------------
    # CODIGO PRINCIPAL
    # ----------------------------------------------------
    request = recv_message(client_socket)
  
    response = "Message from the server"

    send_message(client_socket,response)

    # ----------------------------------------------------

# ----------------------------------------------------------------------------

def main():
  server_address = ("localhost",5000)
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    try:

      server_socket.bind(server_address)
      server_socket.listen(4)

      print(f"Listening at {server_address[0]}:{server_address[1]}")
      while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket,client_address)

    except KeyboardInterrupt:
      print("\nExiting")

    except Exception as err:
      print(f"Aborting: {err}")

if __name__ == "__main__":
  main()
  