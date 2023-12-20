
# table of probabilities for each letter...
def letProb( c ):
    """ if c is the space character or an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    https://en.wikipedia.org/wiki/Letter_frequency
    """
    if c == 'e' or c == 'E': return 0.12782
    if c == 't' or c == 'T': return 0.09056
    if c == 'a' or c == 'A': return 0.08167
    if c == 'o' or c == 'O': return 0.07507
    if c == 'i' or c == 'I': return 0.06966
    if c == 'n' or c == 'N': return 0.06749
    if c == 's' or c == 'S': return 0.06327
    if c == 'h' or c == 'H': return 0.06094
    if c == 'r' or c == 'R': return 0.05987
    if c == 'd' or c == 'D': return 0.04253
    if c == 'l' or c == 'L': return 0.04025
    if c == 'c' or c == 'C': return 0.02782
    if c == 'u' or c == 'U': return 0.02758
    if c == 'm' or c == 'M': return 0.02406
    if c == 'w' or c == 'W': return 0.02360
    if c == 'f' or c == 'F': return 0.02228
    if c == 'g' or c == 'G': return 0.02015
    if c == 'y' or c == 'Y': return 0.01974
    if c == 'p' or c == 'P': return 0.01929
    if c == 'b' or c == 'B': return 0.01492
    if c == 'v' or c == 'V': return 0.00978
    if c == 'k' or c == 'K': return 0.00772
    if c == 'j' or c == 'J': return 0.00153
    if c == 'x' or c == 'X': return 0.00150
    if c == 'q' or c == 'Q': return 0.00095
    if c == 'z' or c == 'Z': return 0.00074
    return 1.0