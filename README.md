# Arts Search-bot Tool
A tool built with Python and Selenium for automaticg a search for all galleries, museums and art schools in a given city. Search attempts to find website, email and physical addresses.

<img src="https://www.stayconnect.info/wp-content/uploads/2020/03/Search-engine-robot-min.jpg" alt="" height="275px"/>

### Non-Functional Goals
1. Help artists compile lists of galleries, museums, art schools and / or artists in a given area to aid and empower their studio practice.

### Minimum Functional Goals
1. Takes input of a city from the user.
2. Finds a list of results from search for 'art gallery'.
3. Catalogues adresses, phone numbers, websites for galleries.
4. Outputs csv file with this data.

### Stretch Functinoal Goals
1. Find and output artist list from gallery website.
2. Catalogues images of galleries and artworks from gallery artist pages.
3. Matches result images to custom preferences using TensorFlow.
4. Search gallery websites for email contact and artists names.
5. Search individual artist sites for image and contact information.
6. Find artist cv if present and search for education / more gallery names.
7. Break off functionality into arts_artistsearch and arts_gallerysearch classes.
8. Give them the ability to instantiate one another for indefinite search sessions.


***


# Example Images:

<img src="https://raw.githubusercontent.com/tombetthauser/image_library/master/Screen%20Shot%202020-05-16%20at%208.51.57%20AM.png">

The search tool running independently searching for Chicago art galleries.

<br>
<img src="https://raw.githubusercontent.com/tombetthauser/image_library/master/Screen%20Shot%202020-05-16%20at%208.52.54%20AM.png">

Sample csv data output for galleries in Madison, Wisconsin.

# How to Use the Tool:
```
Note that for now this app is only set up to work with Unix based systems (MacOS and Linux).
Sorry in advance! 😕
```
1. Download the zipped version of the project folder and Google Chrome if you don't already have it...

 ---> [download arts_webscraper.zip]()
 ---> [download Google Chrome]()

2. Go to your downloads folder and double click the arts_webscraper.zip file to uncompress it.
3. Open the folder and **double click the arts_webscraper.command file to start** the application.

## If you encounter an issue...
1. If you get a popup after you double-click the application file about permissions need to be changed, open up your Terminal application (hit command + space, then type "Terminal", then hit enter).
2. Then paste the following code into your command line...
```
chmod u+x ~/Downloads/arts_webscraper/arts_webscraper.command
```
3. This will let the computer know you want to be able to open the app directly.
4. If you're a regular Terminal user make sure that file path there makes sense.
5. You can also open the file directly through Terminal with this command...
```
bash ~/Downloads/arts_webscraper/arts_webscraper.command
```
6. If it still wont open for some reason give up and forget any of this ever happened, this tool is still under construction!
7. **Please let me know if you have any trouble** so I can fix it!..
```
tombetthauser@gmail.com / twitter: @tombetthauser
```
## As it's opening up...
1. Before starting the application will check to see if you have access to the following tools...
```
• python3 –– pre-installed on most Macs
• chromedriver –– an extension to connect to the webscraper
• webdriver –– to connect python to the web browser
```
2. You might be asked for your main password if needed during these downloads.
3. If you already have these set up you can directly open the application in Terminal...
```
python3 ~/Downloads/arts_dataexplorer/frontend.py
```

## Once you've got the application open...
1. Enter a city and watch it go!
2. In this less-than-perfect version of the tool you have to let it finish.
3. Once it finishes it will output a data file (.csv) that will contain all the galleries in your input city.
4. You can import this into excel to expore it.
```
Thanks for checking out the tool, hope it helps you do something cool! 🎉
```
***  

# Project Details
<img src="https://selenium-python.readthedocs.io/_static/logo.png" height="175px"> 

This project was built with **Python** primarily using the **selenium** library in conjunction with the **chromium** tool to interface with the Google Chrome web browser. The seperate installer file was written specifically for this project in **bash** shell script.

This was originally developed as two day project by [Tom Betthauser](http://www.tombetthauser.com/) in 2020.  

***
