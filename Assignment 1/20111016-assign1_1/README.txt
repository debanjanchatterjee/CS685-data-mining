Hi!

All the necessary scripts and output files(.json and .csv) has been included in the main folder.

The .sh scripts invoke Python programs from within. Only 3 python libraries have been used: (csv, json, statisticts)

Important: To sucessfully run the scripts 4 files must be present (all of them have been included): data-all.json, neighbor-districts-modified.json, coded-edge-graph.json, code-map.json

coded-edge-graph.json- is exactly same as 'neighbor-districts-modified.json', but here the adjacency list contains the unique 3 digit values that I have assigned to each district after correcting names, merging and sorting (ques 1).

code-map.json: Here I am storing the mapping from the modified district name to the 3 digit code for future.


The 3 files: neighbor-districts-modified.json, coded-edge-graph.jon, code-map.json, have been generated using the 3 jupyter notebooks I used to clean and preprocess all the data. They can be found in the folder- Rough Notebooks. (fuzzywuzzy library has been used to match district names). 

Note: Format of districts in neighbor-districts-modified.json- 
districtname_statename/unique3digitcode.


For running the scripts: (Important)

Either run the top level script assign1.sh , which will run all the scripts in order.

or, please maintain the order of exection of the .sh scripts according to the question order in the assignment, 
Reason for matntaining order: Since there is a large dependecy of the later questions on the outputs of the earlier questions, to avoid rewriting same code/recomputing the same values, I've stored the data structures(dicionaries) I used, whenever I felt it'll be required again, as .json files. For example: lookup-ovr.json, (contains same information as cases.overall.csv), neighbor-month(contains same information as neighbor-month)

The report.tex (along with all the files for compilation as well as the pdf) has been provided in the folder named- 'report'. 



  
