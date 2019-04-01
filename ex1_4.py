#!/usr/bin/env python
"""Create a show_version variable that contains the following

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
"""

from __future__ import print_function
show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
show_version=show_version.strip()
[dummy,model,serial]=show_version.split()
print("Is model Cisco? : {}".format("cisco" in model.lower()))
print("Is model 881? : {}".format("881" in model.lower()))
print("Model : {}".format(model.upper()))
print("Serial : {}".format(serial.upper()))
