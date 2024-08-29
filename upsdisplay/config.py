# Table schema options are:
# Options are:
#   '<unique-node>'                           # Select a node name that is not already in the nodes.data table
#   '<zero-or-more-nodes>'                    # A list of zero or more node names
#   '<one-or-more-nodes>'                     # A list of one or more node names
#   '<one-of-node>'                           # A single node name
#   [ '<zero-or-more>' 'item' 'item' ... ]    # Zero of more from a list of string items
#   [ '<one-or-more>' 'item' 'item' ... ]     # One of more from a list of string items
#   [ '<one-of>' 'item' 'item' ... ]          # One from a list of string items
#   '<str>'                                   # A generic string
#   '<bool>'                                  # A boolean item (value cell is True or False and display value is Yes or No)

DEFAULT_CONFIG = {
    "version": 1,
    "global": {
        # Global configuration goes here
    },
    "available": [
        # List of available devices seen by scanner
    ],
    "devices": {
        # Editing schema infomration (format of each field)
        "schema": {
        },
        # Headers to display
        "headers": {
        },
        # Default values when creating new entry
        "default": {
        },
        # Fields to show in record edit dialog
        "edit_fidlds": [
        ],
        # Fields to show in table view
        "table_fields": [
        ],
    },
    "nodes": {
        "schema": {
            "name": "<unique-node>",                # name is a unique node name
            "icon": "<icon>",                       # Device icon
            "dns": "<str>",                         # dns is a string (but should be smarter)
            "uri": "<str>",                         # uri is a string (but should be smarter)
            "requires": "<zero-or-more-nodes>",     # requires is a list of <node names>
            "wants": "<zero-or-more-nodes>",        # wants is a list of <node names>
            "start": "<str>",                       # start is a string (action function)
            "stop": "<str>",                        # stop is a string (action function)
            "showmain": "<bool>",                   # main is a boolean (show on main page if True)
            "username": "<str>",                    # User name credential for access
            "password": "<password>",               # Password for credential    
        },
        # If displayed, use these strings to identify the value on screen
        "headers": {
            "name": "Name",
            "icon": "Icon",
            "dns": "Dns",
            "uri": "URI",
            "requires": "Requires",
            "wants": "Wants",
            "start": "Start Action",
            "stop": "Stop Action",
            "showmain": "On Main Page",
            "username": "User name",
            "password": "Password",
        },
        # Include these in the table shown for configuration, in order of display
        'table_fields': [
            'name',
            "uri",
            "requires",
            "wants",
            "showmain",
        ],
        # Include these in the detailed edit dialog, in order of display
        'edit_fields': [
            'name',
            'icon',
            'dns',
            'uri',
            'requires',
            'wants',
            'start',
            'stop',
            'showmain',
            'username',
            'password',
        ],
        # A default setting when creating a new entry
        'default': {
            "name": None,
            "icon": None,
            "dns": "",
            "uri": "",
            "requires": [],
            "wants": [],
            "start": "",
            "stop": "",
            "showmain": False,
            "username": "",
            "password": "",
        },
        "data": [{
            "name": "Nimbus",
            "icon": None,
            "dns": "nimbus.aerodesic.net",
            "uri": "APC1:1",
            "requires": ["Nas3"],
            "wants": ["Nas1", "Nas2"],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": True,
            "username": "",
            "password": "",
        },{
            "name": "Cirrus",
            "icon": None,
            "dns": "cirrus.aerodesic.net",
            "uri": "APC1:2",
            "requires": ["Nas3"],
            "wants": ["Nas1", "Nas2"],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": True,
            "username": "",
            "password": "",
        },{
            "name": "Cumulus",
            "icon": None,
            "dns": "cumulus.aerodesic.net",
            "uri": "APC1:3",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": True,
            "username": "",
            "password": "",
        },{
            "name": "Nas1",
            "icon": None,
            "dns": "nas1.aerodesic.net",
            "uri": "APC1:4",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
            "username": "",
            "password": "",
        },{
            "name": "Nas2",
            "icon": None,
            "dns": "nimbus.aerodesic.net",
            "uri": "APC1:5",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
            "username": "",
            "password": "",
        },{
            "name": "Nas3",
            "icon": None,
            "dns": "nas3.aerodesic.net",
            "uri": "APC1:6",
            "requires": [],
            "wants": ["Gatekeeper"],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
            "username": "",
            "password": "",
        },{
            "name": "Gatekeeper",
            "icon": None,
            "dns": "gatekeeper.aerodesic.net",
            "uri": "APC1:7",
            "requires": [ "DmzSwitch", "NasSwitch" ],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
            "username": "",
            "password": "",
        },{
            "name": "DmzSwitch",
            "icon": None,
            "dns": "",
            "uri": "APC1:8",
            "requires": [],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
            "username": "",
            "password": "",
        },{
            "name": "NasSwitch",
            "icon": None,
            "dns": "",
            "uri": "APC2:1",
            "requires": [],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
            "username": "",
            "password": "",
        }],
    }
}
