import argparse
import text_color


class ArgumentAction:
    STORE = 'store'
    STORE_CONST = 'store_const'
    STORE_TRUE = 'store_true'
    STORE_FALSE = 'store_false'
    APPEND = 'append'
    APPEND_CONST = 'append_const'
    COUNT = 'count'
    EXTEND = 'extend'
    BOOLEAN_OPTIONAL = argparse.BooleanOptionalAction


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    epilog = text_color.get_colored_text('--Developed by Davide Ponzini (davide.ponzini95@gmail.com)', text_color.TextFormatOption.Style.ITALIC)
)

groups = {}


def set_version(version: str):
    parser.add_argument('--version', action='version', version=f'%(prog)s {version}')

def set_description(description) -> None:
    parser.description = description

def parse_args() -> argparse.Namespace:
    return parser.parse_args()

def group(name: str, description: str = None) -> argparse._ArgumentGroup:
    if name in groups:
        return groups[name] 

    if description is None:
        new_group = parser.add_argument_group(name)
    else:
        new_group = parser.add_argument_group(name, text_color.get_colored_text(description, text_color.TextFormatOption.Style.ITALIC))

    groups[name] = new_group
    return new_group

def add_mutually_exclusive_group(parent: argparse._ArgumentGroup=parser) -> argparse._MutuallyExclusiveGroup:
    return parent.add_mutually_exclusive_group(
        # formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

def add_argument(*name_or_flags,
                 argument_group: argparse.ArgumentParser | argparse._ArgumentGroup | argparse._MutuallyExclusiveGroup | str=parser,
                 **kwargs):
    if type(argument_group) == str:
        argument_group = group(argument_group)

    argument_group.add_argument(*name_or_flags, **kwargs)

def add_quiet_mode() -> None:
    add_argument('--quiet', argument_group=group('verbosity'), help='Suppresses all non-critical messages', action=ArgumentAction.STORE_TRUE)

def add_verbose_mode() -> None:
    add_argument('--verbose', argument_group=group('verbosity'), help='Prints additional debug messages', action=ArgumentAction.STORE_TRUE)


if __name__ == '__main__':
    set_description('This module provides an easy-to-use way to handle command line arguments')
    set_version('1.0')

    files = group('files')
    add_argument('input_file', argument_group=files, help='first input file', nargs='?')
    add_argument('input_file_2', argument_group=files, help='second input file', nargs='*')
    add_argument('-o', '--output', argument_group=files, help='output files', nargs='+')
    
    add_quiet_mode()
    add_verbose_mode()

    print(parse_args())
