import arg_parser

if __name__ == '__main__':
    options = arg_parser.add_mutually_exclusive_group()
    arg_parser.add_argument('--info', action=arg_parser.ArgumentAction.STORE_TRUE, argument_group=options)
    arg_parser.add_argument('--success', action=arg_parser.ArgumentAction.STORE_TRUE, argument_group=options)
    arg_parser.add_argument('--warning', action=arg_parser.ArgumentAction.STORE_TRUE, argument_group=options)
    arg_parser.add_argument('--error', action=arg_parser.ArgumentAction.STORE_TRUE, argument_group=options)
    arg_parser.add_argument('category', type=str, nargs='?', default='x')
    arg_parser.add_argument('message', type=str)
    
    args = arg_parser.parse_args()
    
    print(f'[{args.category}] {args.message}')