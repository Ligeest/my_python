def count_words(filename):
    """jisuan"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
            msg = "sorry about" + filename
            print (msg)
    else:
        word = contents.split()
        len1 = len(word)
        #print(filename+word+str(len1))
filename = "pi.txt"
count_words(filename)
