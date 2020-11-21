# Zoom-bot
A python boot to automatically attend


This bot can automatically join a zoom meeting at a specified time.

To run this in your pc, these are the reqiurements

1.chromedriver
2.Python version3

To download the chromedriver: 
 Go to https://chromedriver.chromium.org/downloads 
 and select the version matching with your chrome browser and then install in the same directory as the program.

Reqiured python libraries for this program

1.selenium
  To install this, copy this command( pip install selenium )and paste it in your command prompt.

The remaining libraries are pre installed in python.

If the program connot find the csv file then provide the full link.For example "E:\\Zoom bot\\Meeting_link.csv"

In the csv file provide the details in the following format
<Time in 24 format.Example 13:00>,<full meeting link>
<2nd meeting time>,<2nd meeting link>
and so on.

NOTE:

1.Sometimes it may fail if the network is too slow.
2.Make sure that the Zoom is not running in tha background by checking in the tray icons.
