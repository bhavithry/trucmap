# trucmap
TRU Color Map Package

Project description

trucmap

trucmap is a Python package that contains functions to set color map of TRU.

Installation and updating

Use the package manager pip to install trucmap like below. Rerun this command to check for and install updates .

pip install git+https://github.com/bhavithry/trucmap

Usage

Features:

functions.cmap1 --> Primary colour map

functions.cmap2 --> Secondary colour map

Demo of some of the features:

import trucmap

from trucmap import cmap1

cmap1()

This will set the color palette of matplotlib to TRU primary colour map.

cmap2()

This will set the color palette of matplotlib to TRU secondary colour map used for web based applications.

cmap_reset()

This will reset the color palette of matplotlib to its default.


Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

MIT
