#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
check_ba_2_86_files.py - Check BA.2.86 files for consitency
author: Bill Thompson
license: GPL 3
copyright: 2023-08-24
"""
import sys
import pandas as pd
from Bio import SeqIO
sys.path.append('/mnt/g/Covid-19/GISAID/2023_09_04/src/')
from utils import read_fasta

def main():
    fasta_file = '/mnt/g/Covid-19/GISAID/2023_09_04/data/gisaid_hcov-19_2023_09_04_13.fasta'
    meta_file = '/mnt/g/Covid-19/GISAID/2023_09_04/data/ba_2_86.csv'
    out_file = '/mnt/g/Covid-19/GISAID/2023_09_04/data/ba_2_86.fasta'

    recs = read_fasta(fasta_file)
    df = pd.read_csv(meta_file)

    # check the accession numbers
    rec_list = []
    for rec_id, rec in recs.items():
        if rec_id in df['Accession.ID'].values:
            rec_list.append(rec)

    SeqIO.write(rec_list, out_file, 'fasta')

if __name__ == "__main__":
    main()
