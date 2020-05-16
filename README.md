# Arts Search Bot Tool
A tool built with Python and Selenium for automaticg a search for all galleries, museums and art schools in a given city. Search attempts to find website, email and physical addresses.

<img src="https://www.stayconnect.info/wp-content/uploads/2020/03/Search-engine-robot-min.jpg" alt="" height="275px"/>

### Non-Functional Goals
1. Help artists compile lists of galleries, museums, art schools and / or artists in a given area to aid and empower their studio practice.

### Functional Goals
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


## Example Images:

<br><br>
<img src="https://raw.githubusercontent.com/tombetthauser/image_library/master/Screen%20Shot%202020-05-16%20at%208.51.57%20AM.png">

The search tool running independently searching for Chicago art galleries.

<br><br>
<img src="https://raw.githubusercontent.com/tombetthauser/image_library/master/Screen%20Shot%202020-05-16%20at%208.52.54%20AM.png">

Sample csv data output for galleries in Madison, Wisconsin.

***

## How to Use the Tool:
1. Download and run the seperate **arts_installer** tool linked (here)[https://tombetthauser.github.io/arts_installer/installer.sh]
2. Open your command line application (Terminal on MacOS), paste the following and hit enter to run the installer.
```
bash ~/Downloads/installer.sh
```
3. Install the Chromium tool in your Chrome web browser.
4. Download this GitHub project with the link above.
5. Paste the following in your command line and hit enter.
```
python3 ~/Downloads/arts_citysearch/search.py
```
6. You will be prompted to enter a city, hit enter and allow the search to run.
7. Depending on the city you enter the search could take seconds or hours to catalogue all gallery data.
8. When the search is complete you will find a csv data file in the project folder.
```
The data is all yours, now find something cool to do with it!
```
