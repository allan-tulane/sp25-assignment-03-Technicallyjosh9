import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    else:
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):  #From lecture notes
    if (S, T) in MED:
        return MED[(S, T)]

    if not S:
        return len(T)
    if not T:
        return len(S)

    if S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED) + 1
        delete = fast_MED(S[1:], T, MED) + 1

        MED[(S, T)] = min(insert, delete)

    return MED[(S, T)]


def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
        
    if not S:
        align = ('-' * len(T), T)
        MED[(S, T)] = align
        return align
    if not T:
        align = (S, '-' * len(S))
        
        MED[(S, T)] = align
        return align
        
    if S[0] == T[0]:
        
        AS, AT = fast_align_MED(S[1:], T[1:], MED)
        align = (S[0] + AS, T[0] + AT)
        MED[(S, T)] = align
        return align
        
    else:
        insert = fast_MED(S, T[1:])
        delete = fast_MED(S[1:], T)
        if insert <= delete:
            AS, AT = fast_align_MED(S, T[1:], MED)
            align = ('-' + AS, T[0] + AT)
        else:
            AS, AT = fast_align_MED(S[1:], T, MED)
            align = (S[0] + AS, '-' + AT)
        MED[(S, T)] = align
        return align

