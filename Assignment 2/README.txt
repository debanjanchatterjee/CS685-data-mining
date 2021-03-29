Hi!

All the necessary scripts and output files(.csv) has been included in the main folder.

The .sh scripts invoke Python(.py) programs from within. Only 2 python libraries have been used: (csv, networkx)
Note: If networkx is not installed, use : pip install networkx (or, pip3 install networkx)


To sucessfully run the scripts: I have already included all the important input files like 'articles.tsv', 'categories.tsv', etc. inside the main folder.


For running the scripts: (Important)

Either run the top level script assign2.sh , which will run all the scripts in order. (Total time taken- under 10 minutes)

or, please maintain the order of exection of the .sh scripts according to the question order in the assignment, I have included a separate script(.sh) for every question. The scripts have been named intuitively, by adding '-generator' to the name of the .csv file it is generating.

For example: article-id-generator.sh generates 'article-ids.csv' (question 1)
category-ids-generator.sh generates 'category-ids'.csv' (question 2) and so on..... (Total: 11 individual scripts for the 11 programming questions respectively)


Reason for matntaining order: There is a large dependecy of the later questions on the outputs of the earlier questions.

Two Additional Remarks:
1) In question5, while findhing the graph compenents, the graph have been assumed to be undirected.
2) In question10, there were some spelling mistakes in Article names, which have been corrected.

The output files have also been added in the main folder.
(Note: I have intentionally left out the headers of the .csv files, as sir said in one of the discussion sessions that including headers is optional and it is upto us.)


The report.tex (along with all the files for compilation as well as the pdf) has been provided in the folder named- 'report'. 

























  
