Steam Redirector
=========

A quick tool I wrote using Python and Flask that allows you to create a quick landing page that will point users toward the Steam webpage or directly launch the Steam Application.

This allows you to send potential users to their actual Steam application, where they're logged in.  This is advantageous, as many users aren't logged into Steam on the webpage, but they are in the application.  This will reduce the friction, and hopefully increase overall conversion.

You can check out a live demo [here](http://steamapps.herokuapp.com/SongBringer/367080/tGWGLL0).

Using this tool
------------
This tool uses URLs as input parameters.  There are three possible input parameters that you can input into the URL.

* The name of your game. For example, Songbringer.
* The unique Steam key ID identifier.  For example, the unique steam key ID for the game located at "http://store.steampowered.com/app/367080" is 367080.
* An optional key ID for a background image that is hosted on imgur.  For example, for the image URL "http://imgur.com/tGWGLL0", the unique id would be tGWGLL0

The finished built URL will look like: [http://steamapps.herokuapp.com/SongBringer/367080/tGWGLL0](http://steamapps.herokuapp.com/SongBringer/367080/tGWGLL0)

![alt text](readme_picture.PNG "readme")

Installation
------------
Clone the repository and push to Heroku.  I've included the Procfiles and requirements.txt.  It should be pretty painless.

How did this project come about?
------------

This project was created at Tool Jam 2016, a hackathon for creating game development tools.

Tool Jam was presented by [Playcrafting](https://www.playcrafting.com/) and [Microsoft](https://developer.microsoft.com/) and took place in San Francisco on May 13th through 15th.

[Click here](https://github.com/TobiahZ/ToolJam2016) to see other Tool Jam 2016 projects.

Video Pitch
------------

[![Final Presnetation: Steam-Redirector](http://video.ch9.ms/ch9/62cd/1806924e-3242-4ef0-b2f8-91fcd92a62cd/tj16steam_Custom.jpg)](https://channel9.msdn.com/Events/ToolJam/2016/Steam-Redirector "Final Presnetation: Steam-Redirector")

Todo
------------
* Code cleanup
* Better error handling
* Fix mobile rendering
