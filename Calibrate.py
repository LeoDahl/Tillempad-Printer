## Code made by Leo Dahl
## Latest Change was made 2025-02-07 22:21


from SerialConnector import RunCommand

## While loop makes code never stop
while True:
    print("Command:")
    Command = input()
    RunCommand(Command) ## Runs function RunCommand