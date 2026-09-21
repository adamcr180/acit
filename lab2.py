KB = 1024
MB = 1048576
GB = 1073741824

num_entries = input("Please enter the number of entries per second:      ")
entry_size = input("Please enter the average number of bytes per entry:     ")


bps = (int(num_entries) * int(entry_size))

bpm = bps * 60
kbpm = bpm /KB
bph = bps * 3600
mbph= bph / MB
gbpd = (bph * 24) / GB
print("Storage Estimates")
print(f"Per minute: {kbpm} KB")
print(f"Per hour: {mbph} MB")
print(f"Per day: {gbpd} GB")

#1. Read (using the input() function) the number of log entries per second
#2. Read (using the input() function) the average size of a log entry in bytes
#3. Display:
#a) The storage required for 1 minutes worth of log entries, in KB
#b) The storage required for 1 hours worth of log entries, in MB
#c) The storage required for 1 days worth of log entries, in GB

#To finish the assignment, complete the following tasks:

#- Correct the error(s) in the provided code
#- Implement the remaining functionality 