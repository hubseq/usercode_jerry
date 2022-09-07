import sys, os

def canonicalOnlyGTF( gtf_in, gtf_out ):
    with open(gtf_in, 'r') as f, open(gtf_out,'w') as fout:
        for r in f:
            rt = r.split('\t')
            if '_' not in rt[0]:
                fout.write(r)
    return 0

if __name__ == '__main__':
    canonicalOnlyGTF( sys.argv[1], sys.argv[2] )
