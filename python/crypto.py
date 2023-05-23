import arg_parser as arg_parser

# applies bitwise xor on a given message and a given key
def bitwise_xor(message: str, key: str):
	result = ''

	for m, k in zip(message, key):
		result += chr(ord(m) ^ ord(k))

	return result


if __name__ == '__main__':
	arg_parser.set_description('Applies one-time-pad encoding to a given message')
	arg_parser.parser.add_argument('message', help='message to cipher')
	arg_parser.parser.add_argument('key', help='string to be used as key, must be same length as `message`')
	args = arg_parser.parse_args()

	print(bitwise_xor(args.message, args.key))