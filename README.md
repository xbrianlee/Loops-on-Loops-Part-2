# Loops-on-Loops-Part-2

Team Members:
* Paul-Valentin Mini
* Max Hufft
* John Kang
* Brian Lee

Instructions:
* How to generate an input file:
	Execute the python program make_tfile.py like so:
	$ python make_tfile.py [word count] [length of a word]

	For our experiments, we used a word count between 500 
	and 50,000 with a length of 5 characters for each word. 

	The program will output a file "input.txt" which can be
	used with various languages and sorting algorithms as 
	instructed bellow.

* Java:
	[text here]

* Javascript:
	To run the program: 
	-Open index.html in a browser, preferably Firefox or Chrome.
	-Generate a test input file using python script project root directory.
 	-Open the Javascript console in the browser.
	-Open the browser's web console
 	-Click the Browse button and open input.txt generated from python script.

* Python:
	The sorting algorithms can be found under "python/".
	Run each algorithm using the following command:
	$ python [python program] [input file]

	Where [python program] is one of the sorting programs
	and [input file] is a text file, most likely "input.txt".

	For example, to run Quicksort on "input.txt" from the 
	sorting algorithms folder:
	$ python quicksort.py input.txt

	Each program will output the runtime in seconds of the 
	algorithm surrounded by quotation marks, like so: 
	"0.0012345678"

	Additionally, you can compile multiple successive runtimes
	into a .csv file using the shell script "createCSV" located 
	at the root of the project folder. The program was used to 
	graph statistics about python runtimes, but it requires 
	manual editing to modify its parameters. I only advise to 
	use it if you know Unix Shell scripts and are curious too 
	see how the data was collected. After setting the approriate
	flags, it can be executed using:
	$ createCSV [python sorting script]

* Haskell:
	[text here]
