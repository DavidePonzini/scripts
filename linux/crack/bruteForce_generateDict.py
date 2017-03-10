#!/usr/bin/env python3

import itertools
import argparse
import string


def generate(length, charset=string.printable, sep=''):
	values = itertools.combinations_with_replacement(charset, length)

	for value in values:
		yield ''.join(value) + sep


def write_to_file(filename, length, charset):
	with open(filename, 'w') as file:
		for value in generate(length, charset, '\n'):
			file.write(value)


def write_to_screen(length, charset):
	for value in generate(length, charset):
		print(value)


def _main():
	parser = argparse.ArgumentParser()

	parser.add_argument('--version',
		action='version',
		version='%(prog)s 1.0')
	
	parser.add_argument("-l", '--length',
		type=int,
		dest='length',
		help='the number of characters for each word',
		required=True)
	parser.add_argument("--charset",
		type=str,
		help='list of characters to use',
		default=string.printable)
	parser.add_argument('-f', '--filename',
		type=str,
		dest='filename',
		help='file to write to',
		default='')

	args = parser.parse_args()

	if(args.filename != ''):
		write_to_file(args.filename, args.length, args.charset)
	else:
		write_to_screen(args.length, args.charset)


if __name__ == '__main__':
	_main()
