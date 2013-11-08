stlviewer
=========

A simple viewer for STL files, powered by [thingiview.js](https://github.com/LongHairedHacker/thingiview.js).


Installation
------------

As a [docker](http://docker.io/) container:

    $ ID=$(docker run -p 5000 -d philippbosch/stlviewer)
    $ docker port $ID 5000
    0.0.0.0:99999

The last command outputs the port (99999) that is bridged to the web server running inside the container.


Usage
-----

Open a URL like `http://yourhost:99999/?stl=http://url.to/your/file.stl` (replace port number) in your browser. 

Optional parameters:

- `objectColor` – surface color of the rendered object as six hex digits without `#` (default: `666666`)
- `backgroundColor` – background color of the scene as six hex digits (default: `CCCCCC`)
- `rotation` – turn rotation on (`=true`) or off (default)
- `cameraView` – one of `top`, `bottom`, `side`, `diagonal` (default)
