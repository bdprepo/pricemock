'''
Created on 25/giu/2014

@author: lorenzo.digaetano
'''

from it.istat.prezzi.gen.RandomStuff import getRandomSales,pickRandomElement

class PV(object):
    '''
        Object representing a single Sales Point (PV)
        Keeps a list of eancodes assigned to this PV, randomly picked by a given list and generates
        a base value for every eancode sales value
    '''
    def buildBasePrices(self):
        
        for i in range(self.numberOfEanCodesPerPv):
            eancode = pickRandomElement(self.totalEancodes)
            sales = getRandomSales()
            self.eancodes[eancode] = sales
    
    def __init__(self, idpv, totalEancodes, numberOfEanCodesPerPv):
        '''
        Constructor
        '''
        self.idpv = idpv
        self.totalEancodes = totalEancodes
        self.numberOfEanCodesPerPv = numberOfEanCodesPerPv
        self.eancodes = {}
        self.buildBasePrices()
        