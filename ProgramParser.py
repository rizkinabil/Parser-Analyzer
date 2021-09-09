#inputan
sentence = 'moeder zitten'
tokens = sentence.lower().split()
tokens.append('EOS')

#define
nonterminals = ['S','SB','VB','OB']
terminals =['vader','moeder','zitten','eten','wassen','stoel','fiets','vis','kip','ei']

#parse table
parse_table = {}

parse_table[('S','vader')] = ['SB' , 'VB', 'OB']
parse_table[('S','moeder')] = ['SB' , 'VB', 'OB']
parse_table[('S','zitten')] = ['error']
parse_table[('S','eten')] = ['error']
parse_table[('S','wassen')] = ['error']
parse_table[('S','stoel')] = ['error']
parse_table[('S','fiets')] = ['error']
parse_table[('S','vis')] = ['error']
parse_table[('S','kip')] = ['error']
parse_table[('S','ei')] = ['error']
parse_table[('S','EOS')] = ['error']

parse_table[('SB','vader')] = ['vader']
parse_table[('SB','moeder')] = ['moeder']
parse_table[('SB','zitten')] = ['error']
parse_table[('SB','eten')] = ['error']
parse_table[('SB','wassen')] = ['error']
parse_table[('SB','stoel')] = ['error']
parse_table[('SB','fiets')] = ['error']
parse_table[('SB','vis')] = ['error']
parse_table[('SB','kip')] = ['error']
parse_table[('SB','ei')] = ['error']
parse_table[('SB','EOS')] = ['error']

parse_table[('VB','vader')] = ['error']
parse_table[('VB','moeder')] = ['error']
parse_table[('VB','zitten')] = ['zitten']
parse_table[('VB','eten')] = ['eten']
parse_table[('VB','wassen')] = ['wassen']
parse_table[('VB','stoel')] = ['error']
parse_table[('VB','fiets')] = ['error']
parse_table[('VB','vis')] = ['error']
parse_table[('VB','kip')] = ['error']
parse_table[('VB','ei')] = ['error']
parse_table[('VB','EOS')] = ['error']

parse_table[('OB','vader')] = ['error']
parse_table[('OB','moeder')] = ['error']
parse_table[('OB','zitten')] = ['error']
parse_table[('OB','eten')] = ['error']
parse_table[('OB','wassen')] = ['error']
parse_table[('OB','stoel')] = ['stoel']
parse_table[('OB','fiets')] = ['fiets']
parse_table[('OB','vis')] = ['vis']
parse_table[('OB','kip')] = ['kip']
parse_table[('OB','ei')] = ['ei']
parse_table[('OB','EOS')] = ['error']

#inisialisasi
stack = []
stack.append('#')
stack.append('S')

#input inisialisasi
idxtoken = 0
symbol = tokens[idxtoken]

#proses parsing
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top adalah',top)
    print('symbol adalah',symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top==symbol:
            stack.pop()
            idxtoken = idxtoken + 1
            symbol = tokens[idxtoken]
            if symbol=='EOS':
                print('isi stack adalah',stack)
                stack.pop()
        else:
            print('error')
            break;
    elif top in nonterminals:
        print('top adalah simbol non terminal')
        if parse_table[(top,symbol)] [0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top,symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack adalah',stack)
    print()

#conclu
print()
if symbol=='EOS' and len(stack)==0:
    print('Input string adalah ', sentence, '. Kalimat diterima, sesuai Grammar')
else:
    print('Error, input string adalah', sentence, '. Kalimat tidak diterima, tidak sesuai Grammar')


