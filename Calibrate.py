##  File: Calibrate.py
##  Author: Leo Dahl
## Date: 2025-02-07
##  Simple command prompter which runs commands via RunCommand() function
##  
##

from SerialConnector import RunCommand

## While loop makes code never stop
while True:
    print("Command:")
    Command = input()
    RunCommand(Command) ## Runs function RunCommand
