import random

MAX_QUANTITY = 1000
MAX_SALES = 1000000 # 10000.00

def getRandomQuantity():
    return random.randint(1,MAX_QUANTITY)

def getRandomSales():
    return round(random.random() * MAX_SALES,2)

def getRandomDiscount():
    return random.randint(0,1)

def pickRandomElement(elements):
    size = len(elements)
    randm = random.randint(0,size-1)
    return elements[randm]

# Adds or subtract a random value to the original sales value, proportional to a maximum given percentage value
def addRandomDelta(original, maxPerc):
    # Generates a random value
    randm = random.random()
    
    # Generates a random percentage value in range 0-maxPerc
    randomPerc = random.randint(0,maxPerc)
    
    # Calculates the delta from the previous sales value
    delta = (original / 100) * randomPerc
    
    randm *= delta
    
    # Randomly set the sign
    sign = random.randint(0,2)
    if sign > 1:
        randm *= -1
    
    withDelta = original + randm;
    
    return withDelta