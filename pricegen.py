import sys, getopt

from it.istat.prezzi.gen.model.PV import PV
from it.istat.prezzi.gen.Generator import generateEanCodes, generateSequence
from it.istat.prezzi.gen.RandomStuff import getRandomDiscount,getRandomQuantity,addRandomDelta

NUMBER_OF_WEEKS = 104
EANCODES_PER_IDPV = 0

HEADER = "IDPV,TIMESTAMP,EANCODE,QUANTITY,SALES,SC\n"

# Generate a set of rows for a given list of pvs, randomly adds or subtract a 10% of the base sales value
def buildRowsForPV(pvs,week):
    global EANCODES_PER_IDPV
    
    rows = ""
    
    for pv in pvs:        
        for eancode in pv.eancodes.keys():
            idpv = pv.idpv
            timestamp = str(week)           
            quantity = getRandomQuantity()
            sales = pv.eancodes[eancode]                        # Get the original base price
            sales = round(addRandomDelta(sales, 10),2)          # Adds or substract 10%
            pv.eancodes[eancode] = sales                        # Saves in the dict for future
            discount = getRandomDiscount()

            rows += str(idpv)+","+timestamp+","+str(eancode)+","+str(quantity)+","+str(sales)+","+str(discount)+"\n"

    return rows
    
def usage():
    print ("Usage: \n")
    print ("pricegen --ofile <OUTPUTFILE> --pvn <NUMBER OF PV> --ecppv <EANCODES PER PV>")


def main(argv):
    global EANCODES_PER_IDPV
    
    OUTPUT_FILE = ""
    NUMBER_OF_IDPV = 0
    
    try:
        opts, args = getopt.getopt(argv,"",["ofile=","pvn=","ecppv="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if (len(opts) != 3):
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--ofile':
            OUTPUT_FILE = arg
        elif opt == ("--pvn"):
            NUMBER_OF_IDPV = int(arg)
        elif opt == ("--ecppv"):
            EANCODES_PER_IDPV = int(arg)

    print ("Output file is: ", OUTPUT_FILE)
    print ("Number of PV is: ", NUMBER_OF_IDPV)
    print ("EANCODES for PV is: ", EANCODES_PER_IDPV)
    
    totalEanCodes = generateEanCodes()
    idpvList = generateSequence(NUMBER_OF_IDPV)
    
    pvs = []
    
    # Generates a list of PV (sales point) object with a map of idpv <-> base sales
    for idpv in idpvList:
        pv = PV(idpv, totalEanCodes, EANCODES_PER_IDPV)
        pvs.append(pv)
   
    outputfile = open(OUTPUT_FILE, "w")
    
    outputfile.write(HEADER)
    
    totalRows = NUMBER_OF_IDPV * EANCODES_PER_IDPV * NUMBER_OF_WEEKS
    
    counter = 0;
   
    for week in range(NUMBER_OF_WEEKS):
        rows = buildRowsForPV(pvs,week)
        outputfile.write(rows)
        counter += EANCODES_PER_IDPV * NUMBER_OF_IDPV
        print ("Wrote "+str(counter)+" rows of "+str(totalRows))
    
    outputfile.close()    

if __name__ == '__main__':    
    main(sys.argv[1:])
    