import random
import lxml
import bs4
import requests
import re
import math

genre_scores = {"romance":0, "comedy":0, "action":0, "animation":0, "adventure":0,"sci-fi":0, 
                "horror":0, "drama":0, "thriller":0, "musical":0, "fantasy":0, "war":0, "crime":0, "mystery":0}

movies = {}

#WEB SCRAPING!

links =['https://www.imdb.com/search/title/?genres=comedy&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=romance&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=animation&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=sci-fi&groups=top_250&sort=user_rating,desc'
        'https://www.imdb.com/search/title/?genres=musical&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=fantasy&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=war&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=crime&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?genres=mystery&groups=top_250&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?groups=top_1000&sort=boxoffice_gross_us,desc',
        'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?groups=top_1000']

for link in links:
    
    website =  requests.get(link)
    website = bs4.BeautifulSoup(website.text,"lxml")
    header = website.select('.lister-item-header')
    imdb_movies = []

    for item in header:

        movie = item.getText()

        movie = re.sub(r'\d{1,}\.', '', movie)
        movie = movie.replace('(','')
        movie = movie.replace(')','')
        movie = movie.replace('\n', '')

        movie = movie[:-4:]
        
        if movie[-2] == 'I':
            movie = movie[:-1:]
        
        if movie[-1] == 'I':
            movie = movie[:-1:]

        imdb_movies.append(movie)

    header = website.select('.genre')
    imdb_genres = []

    for item in header:

        global genre_scores

        genre = item.getText()

        genre = genre.replace(',', '')
        genre = genre.replace('\n', '')

        genre = genre.lower()
        
        temp_list = list(genre.split(' '))
        genre_list = []

        for item in temp_list:

            if item == '':
                
                pass

            if item not in genre_scores:
                
                pass

            else:
                
                genre_list.append(item)

        imdb_genres.append(genre_list)

    for movie in imdb_movies:

        global movies

        movies[movie] = imdb_genres[imdb_movies.index(movie)]
        

#DEFINING FUNCTIONS!

def rand_movies(movies):
    
    movies_list = []
    
    for item in movies:
        
        movies_list.append(item)
    
    return random.sample(movies_list, 2)

def get_choice():
    
    global movies
    
    choice = '0'
    
    temp_movies = rand_movies(movies)
    
    while choice not in ['A', 'B']:
        
        choice = input('\n\n[A] {}\n[B] {}'.format(temp_movies[0], temp_movies[1]))
        
        if choice == '':
            
            pass
        
        else:
            choice = choice[0].upper()

    if choice == 'A':
        
        return temp_movies[0]
    
    elif choice == 'B':
        
        return temp_movies[1]
    

def score_alg():
    
    global genre_scores
    global movies
    
    movie_choice = get_choice()
    
    if len(movies[movie_choice]) == 0:
        
        pass
    
    else:
        
        points = round(1/len(movies[movie_choice]),2)

    for genre in movies[movie_choice]:
        
        current_points = genre_scores[genre]
        
        points_given = (1/(math.floor(current_points)+1))
        
        genre_scores[genre] += points_given

def repeat_times():
    
    global genre_scores
    
    repeats = [x for x in range(15, 26)]
    
    repeats = random.sample(repeats, 1)
    
    for i in range(repeats[0]):
        
        score_alg()
        
def order_scores():
    
    global genre_scores
    
    score_list = []
    top_scores = []
    
    repeat_times()
    
    for genre in genre_scores:
        
        score_list.append((genre_scores[genre], genre))
        top_scores.append(genre_scores[genre])
    
    top_scores.sort(reverse=True)
    
    return [top_scores[0], top_scores[1], top_scores[2]]
    
    
def get_genres():
    
    global genre_scores

    top_scores = order_scores()
    
    top_genres = []
    
    for top_genre in top_scores:
        
        for genre in genre_scores:
            
            if genre_scores[genre] == top_genre and genre not in top_genres:

                top_genres.append(str(genre))
                
                break
            
            else:
                
                pass
    
    return top_genres


def get_movies():
    
    global movies
    
    top_genres = get_genres()
    
    top_genres.sort()
    
    movie_list = []
    
    if random.randint(0, 1) == 0:
        
    #Option 1- movies (dict)
        
        movie_dict = {0:[], 1:[], 2:[], 3:[]}

        for movie in movies:

            score = 0

            for genre in top_genres:

                if genre in movies[movie]:

                    score += 1

                else:

                    pass

            movie_dict[score].append(movie)

        movies_list = [movie for movie in movie_dict[3]]

        if len(movies_list) <= 10:

            movie_list.extend(random.sample(movie_dict[2], 5))
            
        if len(movies_list) < 10:

            num_of_movies = 10-len(movies_list)
            
            movie_list.extend(random.sample(movie_dict[1], num_of_movies))

        return movie_list
    
    else:
    
    #Option 2- Random Web Scraping

        for genre in top_genres:
            
            temp_movies = []
            
            link = requests.get('https://www.imdb.com/search/title/?genres={}&groups=top_250&sort=user_rating,desc'.format(genre))
            link = bs4.BeautifulSoup(link.text, "lxml")
            header = website.select('.lister-item-header')
            
            for item in header:

                movie = item.getText()

                movie = re.sub(r'\d{1,}\.', '', movie)
                movie = movie.replace('(','')
                movie = movie.replace(')','')
                movie = movie.replace('\n', '')

                movie = movie[:-4:]

                if movie[-1] == 'I':
                    movie = movie[:-1:]

                if movie[-1] == 'I':
                    movie = movie[:-1:]

                temp_movies.append(movie)
            
            temp_movies = [x for x in random.sample(temp_movies,4)]
            movie_list.extend(temp_movies)
            
        return movie_list


def repeat():
    
    ans = 'temp'
    
    while ans[0].lower() not in ['y', 'n']:
        
        temp = input("\nWould you like to go again? [Y] or [N]")
        
        if temp == '':
            continue
            
        else:
            ans = temp[0].lower()
    
    
    if ans == 'y':
        return True
    else:
        return False    
            
while True:
    
    print('SR2\n020\n\n')
    print('''Welcome to the movie recommendation generator!
    \nEver been on your favourite streaming platform, but you don't know what to watch? No problem!
    \nChoose your favourite movie out of the two options- that's it!
    \nWe will give you movies that you will enjoy based on what you chose!
    \nDone in 2 minutes or less!
    \n\nBeta 0.30''')
    
    best_movies = get_movies()
    
    print('\n\nRemember, give foreign language films a chance; they might surprise you!')
    print('Movies you will love, in no particular order, are:\n')
    
    for movie in best_movies: 
        print(movie)
    
    if repeat():
        pass
    else:
        print('\nThank you for using the movie generator!')
        break