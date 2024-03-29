# Simple usage example for the .tsvlib.py library, which handles files in .cupt format
# By Silvio Cordeiro, 1 Oct 2019

import argparse
import os
import sys

sys.path.append('.')
import tsvlib

parser = argparse.ArgumentParser(description='Simple usage example of the tsvlib library')
parser.add_argument("--input", type=argparse.FileType('r'), required=True,
        help="""Path to input file (in .cupt format)""")
args = parser.parse_args()
with args.input as f:
    sentences = list(tsvlib.iter_tsv_sentences(f))
    print(len(sentences))
    # input()
    max_len = []
    for sentence in sentences:
        # print("\n-------------------------------")
        # print("NEW SENTENCE")
        forms = " ".join(token['FORM'] for token in sentence.words)
        len_ = len(forms)
        # print("Text:", forms)
        max_len.append(len_)
        first = sentence.words[0]
        # first_LEMMA = first['LEMMA']
        # first_UPOS = first.get('UPOS', '??')  # UPOS not necessarily defined for every token...
        # first_FEATS = first.get('FEATS', '??')  # FEATS not necessarily defined for every token...
        # first_HEAD = int(first.get('HEAD', 0))
        # parent = sentence.words[first_HEAD-1]['FORM'] if first_HEAD != 0 else '<unknown>'

        # print("First word: LEMMA={!r}, POS={!r}, FEATS={!r}, DepParent={!r}".format(
        #     first_LEMMA, first_UPOS, first_FEATS, parent))
    print("MAX_LEN: ", max(max_len))
    print(max_len)
    # print("\n#####################################")
    # print("LAST 3 SENTENCES WITH LEMMA='modified'")
    # for sentence in sentences[-3:]:
    #     for token in sentence.words:
    #         token['LEMMA'] = 'modified'
    # tsvlib.write_tsv(sentences[-3:], file=sys.stdout)

# print(len(sentences))
# avg_ = sum_len / len(sentences)
# print(f"avg of length of the sentences: {avg_}")
# print(pos_set)