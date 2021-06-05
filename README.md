How to install

If you don't have python, either...

	1) Run Rou extract the folder to your preferred directory and run the exectuable.

	2) Download Roulette V2 Installer.msi, and install the program into your preferred directory.

If you wish the run the program with python, download the Roulette_GUI_V2 Script.zip and extract all the contents to a folder then run Roulette_GUI_V2.py you will need to download the external python modules listed below.



Additional notes about the program:

External modules used: Pillow, playsound
cx-Freeze was also used to create the build files/installer, however it has no use within the actual program itself.

Art drawn using Python's turtle module and modified in paint.net

Sounds from: https://www.zapsplat.com/

Screenshot of the game: ![1](https://i.imgur.com/GQeLNQt.png)

Issues 

If you somehow run into an issue where your game instantly crashes on startup, delete the Game_data file in your install folder.
Though it shouldn't happen, if it does then that means that your save data was corrupted somehow.


Changelog

3/16/2021: Added roulette wheel to GUI.
		   Changed from Roulette_GUI to Roulette_GUI_V2

3/17/2021: Added buttons to the roulette table
		   Added sound effects

3/18/2021: Game now saves data to show total money lost/gained as well as the number of times you rolled on each number.
		   Fixed buggy data logging.
		   
3/19/2021: Fixed issue where Net Earnings was not displaying the right value.
		   Odds calculation is now out of 37 (This was not accounting for 0 before)
		   Payout rates still do not include zero in the calculations (as it is in real roulette)
3/20/2021: Fixed an issue where entering an empty bug type would cause an error, which also caused the GUI to display funky things.
