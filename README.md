# Movie Recommendation Generator

## Background

Not knowing what to watch is a problem that plagues our society. Too many choices, but nothing seems to pop out at you. With this project, you will know what you will love watch in under 2 minutes. Simply answer with your preference of two options, and using an algorithm, we will determine the movies that you will love! 

## Requirements

- python3
- re
- math
- requests
- bs4
- lxml

You can install the required libraries after installing Python 3 by typing in:

```
pip install 'module_name'
```

at the command line.

## How does it work?

This project works by scraping the IMDb website for movies and their genres. Choosing a film will give its genres a boost, which are added up to tell us your preferred genres of film. We then scrape the website another time to get films of your favourite genres back to you.

## Usage

You can run this file from the terminal like this:

```
python3 --movie_rec.py
```
If you prefer to use Jupyter Notebooks, I have also attached a .ipynb version of the file.

## To-do

Feel free to contribute in any way you wish, but the required updates are below.

- Create GUI for the program, preferably using Tkinter or Django
- Update scoring algorithm 

## Project Difficulty Level

This project uses web-scraping libraries, which are moderately difficult to get a hang of, but it doesn't use any Object Orientated Programming.

### Difficulty Rating: 4/10

Project 1 | SR2020
