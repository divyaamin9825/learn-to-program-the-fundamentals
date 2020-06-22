def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(potential_dna):
    '''(str) -> bool

    Returns True if and only if potential DNA sequence potential_dna is valid.
    
    >>> is_valid_sequence('AGCTAC')
    True
    >>> is_valid_sequence('AGCTAC1')
    False
    >>> is_valid_sequence('atcga')
    False
    >>> is_valid_sequence('AGCTACS')
    False
    >>> is_valid_sequence('')
    True
    '''
    pot_dna_validity = False
    result = ''
    if potential_dna == '':
        pot_dna_validity = True
    else:
        for s in potential_dna:
            if s in "ATCG":
               result = result + s
            else:
                pot_dna_validity =  False
    if result == potential_dna:
        pot_dna_validity = True
    return pot_dna_validity

def insert_sequence(dna1, dna2, index):            
    '''(str, str, int) -> str
    Inserts DNA sequence dna2 into DNA sequence dna1 at the position
    specified by index.

    Prerequisite: 0 <= index < len(dna1)
    >>> c
    'CCATGG'
    >>> insert_sequence('TCATG','T', 4)
    'TCATGT'
    >>> insert_sequence('CATGT','T', 0)
    'TCATGT'
    >>> insert_sequence('TATACGAG', 'AT', 0)
    'ATTATACGAG'
    >>> insert_sequence('TACGAG', 'AT', 5)
    'TACGAGAT'
    '''
    i = 0
    result = ''
    if index == (len(dna1)-1):
        result = dna1 + dna2
    else:
        for char in dna1:
            if i == index:
                result = result + dna2 
            result = result + char
            i = i + 1
    return result

def get_complement(nuc):
    '''(str) -> str

    Return the complement of nucleotide nuc.
    
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    '''
    complement = ''
    if nuc == 'A':
       complement = complement + 'T'
    elif nuc == 'T':
        complement = complement + 'A'
    elif nuc == 'C':
        complement = complement + 'G'
    elif nuc == 'G':
        complement = complement + 'C'
    return complement

def get_complementary_sequence(dna):
    '''(str) -> str
    Returns the DNA sequence that is complementary to DNA sequence dna.
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    >>> get_complementary_sequence('TCATGT')
    'AGTACA'
    '''
    complement_dna = ''
    for char in dna:
        complement_dna = complement_dna + get_complement(char)
    return complement_dna
