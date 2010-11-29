import os
import sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
import locale
idioma = locale.setlocale(locale.LC_ALL, '')
import core

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print """
        You must specify a front-end to use:
    
        The next frontends are avaible:
        Command Line  =    mcookbook -c
        Curses        =    Not Avaible Yet    
        GTK           =    Not Avaible Yet
        QT            =    Not Avaible Yet    
        WX            =    Not Avaible Yet    
        SDL           =    Not Avaible Yet
        EFL           =    Not Avaible Yet
        """
    else:
        if sys.argv[1] == "-c":
            import mcookbook_console
        else:
            print "The Argument '" + sys.argv[1] + "' does not belong to any frontend"
