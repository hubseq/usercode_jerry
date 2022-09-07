import sys, os
#
# Line-wraps sequences of a FASTA file. Also does header cleanup and sequence removal as options.
#
def _isValidHeaderAndSeq(header, seq, canonical_only):
    """ Check if we should write this header and sequence
    """
    if ((canonical_only.upper()[0] == 'F') or (canonical_only.upper()[0] == 'T' and '_' not in header)) and \
       seq != '' and header != '':
        return True
    else:
        return False

def wrap_fasta( fasta_in, fasta_out, canonical_only = 'F' ):
    """ Main function
    """
    header, seq, prev_header = '', '', ''
    with open( fasta_in, 'r') as f, open( fasta_out, 'w' ) as fout:        
        while True:
            r = f.readline()
            # end of file
            if r == '':
                # write last sequence
                if _isValidHeaderAndSeq(header, seq, canonical_only):
                    fout.write(header+'\n'+seq+'\n')                    
                break
            # header line
            elif r[0] == '>':
                # write previous sequence
                if _isValidHeaderAndSeq(header, seq, canonical_only):
                    fout.write(header+'\n'+seq+'\n')
                # get new header and reset sequence
                header = r.rstrip(' \t\n')
                seq = ''
            # sequence line
            elif not r.isspace():
                seq += r.rstrip(' \t\n')
    return 0


if __name__ == '__main__':
    wrap_fasta( sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'F' )

            
