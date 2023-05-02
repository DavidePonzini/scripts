import sys

from text_color import TextFormatOption, print_colored_text, input_colored


def _message(text, icon=None, text_options=[], icon_options=[], blink=False, end='\n'):
    if icon is not None:
        print_colored_text('[', *icon_options, TextFormatOption.Style.BOLD, end='')
        
        if blink:
            print_colored_text(icon, *icon_options, TextFormatOption.Style.BOLD, TextFormatOption.Style.BLINK, end='')
        else:
            print_colored_text(icon, *icon_options, TextFormatOption.Style.BOLD, end='')
        
        print_colored_text('] ', *icon_options, TextFormatOption.Style.BOLD, end='')
    
    print_colored_text(text, *text_options, end=end)
    

# message indicating an information
def info(text: str, blink=False) -> None:
    _message(text, 
             icon='i', 
             blink=blink)

# message indicating an error
def error(text: str, blink=False) -> None:
    _message(text, 
             icon='-', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.RED
             ]
    )

# message indicating a warning
def warning(text: str, blink=False) -> None:
    _message(text, 
             icon='!', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.YELLOW
             ]
    )

# message indicating a successfully completed action
def success(text: str, blink=False) -> None:
    _message(text, 
             icon='+', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.GREEN
             ]
    )

# prints a question and returns the answer
def ask(question: str, end=': ') -> str:
    _message(f'{question}{end}',
             icon='?',
             icon_options=[
                 TextFormatOption.Color.BLUE
             ],
             end='')
    
    return input_colored(
        TextFormatOption.Style.ITALIC,
    )

# prints a question asking the user if they want to continue executing the program
# 	a positive answer makes the program continues its normal execution
# 	a negative answer terminates the program
# optionally supports a custom question
def ask_continue(text: str=None):
    if text is not None:
        message = f'{text}. Continue? (y/N)'
    else:
        message = 'Continue? (y/N)'

    while True:
        ans = ask(message, end=' ')

        if ans.lower() == 'y':
            break
        if ans.lower() == 'n':
            sys.exit()
        