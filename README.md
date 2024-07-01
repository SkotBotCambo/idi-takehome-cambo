# IDI Take-Home Task

## Scott Cambo
*The work for the assignment is detailed throughout the code base. Review the project outline below for links to the documentation and reports.*

# Overview:
This take-home assignment is designed to assess your ability to ingest a relatively large dataset & package it in a format that can easily be queried. Please do not take more than 8 hours on this assignment; if you’re not finished after 8 hours of work, please send in what you have. Completing the task fully is not a prerequisite for moving on to the next round of interviews. We want to see how you think about solving a problem and building a working system. Attention to detail and thorough documentation are also very important here. We would strongly prefer you complete this assignment in Python, as that is the language you will be working in most of the time for this position. 

## Task:
In this Google Drive folder, you’ll find two TSV files of tweets about Britney Spears. One is ~50MB and the other is ~500MB. While we’d prefer you use the larger file, please feel free to use the smaller one if your computer can’t handle it. The point of this exercise is not doing everything to the letter. We want to see how well you can do an open-ended task and how effectively you write and explain code. Please feel free to email Alyssa at smith.alyss@northeastern.edu if you have questions about the assignment, using [IDI TAKE-HOME] in the subject line, but please understand that this is left as an open-ended exercise for a reason. 

# Part 1
Ingest the data: figure out a way to put the data in a structure so that you can query it as described in Part 2.

*For part 1, review this notebook: `notebooks/Part_1-Data_Ingestion.ipynb`. To use the notebook in the same jupyter environment that I developed it in, you can run the following commands and steps:*
* *`docker compose up --build`*
* *Navigate to `localhost:8888` in your browser.*

# Part 2
Construct functionality that allows you to query the data. If we search for a term, like “music,” we would like to know some subset of the following:
* How many tweets were posted containing the term on each day?
* How many unique users posted a tweet containing the term?
* How many likes did tweets containing the term get, on average?
* Where (in terms of place IDs) did the tweets come from?
* What times of day were the tweets posted at? 
* Which user posted the most tweets containing the term?

*For part 2, review this notebook: `notebooks/Part_2-Querying_Data.ipynb`.*

# Part 3
Explain to us how we can use your system. We should be able to run this system and query it on our own computers using your instructions. Please explain and justify any important design choices you make.

*For part 3, review this notebook: `notebooks/Part_3-Putting_It_All_Together.ipynb`.*

# Part 4
Send us a link to the Github repo that contains your system (you can email smith.alyss@northeastern.edu with [IDI TAKE-HOME] in the subject line).

# Bells and Whistles
We would be really happy to see any of the following:
* Usage of Docker :white_check_mark:
* Usage of a NoSQL database :white_check_mark:
* Construction of an API, with proper documentation (consider using Flask for this) :white_check_mark:
* Queries that return results quickly (and/or optimizations to make queries return quickly on average) :white_check_mark:
* Thorough documentation :white_check_mark:
* Well-commented code :white_check_mark:
* Tests (consider using pytest/mock/similar packages) :warning: (I started working on this, but ran out of time. Happy to discuss how I would have approached it.)
