import subprocess


class _Util:
    def get_color_code(command: str) -> bytes:
        try:
            return subprocess.check_output(command.split())
        except subprocess.CalledProcessError:
            return b''


class TextFormatOption:
    class Style:
        NORMAL              = b'\033]0m'
        BOLD                = _Util.get_color_code('tput bold')
        DIM                 = _Util.get_color_code('tput dim')
        ITALIC              = _Util.get_color_code('tput sitm')
        UNDERLINE           = _Util.get_color_code('tput smul')
        UNDERLINE_DOUBLE    = b'\033]4:2m'
        UNDERLINE_CURLY     = b'\033]4:3m'
        BLINK               = _Util.get_color_code('tput blink')
        REVERSE             = _Util.get_color_code('tput rev')
        INVISIBLE           = _Util.get_color_code('tput invis')		# Invisible but copy-pasteable
        STRIKETHROUGH       = b'\033]9m'
        OVERLINE            = b'\033]53m'
    class Color:
        DARKGRAY    = _Util.get_color_code('tput setaf 0')
        RED         = _Util.get_color_code('tput setaf 1')
        GREEN       = _Util.get_color_code('tput setaf 2')
        YELLOW      = _Util.get_color_code('tput setaf 3')
        BLUE        = _Util.get_color_code('tput setaf 4')
        PURPLE      = _Util.get_color_code('tput setaf 5')
        CYAN        = _Util.get_color_code('tput setaf 6')
        WHITE       = _Util.get_color_code('tput setaf 7')
    class Background:
        DARKGRAY    = _Util.get_color_code('tput setab 0')
        RED         = _Util.get_color_code('tput setab 1')
        GREEN       = _Util.get_color_code('tput setab 2')
        YELLOW      = _Util.get_color_code('tput setab 3')
        BLUE        = _Util.get_color_code('tput setab 4')
        PURPLE      = _Util.get_color_code('tput setab 5')
        CYAN        = _Util.get_color_code('tput setab 6')
        WHITE       = _Util.get_color_code('tput setab 7')
    RESET = b'\033[0m'


def get_format(*options):
    result = ''

    for option in options:
        result += option.decode()

    return result

def set_format(*options):
    for option in options:
        print(option.decode(), end='')

def get_colored_text(text: str, *format_options):
    result = ''
    result += get_format(*format_options)
    result += text
    result += get_format(TextFormatOption.RESET)

    return result

def print_colored_text(text: str, *format_options, end: str='\n', file=None):
    text = get_colored_text(text, *format_options)
    print(text, end=end, file=file)

def input_colored(*format_options, text: str=''):
    set_format(*format_options)
    result = input(text)
    set_format(TextFormatOption.RESET)

    return result