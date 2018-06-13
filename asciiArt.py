#pip install pyfiglet http://www.figlet.org/examples.html
#pip install termcolor https://pypi.org/project/termcolor/
#pip install colorama (colour support)
import sys


def makeArt(text,textColor,background,font,intro):
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint
    from pyfiglet import figlet_format
    print('\n')
    if text is not None:
        cprint(figlet_format(text, font=font),textColor, background, attrs=['concealed'])
    if intro is not None:
        cprint(intro, textColor, background)
