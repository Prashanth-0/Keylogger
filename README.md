# Keylogger with Remote Reporting


This is a simple Python keylogger that captures keystrokes and reports them remotely to a specified server. It can be used for educational purposes or as a part of a security testing toolkit. Please use responsibly and only on systems you have explicit permission to monitor.

## Features

- **Remote Reporting:** Captured keystrokes are sent to a remote server for monitoring.
  
- **Stealthy Operation:** The keylogger runs silently in the background without user detection.

- **Customizable Reporting Interval:** You can specify how often the captured keystrokes are sent to the server.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Prashanth-0/keylogger.git


1. **Set up the server:** Ensure you have a server running to receive the keystrokes. Update the ATTACKER_IP and ATTACKER_PORT variables in the keylogger.py script with the appropriate server IP address and port.

2. **Run the keylogger:** Execute the keylogger.py script on the target system you wish to monitor. The keylogger will start capturing keystrokes and sending them to the specified server.

3. **Receive keystrokes:** On the attacker machine, use netcat to listen for incoming connections on the specified port and receive the captured keystrokes.


## Requirements

- `Python 3.x`
- `Netcat utility`
- `Keyboard library (pip install keyboard)`


## Disclaimer
This tool is provided for educational purposes only. Misuse of this tool for unauthorized access to computer systems or networks is illegal and unethical. Use it responsibly and only on systems you have explicit permission to monitor.

