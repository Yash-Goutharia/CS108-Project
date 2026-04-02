# CS108-Project-Spring 2025-26
## Mini Game Hub using Pygame
## Modules
<ul>
<li>pygame-ce - the standard library used to programme games in python</li>
<li>sys - module used to interpret the arguements from command line</li>
<li>numpy - standard python library containing various functions related to multi dimensional arrays </li>
<li>matplotlib - library used to draw and understand various graphs and charts in python </li>
<li>pathlib - standard library for handling filesystem paths</li>
<li>time - module that allows us to work with various time controls and its functions </li>
</ul>
<br>

## Table of Contents

1.[Introduction](#introduction)<br>
2.[Directory Structure](#directory-structure)<br>
3.[Implementation](#implementation)<br>

## Introduction
Mini game hub is a collection of three games tictactoe, othello and connect4 that will be implemented in this project using specifically using Python, Pygame module and Bash
## Directory Structure
The Directory hub structure is given below:
```
hub/
    ├── main.sh
    ├── game.py
    ├── leaderboard.sh
    ├──games
         ├── tictactoe.py
         ├── connect4.py
         ├── othello.py
    ├── users.tsv
    |__ history.csv
```
main.sh - for user authentication of the two players <br>

game.py - will using pygame and use a base class to implement the three games <br>

leaderboard.sh - contains table showing game statistics of winner and loser data <br>

games folder - contains the three individual files for each game that will contain their definition of the game board class <br>

users.tsv - contains the user and password data <br>

history.csv - contains game stat row data of each game showing winner, loser, Date and game time<br>


## Implementation
i) User authentication using main.sh
Starting from authentication of 2 players using shell scripting , we are going to take 2 user inputs using commands like "read" and then search our data base for if the 
username pre-exists using commands like "grep". Next we are going to take in a password and encrypt it using SHA256 hash algorithm and save the details of log in in our 
file users.tsv to register the user. That marks the finishing of our authentication. 
