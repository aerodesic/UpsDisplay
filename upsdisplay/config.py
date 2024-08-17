DEFAULT_CONFIG = {
    "version": 1,
    "global": {
        # Global configuration goes here
    },
    "available": [
        # List of available devices seen by scanner
    ],
    "nodes": {
        "schema": {
            "name": "<unique-node>",                # name is a unique node name
            "dns": "<str>",                         # dns is a string (but should be smarter)
            "uri": "<str>",                         # uri is a string (but should be smarter)
            "requires": "<zero-or-more-node>",      # requires is a list of <node names>
            "wants": "<zero-or-more-node>",         # wants is a list of <node names>
            "start": "<str>",                       # start is a string (action function)
            "stop": "<str>",                        # stop is a string (action function)
            "main": "<bool>",                       # main is a boolean (show on main page if True)
            "choice": [ "<one-of>" "Red", "Blue", "Green" ],   # A test object
            "one-or-more-node": "<one-or-more-node>",
            "one-of-node": "<one-of-node>",
        },
        "headers": {
            "name": "Name",
            "dns": "Dns",
            "uri": "URI",
            "requires": "Requires",
            "wants": "Wants",
            "start": "Start Action",
            "stop": "Stop Action",
            "main": "On Main Page",
            "choice": "Choice",
            "one-or-more-node": "One or More Nodes",
            "one-of-node": "One of Node",
        },
        "data": [{
            "name": "Nimbus",
            "dns": "nimbus.aerodesic.net",
            "uri": "APC1:1",
            "requires": ["Nas3"],
            "wants": ["Nas1", "Nas2"],
            "start": "apcstart",
            "stop": "apcstop",
            "main": True,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "Cumulus",
            "dns": "cumulus.aerodesic.net",
            "uri": "APC1:2",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "Nas1",
            "dns": "nas1.aerodesic.net",
            "uri": "APC1:3",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "Nas2",
            "dns": "nimbus.aerodesic.net",
            "uri": "APC1:4",
            "requires": ["Nas3"],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "Nas3",
            "dns": "nas3.aerodesic.net",
            "uri": "APC1:5",
            "requires": [],
            "wants": ["Gatekeeper"],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "Gatekeeper",
            "dns": "gatekeeper.aerodesic.net",
            "uri": "APC1:6",
            "requires": [ "DmzSwitch", "NasSwitch" ],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "DmzSwitch",
            "dns": "",
            "uri": "APC1:7",
            "requires": [],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        },{
            "name": "NasSwitch",
            "dns": "",
            "uri": "APC1:8",
            "requires": [],
            "wants": [],
            "start": "apcstart",
            "stop": "apcstop",
            "main": False,
            "choice": None,
            "one-or-more-node": [],
            "one-of-node": None,
        }],
    }
}
