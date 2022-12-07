from datetime import datetime
def parsea_fecha(cadena):
    '''01/01/2019 06:19'''
    return datetime.strptime(cadena, '%d/%m/%Y %H:%M')

def fecha_to_string(f):
    return str(f.day) + '/' + str(f.month) + '/' + str(f.year) 

