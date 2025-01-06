#!/usr/bin/env python

# Author: Davide Ponzini
# Date: 22/06/2022

import os
import sys

import pandas as pd
import pandasql as pdsql

from dav_tools import argument_parser, messages


def read_file(filepath):
    file_ext = os.path.splitext(filepath)[1]

    if file_ext == '.xlsx':
        return pd.read_excel(filepath)
    elif file_ext == '.csv':
        return pd.read_csv(filepath)
    else:
        messages.critical_error('Unknown input file format (only .csv and .xlsx are accepted)')


def write_file(filepath, data):
    file_ext = os.path.splitext(filepath)[1]

    if file_ext == '.xlsx':
        return data.to_excel(filepath)
    elif file_ext == '.csv':
        return data.to_csv(filepath)
    else:
        messages.critical_error('Unknown output file format (only .csv and .xlsx are accepted)')

def execute_query(dataset, query):
    return pdsql.sqldf(query, locals())


if __name__ == "__main__":
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Performs a SQL query on an .xlsx or .csv file')
    argument_parser.add_argument('input', help='Input filename (.xlsx or .csv)')
    argument_parser.add_argument('output', nargs='?', help='Output filename (.xlsx or .csv)')
    args = argument_parser.args

    messages.info('Notes:')
    messages.info('- Use \'dataset\' in FROM clause')
    messages.info('- Query is executed on EOF (Ctrl+D)')
    print()
    messages.message('Query: ', icon='?', icon_options=[messages.TextFormat.Color.PURPLE], end='')

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
