# TeamSlothStats
### Application for tracking the stats of the Team Sloth players
---
## Install instructions:

Install Python 3.6 [here!](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe)  
Clone the repository and open up "TeamSloth.py"  
Place your Riot Games API key [(you can acquire that here)](https://developer.riotgames.com/) as a string within the "api_key" variable 

Run the program and input the gameID you want to gain the stats from.  
The program will output the desired information into a CSV file named after the gameID you input

## Team Sloth roster:
Top - TSL smæ  
JG - TSL Cease  
Mid - NewPogChamp  
ADC - TSL Kali  
Supp - Bluesnake  

https://na.op.gg/multisearch/na?summoners=Bluesnake%2CTSL+sm%C3%A6%2CTSL+Cease%2CNewPogChamp%2CTSL+Kali

## How to adapt this script
If you want to adapt this script to your own needs I am all for it. You will need a Riot Games API key [(you can acquire that here)](https://developer.riotgames.com/) and some knowledge how python code although not a ton.  
  
You will want to change each of the classes to search for the ID related to your players. This can be achieved by changing the string passed into the `name = "Bluesnake"` line.  
  
Once all 5 player's names have been added to their respective class, the script is finished and can be used for your purposes. Thanks for using my source code!
