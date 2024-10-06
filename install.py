import subprocess
subprocess.call("sudo apt install python3-venv", shell=True)
subprocess.call("python3 -m venv .venv", shell=True)
subprocess.call("source .venv/bin/activate", shell=True)
subprocess.call("pip install os-sys", shell=True)
subprocess.call("pip install colorama", shell=True)
subprocess.call("pip install fore", shell=True)
subprocess.call("apt install -y aircrack-ng ", shell=True)