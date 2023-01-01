## Mood Tracker: a user writes their story


Live site: [Mood Tracker app](https://moodtracker.onrender.com/)

*Note the live site is currently being migrated from Heroku to Render, hence some bugs might appear and require ironing out, bear with me ;)*



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

This tracker would help a user understand themselves better, and increase self awareness / emotional intelligence and the causes behind a high mood or low mood. They can then adjust their lifestyle based on this data.

#### Languages used:

 - HTML/CSS/Javascript
 - Python/Flask/Jinja
 - PostgresQL
 
### Features included in this version:

-  Login page and sign up page

![enter image description here](https://i.imgur.com/M5TiyOA.gif)

- Form for user to log their moods, saved onto the live server database

![enter image description here](https://i.imgur.com/LXRnIlJ.gif)

- Mood history page

![enter image description here](https://i.imgur.com/WMqnnMO.gif)

- Mood history visualised in graph

![enter image description here](https://i.imgur.com/npxAGRv.gif)


## Instructions for installing

 Add `.DS_Store` to the `.gitignore` file.

Add, commit and push as per usual. 

If the local database (schema.sql) has been edited, connect database with Heroku:

    heroku psql

  Reset database:

    heroku pg:reset
    
Copy local database to Heroku:

    heroku pg:push moodtracker DATABASE_URL

## Code snippets

### Sign up form (Flask/Python)

![signup form](https://i.imgur.com/L2DkiO9.png)

### Login form

![enter image description here](https://i.imgur.com/uCdKxiW.png)

### Logging your mood
![enter image description here](https://i.imgur.com/VBVBAim.png)

### Showing your mood history
![enter image description here](https://i.imgur.com/Lm7X9kp.png)

## To be included in future versions:

- Input for user's medications and associated symptoms
- Input for any unhelpful thinking styles

- “Day with the highest mood”, like a high score factor

-   What they ate, exercised, how much they slept
-   Events that have occurred in the day of the user
-   Main panel displaying mood and lifestyle variables on graphs - think "data is beautiful" styles

## Issues to work on:

- Deployment issues with Heroku, page load takes a while on Render, to be investigated; potential move to fly.io (?)
- Improve security measures for users, 
  1. auth0
  2. add validation measures to backend
- Form needs a better flow
- Make it responsive, i.e. mobile friendly

  
