dicionary = {
    
    'text': {
        #Cores
        'null': '0',
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'purple': '35',
        'cyan': '36',
        'gray': '37',
        'white': '97'
    },

    'back': {
        #Background
        'null': '0',
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'purple': '45',
        'cyan': '46',
        'gray': '47',
        'white': '107'
    },

    'style': {
        #Estilo
        'null': '0',
        'bold': '1',
        'underline': '4',
        'negative': '7'
    },

}

def color(style = 'null', text = 'null', back = 'null'):

    if(style == 'clear'):
        return ('\x1b[m')
    else:
        defstyle = dicionary['style'][style]
        deftext = dicionary['text'][text]
        defback = dicionary['back'][back]

        return (f'\x1b[{defstyle};{deftext};{defback}m')
