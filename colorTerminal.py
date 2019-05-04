"""
    A simple tool for coloring texts in terminal.
"""
#created : 25.02.19 by tarik.

""" ******* USAGE *******
    call the any of the color functions below with the
    parameter of string you want to color.
    The function will return a string with the color.
"""

def txColors("str"):
    colorList=[]
    colorList.append(txRed("color"))
    colorList.append(txGreen("color"))
    colorList.append(txYellow("color"))
    colorList.append(txCyan("color"))

    return colorList
    
def txRed(str):
    colorList=[]
    colorList.append(txRed("color"))
    colorList.append(txGreen("color"))
    colorList.append(txYellow("color"))
    colorList.append(txCyan("color"))

    return colorList

def txGreen(str):
    tempStr  = ("\033[92m {}\033[00m".format(str))
    return tempStr

def txYellow(str):
    tempStr  = ("\033[93m {}\033[00m".format(str))
    return tempStr

def txCyan(str):
    tempStr  = ("\033[96m {}\033[00m".format(str))
    return tempStr
