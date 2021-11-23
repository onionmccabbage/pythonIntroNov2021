# file input and file output

def simpleOutput():
    # Python uses file access objects (defaults to text)
    # NB this will create a file if it does not exist
    # 'a' means 'append to the file, 'w' means 'overwrite' 't' for text 'x' exclusive
    fout = open('output.txt', 'at') 
    print('here is some interesting content', file=fout) # NB print ALWAYS adds a new line
    fout.close()

def simpleInput(): # default format is text
    # CAREFUL - throws exception if the file does not exist
    try:
        fin = open('output.txt', 'r') # 'r' to read, 'rt' read text (the default)
        received = fin.read() # reads the entire file
        print(received)
    except Exception as e:
        print('Oh no.... {}'.format(e))
    finally:
        fin.close()

# auto close a file access object with the 'while' operator (and try-except)
def fileWriter(str='default'):
    try:
        fout   = open('mylog.txt', 'at') # 'xt' to exclusively access, 'at' to append text
        size   = len(str)
        offset = 0
        chunk  = 24
        while True:
            if offset > size:
                fout.write('\n') # put a new-line character at the end of the file
                break # this stops the while loop, which will implicitly close the file access object
            else: # here we write chunks of text to the file access object
                fout.write(str[offset:offset+chunk]) # write 24 characters at a time
                offset += chunk
    except FileExistsError as fe:
        print('The file already exists {}'.format(fe)) 
    except Exception as e:
        print('something wnet wrong {}'.format(e))
    finally:
        print('all done')

def fileReader():
    fin = open('mylog.txt', 'rt')
    retrieved = fin.readline() + '-----' + fin.readline() # read TWO lines
    print(retrieved)
    fin.close() # always check your file access object will be closed!

if __name__ == '__main__':
    simpleOutput()
    simpleInput()
    fileWriter('lots of short bits of text can be written')
    fileWriter('bibblybooblyboo')
    fileWriter('...................')
    fileWriter('thats all folks!!')
    fileReader()