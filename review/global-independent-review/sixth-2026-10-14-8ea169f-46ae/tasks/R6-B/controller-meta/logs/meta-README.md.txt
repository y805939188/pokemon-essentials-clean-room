1: # Pokémon Essentials
2: 
3: Based on Essentials v21.1.
4: 
5: You can build your fangame on top of a fork of this repository. Doing so will let you update your fangame with improvements made to this repo as soon as they are made.
6: 
7: ## Usage
8: 
9: 1. Fork this repo.
10: 2. Get a copy of Essentials v21.1 (a download link cannot be provided here).
11: 3. Clone your forked repo into the Essentials v21.1 folder, replacing the existing files with the ones from the repo.
12: 
13: From here, you can edit this project to turn it into your fangame/develop mods. When this repo is updated, you can pull the changes to update your fork and get the updates into your fangame/modding environment.
14: 
15: ## Scripts
16: 
17: The scripts no longer live in the Scripts.rxdata file. They have been extracted into separate files and placed in the Data/Scripts/ folder (and subfolders within). This makes it easier to work with other people and keep track of changes.
18: 
19: The scripts are loaded into the game alphanumerically, starting from the top folder (Data/Scripts/) and going depth-first. That is, all scripts in a given folder are loaded, and then each of its subfolder is checked in turn (again in alphanumerical order) for files/folders to load/check.
20: 
21: ### Extracting and reintegrating scripts
22: 
23: This repo contains two script files in the main folder:
24: 
25: * scripts_extract.rb - Run this to extract all scripts from Scripts.rxdata into individual .rb files (any existing individual .rb files are deleted).
26:   * Scripts.rxdata is backed up to ScriptsBackup.rxdata, and is then replaced with a version that reads the individual .rb files and does nothing else.
27: * scripts_combine.rb - Run this to reintegrate all the individual .rb files back into Scripts.rxdata.
28:   * The individual .rb files are left where they are, but they no longer do anything.
29: 
30: You will need Ruby installed to run these scripts. The intention is to replace these with something more user-friendly.
31: 
32: ## Files not in the repo
33: 
34: The .gitignore file lists the files that will not be included in this repo. These are:
35: 
36: * The Audio/, Graphics/, Plugins/ and Screenshots/ folders and everything in them.
37: * Everything in the Data/ folder, except for:
38:   * The Data/Scripts/ folder and everything in there.
39:   * Scripts.rxdata (a special version that just loads the individual script files).
40:   * messages_core.dat, which contains common messages and is useful for translation projects.
41: * A few files in the main project folder (two of the Game.xxx files, the RGSS dll file and errorlog.txt).
42: * Temporary files.
