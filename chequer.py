
WORDS = {'1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat', '5': 'lima',
         '6': 'enam', '7': 'tujuh', '8': 'lapan', '9': 'sembilan',
         }


def get_digits(numstr):
    return numstr.split('.')[0]


def get_decimals(numstr):
    try:
        return numstr.split('.')[1]
    except:
        ValueError


def parse_single_digit(numstr):
    return WORDS[numstr]


def parse_two_digits(numstr):
    if numstr[0] is '1':
        if numstr is '10':
            return 'sepuluh'

        elif numstr is '11':
            return 'sebelas'

        else:
            return WORDS[numstr[1]] + ' belas'

    elif numstr[1] is '0':
        return WORDS[numstr[0]] + ' puluh'

    else:
        return WORDS[numstr[0]] + ' puluh ' + WORDS[numstr[1]]
