DEFAULT_CONFIG = {
    "version": 1,
    "global": {
        # Global configuration goes here
    },
    "available": [
        # List of available devices seen by scanner
    ],
    "nodes": {
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
        "schema": {
            "name": "<unique-node>",                  # name is a unique node name
            "dns": "<str>",                           # dns is a string (but should be smarter)
            "uri": "<str>",                           # uri is a string (but should be smarter)
            "requires": "<zero-or-more-nodes>",       # requires is a list of <node names>
            "wants": "<zero-or-more-nodes>",          # wants is a list of <node names>
            "start": "<str>",                         # start is a string (action function)
            "stop": "<str>",                          # stop is a string (action function)
            "showmain": "<bool>",                     # main is a boolean (show on main page if True)
        },
        "headers": {
            "name": "Name",
            "dns": "Dns",
            "uri": "URI",
            "requires": "Requires",
            "wants": "Wants",
            "start": "Start Action",
            "stop": "Stop Action",
            "showmain": "On Main Page",
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
            'dns',
            'uri',
            'requires',
            'wants',
            'start',
            'stop',
            'showmain',
        ],
        # A default setting when creating a new entry
        'default': {
            "name": None,
            "dns": "",
            "uri": "",
            "requires": [],
            "wants": [],
            "start": "",
            "stop": "",
            "showmain": False,
        },
        "data": [{
            "name": "Nimbus",
            "dns": "nimbus.aerodesic.net",
            "uri": "APC1:1",
            "requires": ["Nas3"],
            "wants": ["Nas1", "Nas2"],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": True,
        },{
            "name": "Cirrus",
            "dns": "cirrus.aerodesic.net",
            "uri": "APC1:2",
            "requires": ["Nas3"],
            "wants": ["Nas1", "Nas2"],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": True,
        },{
            "name": "Cumulus",
            "dns": "cumulus.aerodesic.net",
            "uri": "APC1:3",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": True,
        },{
            "name": "Nas1",
            "dns": "nas1.aerodesic.net",
            "uri": "APC1:4",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
        },{
            "name": "Nas2",
            "dns": "nimbus.aerodesic.net",
            "uri": "APC1:5",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
        },{
            "name": "Nas3",
            "dns": "nas3.aerodesic.net",
            "uri": "APC1:6",
            "requires": [],
            "wants": ["Gatekeeper"],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
        },{
            "name": "Gatekeeper",
            "dns": "gatekeeper.aerodesic.net",
            "uri": "APC1:7",
            "requires": [ "DmzSwitch", "NasSwitch" ],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
        },{
            "name": "DmzSwitch",
            "dns": "",
            "uri": "APC1:8",
            "requires": [],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
        },{
            "name": "NasSwitch",
            "dns": "",
            "uri": "APC2:1",
            "requires": [],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "showmain": False,
        }],
    }
}
