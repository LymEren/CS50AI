# This project includes knights puzzle solution

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    Or(AKnight, AKnave), # A is knight or knave
    Not(And(AKnight, AKnave)), # but it is not both at the same time

    Implication(AKnight, And(AKnight,AKnave)),  # if A is a knight his sentence must be true
    Implication(AKnave, Not(And(AKnight,AKnave))) # And if A is a knave his sentence must be false
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    Or(AKnight, AKnave), # A and B are either knights or knaves but not both
    Or(BKnight, BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),

    Implication(AKnight, And(AKnave, BKnave)), # if A is a knight both A and B are knaves
    Implication(AKnave,Not(And(AKnave, BKnave))) # if A is a knave his statement is false
)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # A and B are either knights or knaves but not both
    Or(AKnight, AKnave), 
    Or(BKnight, BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight, BKnave)),
    
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))), # if A is a knight A and B are of the same kind

    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))), # if A is a knave his statement is false

    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))), # if B is a knight A and B are of different kinds

    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave,BKnight))))  # if B is a knave his statement is false
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
    # A, B, C are either knights / or knaves / but not both
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # if B is a knight, A statement is false / and C is a knave
    Implication(BKnight, And(
        Implication(AKnight, AKnave),
        Implication(AKnave,Not(AKnave)),
        CKnave
    )),

    # if B is a knave, A statement is true / and C is not a knave
    Implication(BKnave, And(
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight)),
        Not(CKnave)
    )),
    
    Implication(CKnight, AKnight), # if C is a knight A is a knight

    Implication(CKnave,Not(AKnight)) # if C is a knave A is not a knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
