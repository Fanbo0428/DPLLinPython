# -*- coding = utf-8 -*-
import sys
import fileinput
import numpy as np
import cnf
import propparse
import rules
def check(cnf,model):
     cons=True#consistent set of literals
     empty=False#contains the empty clause
     for clause in cnf[1:]: # skip the "and"
         if len([var for var in clause[1:] if var in model]) == 0:
             cons=False
     modelComplements = rules.complements(model)
     for clause in cnf[1:]:
         if len([var for var in clause[1:] if var not in modelComplements]) == 0:
             empty=True
     if cons:
          return 'consistent'
     elif empty:
          return 'empty'

def dpll(cnf, model):
    if check(cnf,model)=='consistent':
         return model
    if check(cnf,model)=='empty':
         return False
    pure = rules.pureLiteralRuleOperation(cnf, model)
    if pure:
        return dpll(cnf, model + [pure])
    unit = rules.oneLiteralRuleOperation(cnf, model)
    if unit:
        return dpll(cnf, model + [unit])
    pick = rules.chooseLiteral(cnf, model)
    if pick:
        # try positive
        result = dpll(cnf, model + [pick])
        if result:
            return result
        else:
            #backtrack
            #print 'backtrack happen when dealing with' + cnf
            result = dpll(cnf, model + [['not', pick]])
            if result:
                return result
            else:
                return False

#main function starts here
inText = "".join(fileinput.input())
outList = propparse.parse(inText)
for l in outList:
     l = repr(l)
     l_cnf = repr(cnf.cnf(eval(l.strip())))
     inputClauses=eval(l_cnf.strip())
     standardinputClauses=cnf.standardize(inputClauses)
     #print standardinputClauses
     print dpll(standardinputClauses,[])
     
#########################this is for comparison with zChaff########################
# for l in sentences:
#      dpll(cnf.standardlize(l),[])  
#########################this is for comparison with zChaff######################## 