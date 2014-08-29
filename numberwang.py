import sys
import os
from hashlib import md5
from base64 import b64encode

FILE_PATH = os.path.abspath(__file__)


def get_md5(x):
    return md5(x).hexdigest()
    
    
def calculate_state(data):
    state = ''.join(
        (
            ''.join(
                (
                    c for c in b64encode(get_md5(str(ord(item))))[::-1][:8]
                    if c != '='
                )
            )
            for item in get_md5(data)
        )
    )
    
    return state if ord(get_md5(state[0])[0]) % 5 else calculate_state(state)
    
    
def is_numberwang(x, useImag=False):
    imaginary = False in (a.isdigit() for a in x.split('.', 1))
    
    if useImag:
        if not imaginary:
            print "I'm sorry, that is an actual number..."
            return False
            
    else:
        if imaginary:
            print "I'm sorry, that's not a number..."
            return False
            
    x = str(sum((ord(i) for i in x)))
    
    global _state
    _state = calculate_state(x + _state)
    
    return not sum((ord(i) for i in _state)) % 3
    
    
def is_wangernumb(x):
    if False in (a.isdigit() for a in x.split('.', 1)):
        print "I'm sorry, that's not a number..."
        return False
        
    wangernumb = ''.join((str(is_numberwang(x)) for i in xrange(ord(x[0]))))
    
    return not sum((ord(c) for c in get_md5(wangernumb))) % 7
    
    
def main():
    with open(FILE_PATH, 'rb') as f:
        data = f.read()
        
    global _state
    _state = calculate_state(data)
    
    
    while not is_numberwang(raw_input('? ')):
        pass
        
    print "THAT'S NUMBERWANG!\n"
    
    print "Imaginary round:"
    while not is_numberwang(raw_input('? '), True):
        pass
        
    print "THAT'S NUMBERWANG!\n"
    
    print "It's time for WANGERNUMB!"
    while not is_wangernumb(raw_input('? ')):
        pass
        
    print "THAT'S WANGERNUMB!"
    
    return 0
    
    
if __name__ == '__main__':
    sys.exit(main())
    
    