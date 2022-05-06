## Mood Tracker: a user stores their story

A user wants to track their mood to know what variables affect it, and use it to find out what correlates with mood. 
This may include: 
- Diet  
- Exercise  
- Sleep  
- Past stressors bothering them now  
- Future stressors bothering them now  
- Past activities elevating their mood  
- Future scheduled activities elevating their mood  
- User-added variables
- Thinking styles that affect their mood

This tracker would help a user understand themselves better, and increase self awareness / emotional intelligence and the causes behind a high mood or low mood. They can then adjust their lifestyle based on this data

# Things included in this version:

Create a table for user profiles  

-   Sign up page
-   Login page

Create database for moodtracker  
-  1 table for moods
-  Print tracked moods onto page - with time and date?

-   Mood tracker form

-   Links into database




Join tables

-   Side panel displaying

# To be included in future versions:

   “Day with the highest mood”, like a high score factor

-   What they ate, exercised, how much they slept
-   Special activities

-   Main panel displaying mood on a graph - think "data is beautiful" styles

  

# Instructions for installing

 Add `.DS_Store` to the `.gitignore` file.


  

Add, commit and push as per usual. 

  

Connect database with Heroku:

    heroku psql

  Reset database:

    heroku pg:reset
    
Copy local database to Heroku:

    heroku pg:push moodtracker DATABASE_URL
