import time
import os, signal
import datetime

def Start():

    while True:
        RecordLog = input('Would you like me to record the date and time of this session? ')
        print("")
        if RecordLog == 'yes':
            file = open('C:\csc1AB\PROJECTS_\Project_1\log.txt', 'r+')
            file.truncate()
            file.write('Session started at: ' + datetime.datetime.now().ctime() + '''

''')
            print(file.readlines())
            print("")
            break
        elif RecordLog == 'no':
            break
        else:
            continue

    A = '''

    <!DOCTYPE html> is the declaration tag for a standard HTML
    document. This is used to tell the browser what kind of HTML document
    it is.

    '''
    a = '''

    <p> This tag defines a PARAGRAPH. These are highly customisable
    in CSS, and can be used in any HTML version. There are variations
    of this tag, such as:

    <p1>
    <p2>
    <p3>
    <p4>
    <p5>
    <p6>

    and so on..

    '''
    B = '''

    <h> This tag defines a HEADER. These, like PARAGRAPHS (see <p>),
    are highly custonizable in CSS, and, like PARAGRAPHS, can be used
    in any HTML version. There are variations of this tag, such as:

    <h1>
    <h2>
    <h3>
    <h4>
    <h5>
    <h6>

    and so on..

    '''
    b = '''

    <a> This tag defines a HYPERLINK. This can be used to turn ANY block
    or peice of text into a clickable link. This has a variety of uses, such as:

    Redirection
    Buttons
    Drop down menus
    Navigations bars

    and many more.

    A hyperlink's syntax is as shows:

    <a href = "www.LINK.com"  target = "(_blank, _parent, _self, and _top are
    your options)" type = "(specify the type of linked document.)"></a>

    The closing tag is nessesary for this to work with your given parameters.

    '''
    C = '''

    <div> This tag defines a DIVIDED BLOCK where you can store content,
    such as pictures, videos, buttons, text, and just about anything you can
    think of. This is mainly used for containing things such as:

    Navigation bars
    Buttons
    The entire page (Formally known as "Wrapper")
    ETC.

    This DIV's syntax is as shows:

    <div class = "(calls a certain CSS class)"></div>

    The closing tag is nessesary for this to work with your given parameters.

    '''
    c = '''

    <link> This tag will LINK (a) CSS file(s) to your HTML document. You can
    LINK multiple CSS files to a single HTML document. You can LINK files
    from Google, as well as your own .css files.

    The LINK's syntax is as shows:

    <link href = "FILENAME.css (OR) www.LINK.com" rel = "Stylesheet" type =
    "text/css">

    '''
    D = '''

    <br> This tag creates a LINE BREAK. Just like in any text-editor program,
    you can create a LINE BREAK using ENTER, or the RETURN KEY. This
    tag is a very basic one, and it takes like, 5 minutes to remember.

    The LINE BREAK's syntax is as shows:

    <br>

    Simple right?!

    '''
            
    print("This tool was made to help programmers, like myself,")
    print("with HTML tags. It takes your input, say you typed")
    print("<div>, it would give you an accurate description of")
    print("that tag and a list of its uses.")
    print("")
    print("Guest users please login as 'Guest'")
    print("")
    print("This tool was made by Chase Barnes")
    print("@Copyright 2017")
    print("")
    print("(Remember, type BASE tags -<p>- ONLY)")
    print("")

    while True:
        Username = input("Username: ")
        if Username == 'Guest':
            Username = 'Guest'
            file.write('''User: Guest

''')
            break
        elif Username == '/admin061503':
            Username = "Admin Chase"
            file.write('''User: Admin Chase

''')
            Pass = input("Password: ")
            if Pass == '*************':
                Username = 'Admin Chase'
                file.write('''logged in!

''')
                break
            else:
                print("")
                print("The Input is Incorrect")
                print("")
                file.write('''Wrong Password has been inputed.

''')
        else:
            print("")
            print("UNKNOWN USERNAME")
            print("")
            continue
            

    print("")
    print("Welcome, " + Username + "!")
    print("")

    def main():
        Input = input("TAG: ")
        if Input == '/exit':
            answerexit = input("Are you sure? ")
            if  answerexit == 'yes':
                file.write('session ended at: ' + datetime.datetime.now().ctime() + '''

''')
                file.close()
                print("")
                print("SHUTTING DOWN..")
                print("")
                time.sleep(2)
                os.kill(os.getpid(), signal.SIGTERM)
            elif answerexit == 'no':
                print("")
                print("SHUTDOWN ABORTED..")
                print("")
                main()
        elif Input == '/reset':
                print("")
                print("RESTARTING..")
                print("")
                time.sleep(1.5)
                Start()
        elif Input == '':
            print("")
            print("Please enter a tag or command.")
            print("")
            main()
        elif Input == '<!DOCTYPE html>':
            print(A)
            time.sleep(1)
            main()
        elif Input == '<p>':
            print(a)
            time.sleep(1)
            main()
        elif Input == '<h>':
            print(B)
            time.sleep(1)
            main()
        elif Input == '<a>':
            print(b)
            time.sleep(1)
            main()
        elif Input == '<div>':
            print(C)
            time.sleep(1)
            main()
        elif Input == '<link>':
            print(c)
            time.sleep(1)
            main()
        elif Input == '<br>':
            print(D)
            time.sleep(1)
            main()
        else:
            print("")
            print('''The tag or command you entered is Not Recognized of is not yet
    supported by this tool.''')
            print("")
            main()

    main()
Start()
    
