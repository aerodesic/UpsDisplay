from DistUtilsExtra.auto import setup
from distutils.command.install import install
import os

PACKAGE="upsdisplay"
VERSION="1.0"

# In case we need hooks
class post_install(install):
    def run(self):
        install.run(self)

setup(
    name              = PACKAGE,
    author            = "Gary Oliver",
    author_email      = "go@robosity.com",
    url               = "https://www.robosity.com",
    version           = VERSION,
    packages          = [ "upsdisplay" ],
    package_data      = { "upsdisplay": [ "bitmaps/upsdisplay.png", ] },
    license           = "Copyright 2021, Gary Oliver",
    description       = "UPS and PDU display",
    long_description  = open("README.md").read(),
    data_files        = [
        ("/usr/bin",                         [ "upsdisplay/upsdisplay" ]),
        ("share/bitmaps",                    [ "bitmaps/upsdisplay.png", ] ),
        ("share/upsdisplay",                 [ "extra/COPYING", ] ),
    ],
    cmdclass = { 'install': post_install },
)
