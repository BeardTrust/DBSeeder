#!/usr/bin/env python3

import data.formats
import generators.loanTypes


def generate_loan_types_file(file_format=data.formats.Files.txt):

    file_name = 'C:/Users/enemy/Documents/Smoothstack/BeardTrust/gitrepos/generated_sql_files/loan_type'
    file_name += '.sql' if file_format == data.formats.Files.sql else ''
    file_name += '.txt' if file_format == data.formats.Files.txt else ''

    bigQuery = ''

    for x in range(100):
        loan_types = generators.loanTypes.generate_loan_type()
        bigQuery += loan_types.query
        bigQuery += loan_types.values
        bigQuery += ';\n'

    print("big query: ", bigQuery)
    outfile = open(file_name, 'w')
    outfile.write(bigQuery)

    outfile.close()

    print("Created  loan_types.")