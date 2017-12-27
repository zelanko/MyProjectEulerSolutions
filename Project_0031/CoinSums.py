"""Coin sums
Problem 31 (https://projecteuler.net/problem=31)

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general
circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?"""

productions = {
    '200': (200, ('100', '100')),
    '100': (100, ('50', '50')),
    '50': (50, ('20', '20', '10')),
    '20': (20, ('10', '10')),
    '10': (10, ('5', '5')),
    '5': (5, ('2', '2', 1)),
    '2': (2, (1, 1))
}

class SymbolTuple:
    """Represents the set of terminals and non-terminals in the 'productions' grammar."""
    def __init__(self, symbols)
        terminals = []
        non_terminals = []
        for s in symbols:
            t = type(s)

            if t == int:
                terminals.append(s)
            elif t == str:
                non_terminals.append(s)
            else:
                raise f"Unsupported symbol type {t}"                

        self.terminals = tuple(sorted(terminals))
        self.non_terminals = tuple(sorted(non_terminals))


    def derive(self):
        self.terminals + self.non_terminals
        

inputs = {SymbolTuple(['200'])}
outputs = set()

while len(inputs) > 0: 
    for p in inputs.pop():
        if is_terminal(p):
        for x in productions[p]:
            if type(x) == int:
                outputs.add((x))
            elif type(x) == tuple:
                tuple_expansion = []
                for y in x:
                    

            else:
                raise Exception(f"Unexpected input type {type(x)}")
    
    outputs.remove(production)


