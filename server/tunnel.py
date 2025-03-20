import ngrok
import time

# Establish connectivity
listener = ngrok.forward(9000, authtoken_from_env=False)

# Output ngrok url to console
print(f"Ingress established at {listener.url()}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing listener")