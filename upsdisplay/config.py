DEFAULT_CONFIG = {
    "global": {
        # Global configuration goes here
    },
    "available": [
        # List of available devices seen by scanner
    ],
    "nodes": {
        "schema": {
            "name": str,                # name is a string
            "dns": str,                 # nns is a string (but should be smarter)
            "uri": str,                 # uri is a string (but should be smarter)
            "requres": [ "<nodes>" ],   # requires is a list of <node names>
            "wants": [ "<nodes>" ],     # wants is a list of <node names>
            "start": str,               # start is a string (action function)
            "stop": str,                # stop is a string (action function)
            "main": bool,               # main is a boolean (show on main page if True)
            "choice": [ "Red", "Blue", "Green" ],  # A test object
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
        }],
    }
}
