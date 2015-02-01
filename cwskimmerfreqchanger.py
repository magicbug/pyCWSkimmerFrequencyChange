import sys, telnetlib, sched, time

# Telnet Connection Information
HOST = "localhost"
user = "m3php"

# Set Default Frequency (should always be zero)
frequency = "0"

# Define the Scheduler
s = sched.scheduler(time.time, time.sleep)

def connction():
    global tn


def do_something(sc):
    global frequency

    count = 0
    while (count is 0):
        try:
            # Connect to telnet
            tn = telnetlib.Telnet(HOST, '7300')

            # Wait till CW Skimmer Telnet Server Asks for Callsign
            tn.read_until("Please enter your callsign:")
            tn.write(user + "\n") # send the callsign

            print "Connected to CW Skimmer\n"
            count = 1
        except:
            print "Connection to CW Skimmer Failed\n"
            count = 0

    # QSY frequency
    if frequency is '0':
        tn.write("skimmer/qsy 1830.0\n")
        frequency = "1830.0"
    elif frequency is '1830.0':
        tn.write("skimmer/qsy 3525.0\n")
        frequency = "3525.0"
    elif frequency is '3525.0':
        tn.write("skimmer/qsy 7025.0\n")
        frequency = "7025.0"
    elif frequency is '7025.0':
        tn.write("skimmer/qsy 10120.0\n")
        frequency = "10120.0"
    elif frequency is '10120.0':
        tn.write("skimmer/qsy 14025.0\n")
        frequency = "14025.0"
    elif frequency is '14025.0':
        tn.write("skimmer/qsy 18080.0\n")
        frequency = "18080.0"
    elif frequency is '18080.0':
        tn.write("skimmer/qsy 21025.0\n")
        frequency = "21025.0"
    elif frequency is '21025.0':
        tn.write("skimmer/qsy 24900.0\n")
        frequency = "24900.0"
    elif frequency is '24900.0':
        tn.write("skimmer/qsy 28025.0\n")
        frequency = "28025.0"
    elif frequency is '28025.0':
        tn.write("skimmer/qsy 1830.0\n")
        frequency = "1830.0"

    print "QSY: " + frequency

    # Run scheduler every 120 seconds
    sc.enter(120, 1, do_something, (sc,))

connction()
print "CW Skimmer Band Change Automation Script\n"
s.enter(0, 1, do_something, (s,)) # Run at second 0
s.run() # run the scheduler
