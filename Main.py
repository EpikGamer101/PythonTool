import time
import os, signal

A = '''

<!DOCTYPE html> is the declaration tag for a standard HTML
document. This is used to tell the browser what kind of HTML document
it is.

'''
a = '''

This tag defines a PARAGRAPH. These are highly customisable
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

print("This tool was made to help programmers, like myself,")
print("with HTML tags. It takes your input, say you typed")
print("<div>, it would give you an accurate description of")
print("that tag and a list of its uses.")
print("")
print("")
print("This tool was made by Chase Barnes")
print("@Copyright 2017")
print("")
print("(Remember, type BASE tags -<p>- ONLY)")
print("")

Username = input("Username: ")


if Username == '':
    Username = 'Anonymous User'
print("")
print("Hello, " + Username + "!")
print("")


def main():
    Input = input("TAG: ")
    if Input == 'exit':
        print("")
        print("SHUTTING DOWN")
        print("")
        time.sleep(1)
        os.kill(os.getpid(), signal.SIGTERM)
    elif Input == '':
        print("")
        print("Please enter a tag.")
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
    else:
        print("Not Recognized!")
        main()

main()
    

