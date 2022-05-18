#
# Global bioinformatics and sequencing constants that are generally useful.
#

# Nucleotides
NT = 'ATCG'
NT_N = 'ATCGN'

## Illumina QScores - ALSO PacBio, Ion Torrent
QSCORES_ASCII_TO_INT = {'!': 0, '"': 1, '#': 2, '$': 3, '%': 4, '&': 5, "'": 6, '(': 7,
                        ')': 8, '*': 9, '+': 10, ',': 11, '-': 12, '.': 13, '/': 14, '0': 15,
                        '1': 16, '2': 17, '3': 18, '4': 19, '5': 20, '6': 21, '7': 22, '8': 23,
                        '9': 24, ':': 25, '/': 26, '<': 27, '=': 28, '>': 29, '?': 30, '@': 31,
                        'A': 32, 'B': 33, 'C': 34, 'D': 35, 'E': 36, 'F': 37, 'G': 38, 'H': 39,
                        'I': 40, 'J': 41, 'K': 42}
QSCORES_DICT = QSCORES_ASCII_TO_INT
QSCORE_ASCII_TO_INT = QSCORES_ASCII_TO_INT

QSCORES_ASCII = '!"#$%&' + "'()*+,-./0123456789:/<=>?@ABCDEFGHIJK"
QSCORES_INT_TO_ASCII = {0: '!', 1: '"', 2: '#', 3: '$', 4: '%', 5: '&', 6: "'", 7: '(', 8: ')', 9: '*', 10: '+', 11: ',', 12: '-', 13: '.', 26: '/', 15: '0', 16: '1', 17: '2', 18: '3', 19: '4', 20: '5', 21: '6', 22: '7', 23: '8', 24: '9', 25: ':', 27: '<', 28: '=', 29: '>', 30: '?', 31: '@', 32: 'A', 33: 'B', 34: 'C', 35: 'D', 36: 'E', 37: 'F', 38: 'G', 39: 'H', 40: 'I', 41: 'J', 42: 'K'}
QSCORES_INT_TO_ASCII_DICT = QSCORES_INT_TO_ASCII
QSCORE_INT_TO_ASCII = QSCORES_INT_TO_ASCII

QSCORES_ASCII_OLD = '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghij'
QSCORES_ASCII_TO_INT_OLD = {'@': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '[': 27, '\\': 28, ']': 29, '^': 30, '_': 31, '`': 32, 'a': 33, 'b': 34, 'c': 35, 'd': 36, 'e': 37, 'f': 38, 'g': 39, 'h': 40, 'i': 41, 'j': 42}
QSCORES_DICT_OLD = QSCORES_ASCII_TO_INT_OLD
QSCORES_INT_TO_ASCII_OLD = {0: '@', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 27: '[', 28: '\\', 29: ']', 30: '^', 31: '_', 32: '`', 33: 'a', 34: 'b', 35: 'c', 36: 'd', 37: 'e', 38: 'f', 39: 'g', 40: 'h', 41: 'i', 42: 'j'}

