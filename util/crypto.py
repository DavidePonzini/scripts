#!/usr/bin/env python3

from dav_tools import argument_parser

# applies bitwise xor on a given message and a given key
def bitwise_xor(message: str, key: str):
	result = ''

	for m, k in zip(message, key):
		result += chr(ord(m) ^ ord(k))

	return result


if __name__ == '__main__':
	argument_parser.set_description('Applies one-time-pad encoding to a given message')
	argument_parser.add_argument('message', help='message to cipher')
	argument_parser.add_argument('key', help='string to be used as key, must be same length as `message`')
	args = argument_parser.args

	print(bitwise_xor(args.message, args.key).encode())