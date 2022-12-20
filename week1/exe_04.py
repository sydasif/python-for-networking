"""
4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
"""

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
show_version = show_version.split()
model = show_version[1]
serial_number = show_version[2]
has_cisco = 'Cisco' in model
has_881 = '881' in model
print(has_cisco)
print(has_881)
print(model, serial_number)