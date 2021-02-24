
def read_file():
    n = 16
    with open('foobar.file', 'rb') as fp:
        running = True
        while running:
            chunk = fp.read(n)
            if chunk == '': # end of file, stop running.
                running = False
            else:
                print(chunk)
