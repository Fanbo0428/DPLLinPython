# pythonDPLL
This is a Python implementation of DPLL algorithm for SAT problems.

# The code consists of three parts:

1.propparse.py(from Andrew S. Gordon), it turns the input lisp format string to the Python list format indicating the input clauses.

2.cnf.py is modified from the original version of Andrew S. Gordon's cnf.py, it takes the output of propparse.py as input and output the cnf format(standlized) input clauses for DPLL algorithm

3.dpll.py is implemented depends on the previous two files(you can see the 'import' code at the head of the file). It is implemented according to the algorithm described in ISO-report. 

# To run this code, type cat test.lisp | python dpll.py in terminal and you will see the result.
