# Map-Quest-Python
Program that communicates with the mapquest API.

How to use: Excerpt From Project Description, Written by Alex Thornton

Your program will take input in the following format. It should not prompt the user in any way; it should simply read whatever input is typed into the console, and you should assume that your user knows the precise input format.
An integer whose value is at least 2, alone on a line, that specifies how many locations the trip will consist of.
If there are n locations, the next n lines of input will each describe one location. Each location can be a city such as Irvine, CA, an address such as 4545 Campus Dr, Irvine, CA, or anything that the Open MapQuest API will accept as a location. (The details of what is acceptable as a location is described here. Your program won't need to validate this input, but you'll need to expect that you might not get a valid response if you use something that MapQuest won't accept; you'll need to experiment with the Open MapQuest API's to see how they respond to invalid locations.)
A positive integer (i.e., whose value is at least 1), alone on a line, that specifies how many outputs will need to be generated.
If there are m outputs, the next m lines of input will each describe one output. Each output can be one of the following:
        STEPS for step-by-step directions, meaning a brief description of each maneuver (e.g., a turn, entering or exiting a freeway, etc.) you would have to make to drive from one location to another
        TOTALDISTANCE for the total distance traveled if completing the entire trip
        TOTALTIME for the total estimated time to complete the entire trip
        LATLONG for the latitude and longitude of each of the locations specified in the input
        ELEVATION for the elevation, in feet, of each of the locations specified in the input
