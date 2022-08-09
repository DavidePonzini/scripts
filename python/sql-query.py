# Author: Davide Ponzini
# Date: 22/06/2022

import os
import sys

import pandas as pd
import pandasql as pdsql
import argparse


def read_file(filepath):
    file_ext = os.path.splitext(filepath)[1]

    if file_ext == '.xlsx':
        return pd.read_excel(filepath)
    elif file_ext == '.csv':
        return pd.read_csv(filepath)
    else:
        print('Unknown input file format (only .csv and .xlsx are accepted')
        exit(1)


def write_file(filepath, data):
    file_ext = os.path.splitext(filepath)[1]

    if file_ext == '.xlsx':
        return data.to_excel(filepath)
    elif file_ext == '.csv':
        return data.to_csv(filepath)
    else:
        print('Unknown output file format (only .csv and .xlsx are accepted')
        exit(1)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('input', help='Input filename (.xlsx or .csv)')
    args.add_argument('output', nargs='?', help='Output filename (.xlsx or .csv)')
    args = args.parse_args()

    print('Notes:')
    print('- Use \'dataset\' in FROM clause')
    print('- Query is executed on EOF (Ctrl+D)')
    print()
    print('Query: ', end='', flush=True)

    query = ''
    for line in sys.stdin:
        query += line
    print()

    # Read dataset
    dataset = read_file(args.input)

    # Execute query
    result = pdsql.sqldf(query, locals())

    print(result)

    # Save to file
    if args.output:
        write_file(args.output, result)
