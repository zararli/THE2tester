import os
import webbrowser
from subprocess import PIPE, Popen
import time
import platform
import urllib
import sys

#clear screen and print banner
def prepare_screen():
	os.system("cls" if os.name=='nt' else "clear")
	print(bcolors.OKGREEN +
	"""
 _____ _  _ ___ ___   _____ ___  __ _____ ___ ___  
|_   _| || | __(_  | |_   _| __/' _/_   _| __| _ \ 
  | | | >< | _| / /	| | | _|`._`. | | | _|| v / 
  |_| |_||_|___|___|   |_| |___|___/ |_| |___|_|_\ 

	""" + bcolors.ENDC)

#colors to use while prompting 
class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
#helper function to prepare cool messages
def show_message(message, text_type=bcolors.ENDC, clear_before=0,line=0,tab=1,space_before=0):
	if clear_before: 
		print bcolors.ENDC
		prepare_screen()
	print ("\n" * space_before + text_type + tab * "\t" +  message+ "\n" * line)

#converts given parameter to formatted querystring value and opens by default browser of the os
def show_solution(question):
		question = urllib.pathname2url(question)
		Popen(['python -m webbrowser \'' + "https://www.webqc.org/balance.php?reaction=" + question + '\''], stderr=PIPE, stdout=PIPE, shell=True)
		Popen(['python -m webbrowser \'' + "https://www.wolframalpha.com/input/?i=" + question + '\''], stderr=PIPE, stdout=PIPE, shell=True)

#sample format: [<unbalanced equation>, <coefficients of its balanced version>]
samples = [
		["H3PO4 + (NH4)2MoO4 + HNO3 -> (NH4)3PO4(MoO3)12 + NH4NO3 + H2O", "1 12 21 1 21 12"], 
		["Ba3N2 + H2O ->  Ba(OH)2 + NH3", "1 6 3 2"],
		["CaCl2 + Na3PO4 -> Ca3(PO4)2 + NaCl", "3 2 1 6"],
		["FeS + O2 -> Fe2O3 + SO2", "4 7 2 4"],
		["PCl5 + H2O -> H3PO4 + HCl", "1 4 1 5"],
		["As + NaOH -> Na3AsO3 + H2", "2 6 2 3"],
		["Hg(OH)2 + H3PO4 -> Hg3(PO4)2 + H2O ", "3 2 1 6"],
		["HClO4 + P4O10 -> H3PO4 + Cl2O7", "12 1 4 6"],
		["CO + H2 -> C8H18 + H2O", "8 17 1 8"],
		["KClO3 + P4 -> P4O10 + KCl", "10 3 3 10"],
		["SnO2 + H2 -> Sn + H2O", "1 2 1 2"],
		["KOH + H3PO4 -> K3PO4 + H2O", "3 1 1 3"],
		["KNO3 + H2CO3 -> K2CO3 + HNO3", "2 1 1 2"],
		["Na3PO4 + HCl -> NaCl + H3PO4", "1 3 3 1"],
		["TiCl4 + H2O -> TiO2 + HCl", "1 2 1 4"],
		["C2H6O + O2 -> CO2 + H2O", "1 3 2 3"],
		["Fe + HC2H3O2 -> Fe(C2H3O2)3 + H2", "2 6 2 3"],
		["NH3 + O2 -> NO + H2O", "4 5 4 6"],
		["B2Br6 + HNO3 -> B(NO3)3 + HBr", "1 6 2 6"],
		["NH4OH + KAl(SO4)2 + 12H2O -> Al(OH)3 + (NH4)2SO4 + KOH + H2O", "4 1 1 2 1 12"],
		["C2H6O + O2 -> CO2 + H2O", "1 3 2 3"],
		["Fe + HC2H3O2 -> Fe(C2H3O2)3 + H2", "2 6 2 3"],

		["3 4 5", "3 4 5"]  
		]
prepare_screen()
#checks whether the source is available or not
if (os.path.isfile("the2.c") != True):
	show_message("Did you forget to put your the2.c file to this folder?",bcolors.FAIL)
	show_message("I can't believe you!",bcolors.FAIL)
	show_message("Exiting...",bcolors.FAIL)
	show_message("Hint: " + bcolors.ENDC + "copy your the2.c file to " + bcolors.WARNING + os.path.dirname(os.path.realpath(__file__)) + bcolors.ENDC + " directory then run me again",bcolors.OKBLUE,0,2,1,1)
	exit()
#removes compiled file if exists to avoid problems
if (os.path.isfile("the2") == True):
	os.remove("the2")
#compiles file using gcc
p=Popen(['gcc', '-Wall', '-ansi', '-pedantic-errors', '-lm', '-o', 'the2', 'the2.c'], stdout=PIPE, stderr=PIPE)
out, error = p.communicate()
if out != None or error != None:
	prepare_screen()
	show_message("It seems your code having some trouble at compile time.", bcolors.WARNING , 0, 0, 1, 0)
	show_message("1) Stop working and give me some time, I'll be back soon", bcolors.ENDC , 0, 0, 1, 0)
	show_message("2) Continue anyway(Default)", bcolors.ENDC , 0, 0, 1, 0)
	show_message("3) Show me the fine problem :)", bcolors.ENDC , 0, 0, 1, 0)
	answer = raw_input("\tAnswer: ")
	if answer and answer.isdigit():
		if int(answer) == 1:
			show_message("Exiting... I believe you, you can do it!",bcolors.FAIL,0,2,1,1)
			exit()
		elif int(answer) == 3:
			show_message("The fine problem is",bcolors.FAIL,0,0,1,0)
			show_message(out,bcolors.ENDC,0,0,2,0)
			if error: show_message(error,bcolors.ENDC,0,0,1,0)
			show_message("Exiting... Good luck with the problem.",bcolors.FAIL,0,2,1,1)
			exit()
prepare_screen()
type = 0
show_message("How would you want to work?", bcolors.ENDC , 0, 0, 1, 0)
show_message("1) One by one each case (Default)", bcolors.ENDC , 0, 0, 1, 0)
show_message("2) Bulk", bcolors.ENDC , 0, 0, 1, 0)
show_message("3) Exit", bcolors.ENDC , 0, 0, 1, 0)
answer = raw_input("\tAnswer: ")
print bcolors.ENDC
prepare_screen()
if(answer):
	bad_ent = 0
	if answer.isdigit() == True:
		if int(answer) == 1:
			show_message("We're going to inspect each case carefully",bcolors.HEADER)
			type = 1
		elif int(answer) == 3:
			show_message("I cannot understand you humans",bcolors.FAIL,0,2,1,1)
			show_message("Exiting...",bcolors.FAIL,0,2,1,0)
			exit()
		elif int(answer) == 2:
			show_message("Sometimes the questions are complicated and the answers are simple.",bcolors.HEADER,0,1,1)
			type = 2
		else:
			bad_ent = 1
	if(answer.isdigit() != True or bad_ent):
		show_message("Are you bored? Wanna have some fun?",bcolors.HEADER)
		show_message("Consider visiting " + bcolors.ENDC + "http://www.theuselessweb.com", bcolors.HEADER)
		show_message("Exiting...",bcolors.FAIL,0,2,1,1)
		exit()
else:
	show_message("We're going to inpect each case carefully",bcolors.HEADER)
	type = 1
total = len(samples)
index = 0
while index < total:
	smp = samples[index]
	if type == 1: prepare_screen()
	show_message("="*50,bcolors.HEADER)
	show_message("<Testing Equation " + bcolors.BOLD + bcolors.UNDERLINE + str(index) + bcolors.ENDC +"> ",bcolors.WARNING)
	show_message("="*50,bcolors.HEADER)
	input = smp[0]
	cproc = Popen("./the2",stdin=PIPE, stdout=PIPE)
	start_time = time.time()
	out, error = cproc.communicate(input)
	elapsed_time = str(time.time() - start_time)
	show_message("Given input",bcolors.OKBLUE,0,0,1,1)
	show_message(smp[0],bcolors.ENDC,0,0,2,0)
	show_message("Expected output",bcolors.OKBLUE,0,0,1,0)
	show_message(smp[1],bcolors.ENDC,0,0,2,0)
	if(out != smp[1]):
		show_message("Your output",bcolors.OKBLUE,0,0,1,0)
		show_message(out,bcolors.ENDC,0,0,2,0)
		error = "as"
		if error is not None:
			show_message("Runtime Error",bcolors.FAIL,0,0,1,0)
			show_message(error, bcolors.ENDC,0,0,2,0)			
		show_message("Result",bcolors.OKBLUE,0,0,1,0)
		show_message("Failed!",bcolors.FAIL,0,0,2,0)
		if type == 2:
			show_message("Resources may be helpful: ",bcolors.OKBLUE,0,0,1,0)
			show_message("https://www.webqc.org/balance.php?reaction=" + urllib.pathname2url(smp[0]),bcolors.ENDC,0,0,2,0)
			show_message("https://www.wolframalpha.com/input/?i="+ urllib.pathname2url(smp[0]),bcolors.ENDC,0,0,2,0)
	else:
		show_message("Result",bcolors.OKBLUE,0,0,1,0)
		show_message("Succeed!",bcolors.OKGREEN,0,0,2,0)
	show_message("Elapsed Time",bcolors.OKBLUE,0,0,1,0)
	show_message(elapsed_time+ " seconds",bcolors.ENDC,0,0,2,0)
	show_message("="*50,bcolors.HEADER)
	show_message("</Testing Equation " + bcolors.BOLD + bcolors.UNDERLINE + str(index) + bcolors.ENDC +"> ",bcolors.WARNING)
	show_message("="*50,bcolors.HEADER,0,3,1,0)
	if type == 1:
		show_message("What is next?", bcolors.ENDC , 0, 0, 1, 0)
		show_message("1) Go to next equation(Default)", bcolors.ENDC , 0, 0, 1, 0)
		show_message("2) Open the solution of the equation", bcolors.ENDC , 0, 0, 1, 0)
		show_message("3) Exit", bcolors.ENDC , 0, 0, 1, 0)
		answer = raw_input("\tAnswer: ")
		if (answer):
			if answer.isdigit():
				if int(answer) == 1:
					pass #go to next
				elif int(answer) == 2:
					show_solution(smp[0])
					index -= 1
				elif int(answer) == 3:
					show_message("Exiting...",bcolors.FAIL,0,2,1,1)
					exit()

	index += 1
