Hey, You! Hello there! This programs function is to give information
about HTML tags and their uss/functions. 

CHANGELOG:

	Version_1 (9/15/2017):

		Login Feature added
		Six tags are added:
			<!DOCTYPE html>
			<p>
			<a>
			<h>
			<link>
			<div>
		Startup info added
		Shutdown feature added (Does not shutdown your computer, just the file)
		added TWO users:
			-Admin Chase
			-Guest
		MOVED INTO ALPHA STAGE
			
	Version_2: (9/21/17)
		Created errfile.txt (Contains errs)
		Added error messages
		Restart feature fixed
		Login feature now checks for Username - Pointless at the moment. 
		Compacted Login Feature
		Added protected passwords
		Added keywords:
			<br>
			<button>
			<iframe>
		MOVED INTO BETA STAGE
	
	Version_3: (9/28/17)
		Moved all definitions into definitionsHtml.txt.
		Removed 4 bugs from the code:
			err1: The program ran into an unexpected error, and must now close. Sorry for the inconvenience.
			err2: Could not execute Block() = Function.
			err3: (Partally removed) Incorrect Username.
			err4: Program crashed while Reset was commencing. (%s +% completion)
		added one error for comedic purposes.
		fixed the pointless 46-line deflines block.
		fixed bug where program crashes when a tag that doesn't exist is inputed.
		fixed bug where program crashes when incorrect username is inputed.
		removed errfile.txt.
		log.txt now records ALL sessions, not most recent.
		added keyword(s):
			credits
		changed two keywords:
			/exit --> exit
			/reset --> restart
			
		Secret: There are plans to make a "command mode"	
		
		MOVED INTO INDEV STAGE
	Version_4: (10/16/17)
		re-wrote code to comply with the PEP 8 standards.
		changed this project to OPEN-SOURCE

---------------------------------------------------------------------------
			

	Users:

		Username: Guest
		Password: -
		
		Username: /admin061503
		Password: *************

---------------------------------------------------------------------------
		
How To Use:

	DO NOT open in pythons command prompt, open
	through IDLE or Python shell (IDLE)

	Enter Username on startup, then password. (If set)

	After you are logged in, Enter a tag or command!

List of all keywords:

	<!DOCTYPE html>
	<p>
	<h>
	<a>
	<div>
	<link>
	<br>
	<button>
	<iframe>
	credits
	restart
	exit
		yes
		no

	
