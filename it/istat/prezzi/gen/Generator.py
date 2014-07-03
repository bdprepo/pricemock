# The size of the global eancodes list, used to randomly picking eancodes for every PV
EANCODE_MAX = 30000      # Will be around 300000

def generateSequence(max_value):
    elements = []
    
    digits = len(str(max_value))
    
    for i in range(max_value):
        elements.append(str(i).zfill(digits))
    return elements

def generateEanCodes():
    eancodes = generateSequence(EANCODE_MAX)
    return eancodes
