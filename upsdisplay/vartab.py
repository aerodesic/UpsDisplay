# A very simple hierachical data storage

DEFAULT_CONFIG = {
    'global': {
    },
    'available': [],
    'nodes': [{
        'name': 'Nimbus',
            'dns': "nimbus.aerodesic.net",
            'uri': 'APC:1',
            'requires': ["Nas3"],
            'wants': ["Nas1", "Nas2"],
            'start': 'apcstart',
            'stop': 'apcstop',
         },{
         'name': "Cumulus",
            'dns': "cumulus.aerodesic.net",
            'uri': 'APC:2',
            'requires': ["Nas3"],
            'wants': [],
            'start': 'apcstart',
            'stop': 'apcstop',
         },{
            'name': "Nas1",
            'dns': "nas1.aerodesic.net",
            'uri': 'APC:3',
            'requires': ["Nas3"],
            'wants': [],
            'start': 'apcstart',
            'stop': 'apcstop',
        },{
            'name': "Nas2",
            'dns': "nimbus.aerodesic.net",
            'uri': 'APC:4',
            'requires': ["Nas3"],
            'wants': [],
            'start': 'apcstart',
            'stop': 'apcstop',
        },{
            'name': "Nas3",
            'dns': "nas3.aerodesic.net",
            'uri': 'APC:5',
            'requires': [],
            'wants': ["Gatekeeper"],
            'start': 'apcstart',
            'stop': 'apcstop',
        },{
            'name': "Gatekeeper",
            'dns': 'gatekeeper.aerodesic.net',
            'uri': 'APC:6',
            'requires': [ "DmzSwitch", "NasSwitch" ],
            'wants': [],
            'start': 'apcstart',
            'stop': 'apcstop',
        },{
            'name': "DmzSwitch",
            'dns': '',
            'uri': 'APC:7',
            'requires': [],
            'wants': [],
            'start': 'apcstart',
            'stop': 'apcstop',
        },{
            'name': "NasSwitch",
            'dns': '',
            'uri': 'APC:8',
            'requires': [],
            'wants': [],
            'start': 'apcstart',
            'stop': 'apcstop',
        },
    ],
}

class VarTabException(Exception):
    pass

class VarTab():
    MAX_RECURSION = 10

    def __init__(self, init = {}):
        self.__data = init

    def Load(self, values):
        self.__data = values

    def Reset(self):
        self.Load({})

    def FindValue(self, varname, subvar=None, write=False):
        varvalue = self.__data if subvar is None else subvar

        for piece in varname.split("."):
            # print("FindValue: piece %s varvalue %s" % (piece, varvalue))
            if type(varvalue) is dict:
                if piece in varvalue:
                    varvalue = varvalue[piece]
                elif write:
                    # We are setting values, so create the dictionary entry here
                    varvalue[piece] = {}
                    varvalue = varvalue[piece]
                else:
                    raise VarTabException("Undefined: %s in %s" % (piece, varname))
            elif piece == '':
                raise VarTabException("Ran out of subfields looking for %s" % (varname))
            else:
                raise VarTabException("Trying to get element %s in non-dictionary" % (piece))

        return varvalue

    # Return a value if present, else exception thrown for undefined
    # If no value given, returns entire tree
    def GetValue(self, varname="", subvar=None, evaluate=True, recursion=0):
        if recursion > self.MAX_RECURSION:
            raise VarTabException("recursion overflow looking for %s" % (varname))

        if varname == "":
            return self.__data if subvar is None else subvar

        value = self.FindValue(varname, subvar=subvar)

        if evaluate:
            # Process any macros in the varname
            if type(value) is str:
                working = True
                while working:
                    # Look for start of macro
                    start = value.find("${")
                    if start >= 0:
                        # Look for end of macro
                        end = value.find("}", start + 2)
                        if end >= 0:
                            newvalue = self.GetValue(value[start+2:end], recursion=recursion + 1, evaluate=evaluate)
    
                            # String replacement within the text
                            value = value[:start] + str(newvalue) + value[end+1:]
                        else:
                            working = False
                    else:
                        working = False
    
            if type(value) == str:
                # If $evel{xxx} then evaluate expression to get return value
                start = value.find("$eval{")
                if start >= 0:
                    end = value.find("}", start+6)
                    if end >= 0:
                        value = eval(value[start+6:end])

        return value

    def SetValue(self, varname, value, subvar=None, protect=True):
        try:
            first, last = varname.rsplit('.', maxsplit=1)
            subvar = self.FindValue(first, subvar=subvar, write=True)

        except:
            subvar = self.__data if subvar is None else subvar
            last = varname

        if protect and last in subvar and (subvar[last].find("$eval{") >= 0 or subvar[last].find("${") >= 0):
            raise VarTabException("Var %s contains evaluated field and not overriden: %s" % (varname, subvar[last]))

        else:
            subvar[last] = value

