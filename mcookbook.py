import sys

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
        print "Cargando..."
    else:
        print "The Argument '" + sys.argv[1] + "' does not belong to any frontend"
