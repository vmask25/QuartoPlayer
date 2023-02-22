
def library_of_piece():
    pieces = dict()
    pieces[0] =[False, False, False, False] # basso, bianco, vuoto, tondo
    pieces[1] =[False, False, False, True]
    pieces[2] =[False, False, True, False]
    pieces[3] =[False, False, True, True]
    pieces[4] =[False, True, False, False]
    pieces[5] =[False, True, False, True]
    pieces[6] =[False, True, True, False]
    pieces[7] =[False, True, True, True]
    pieces[8] =[True, False, False, False]
    pieces[9] =[True, False, False, True]
    pieces[10] =[True, False, True, False]
    pieces[11] =[True, False, True, True]
    pieces[12] =[True, True, False, False]
    pieces[13] =[True, True, False, True]
    pieces[14] =[True, True, True, False]
    pieces[15] =[True, True, True, True] # alto, nero, pieno, quadrato
    return pieces

def encoder(v):
    ret = []
    ret.append('Alto') if v[0] else ret.append('Basso')
    ret.append('Nero') if v[1] else ret.append('Bianco')
    ret.append('Pieno') if v[2] else ret.append('Vuoto')
    ret.append('Quadrato') if v[3] else ret.append('Tondo')
    return ret

def transformer(s):
    ret = []
    for c in s:
        ret.append(not int(c)==0)
    return ret

def printer(pieces: dict, k = None, characteristic = None):
    if k == None:
        characteristic = transformer(characteristic)
        return [_key for _key, v in pieces.items() if v == characteristic]
    if characteristic == None:
        return pieces[k]

if __name__ == '__main__':
    pieces = library_of_piece()
    while(1):
        print("Z to close, Enter for characteristic")
        _key = input("Insert piece number: ")
        if _key == '':
            value = input("Insert piece characteristic: ")
            if value[0].isdigit():
                k = printer(pieces, None, value)[0]
                p = k, encoder(printer(pieces, k, None))
            else:
                p = "Wrong value, retry"
        elif _key.isdigit() and int(_key) < 16:
            p = int(_key), encoder(printer(pieces,int(_key), None))
        elif _key == "Z":
            break
        else:
            p = "Wrong value, retry"
        print(p)

