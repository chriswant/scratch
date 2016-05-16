#!/usr/bin/python3

import time
#import RPi.GPIO as GPIO

class AcUnit:
    "AC unit state"
    __id = 0
    __in = 0
    __out = 0
    __value = 0
    __on = 0.0
    __off = 0.0

    def __init__(self, ident, pin_in, pin_out, v = 0):
        self.__id = ident
        self.__in = pin_in
        self.__out = pin_out
        self.setVal(v)

    # query state
    def isOn(self):
        return self.__value > 0
    def isOff(self):
        return not self.isOn()
    def getOut(self):
        return self.__out
    def getIn(self):
        return self.__in
    def getVal(self):
        return self.__value
    def getId(self):
        return self.__id
    def getElapsed(self):
        if self.isOn():
            return time.time() - self.__on
        else:
            return time.time() - self.__off

    # change state
    def setVal(self, v):
        if v > 0:
            self.setTimeOn()
        elif v == 0:
            self.setTimeOff()
        self.__value = v
    def setTimeOn(self):
        self.__off = 0
        self.__on = time.time()
    def setTimeOff(self):
        self.__on = 0
        self.__off = time.time()

def state(series):
    print("State:", ['On' if ac.isOn() else 'Off' for ac in series])

def main():
    "Example usage"

    timeout = 2.5

    # initialize objects
    units = [AcUnit(1, 17, 5, 0), AcUnit(2, 27, 6, 5), AcUnit(3, 22, 13, 9)]
    state(units)
    print("Sum: ", sum(v.getVal() for v in units), '\n')

    print("Sleeping for {0} seconds...\n".format(timeout))
    time.sleep(timeout)

    print("Timer states:")
    for ac in units:
        msg = "Time on (ID: {0:d}): " if ac.isOn() else "Time off (ID: {0:d}): "
        msg += "{1:03.3f} secs"
        print(msg.format(ac.getId(), ac.getElapsed()))

        print("Pin (input): {0}; Pin (output): {1}\n".format(ac.getIn(), ac.getOut()))

if __name__ == "__main__":
    main()

