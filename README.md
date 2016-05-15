Steam Redirector
=========

A quick tool I wrote using Python and Flask that allows you to create a quick landing page that will point users toward the Steam webpage or directly launch the Steam Application

Using this tool
------------
This tool uses URLs as input parameters.  There are three possible input parameters that you can input into the URL.
1) The unique Steam key ID identifier.  For example, the unique steam key ID for the game located at "http://store.steampowered.com/app/367080" is 367080
2) The name of your game. For example, Songbringer
3) An optional key ID for a background image that is hosted on imgur.  For example, for the image URL "http://imgur.com/tGWGLL0", the unique id would be tGWGLL0
The finished built URL will look like: [rooturl].com/SongBringer/367080/tGWGLL0

![alt text](readme_picture.PNG "readme")



Installation
------------

The tutorial referenced above explains how to setup a virtual environment with all the required modules.

The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------

To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment.

