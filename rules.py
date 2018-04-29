#Implementation of rules applied in DPLL
def complements(model): # returns the complement of each model literal
    result = []
    for literal in model:
        if type(literal) is str:#if the literal is positive, it must be a string type
            result.append(["not", literal])
        elif literal[0] == 'not':#if the literal is negative, it is a list strat with 'not'
            result.append(literal[1])#add the original part into results
            #print '('+literal[1]+')'
    #print result
    return result
 
def pureLiteralRuleOperation(cnf, model): # finds a pure literal not already in model
    modelComplements = complements(model)
    candidates = []
    for clause in cnf[1:]:
        if len([var for var in clause[1:] if var in model]) == 0:
            # there is no literals in this clause occured in the current model
            # which means that the clause is not satisfied by the model yet.
            candidates = candidates + [var for var in clause[1:]]#they become candidates
    candidateComplements = complements(candidates)
    #occurs with only one polarity in the formula
    pureLiterals = [var for var in candidates if var not in candidateComplements]
    
    for literal in pureLiterals:
        if literal not in model + modelComplements:#The literal never added to the model before
            return literal
    return False

def oneLiteralRuleOperation(cnf, model): # finds one-literal not in model appearing by itself in a clause
    modelComplements = complements(model)
    for clause in cnf[1:]:
        remaining = [var for var in clause[1:] if var not in modelComplements]
        if len(remaining) == 1:
            if remaining[0] not in model:
                return remaining[0]
    return False

def chooseLiteral(cnf, model): 
    # finds a positive literal not in model or model complements
    for clause in cnf[1:]:
        for literal in clause[1:]:
            if type(literal) == str and literal not in model + complements(model):
                return literal
    return False