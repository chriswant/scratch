#!/usr/bin/python3

from acunits.ac import AcUnit

ac = AcUnit("AC1", 5, 75)

print(ac.getId() + " is on" if ac.isOn() else ac.getId() + " is off")

