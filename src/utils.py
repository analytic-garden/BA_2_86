#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
utils.py - utilities for BA.2.86 analysis
author: Bill Thompson
license: GPL 3
copyright: 2023-08-24
"""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def read_fasta(fasta_file: str) -> dict[str, SeqRecord]:
    """read a FASTA file and return a dictionary of 

    Parameters
    ----------
    fasta_file : str
        the file name

    Returns
    -------
    dict[str, SeqRecord]
        key: EPI id from the FASTA header
        value: a SeqRecord
    """
    fasta_recs = {}
    with open(fasta_file) as f:
        for record in SeqIO.parse(f, 'fasta'):
            EPI_id = record.id.split('|')[1]
            fasta_recs[EPI_id] = record

    return fasta_recs

