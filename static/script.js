let fear = ["Fear", "Scared", "Terror", "Insecure", "Nervous", "Horror", "Frightened", "Helpless", "Panic", "Hysterical", "Inferior", "Inadequate", "Worried", "Anxious", "Mortified", "Dread"]
let anger =["Anger", "Rage", "Exasperated", "Irritable", "Envy", "Disgust", "Hate", "Hostile", "Agitated", "Frustrated", "Annoyed", "Aggravated", "Resentful", "Jealous", "Contempt", "Revolted"]
let love = []
let joy = ["Joy", "Content", "Happy", "Cheerful", "Proud", "Optimistic", "Enthusiastic", "Elated", "Enthralled", "Pleased", "Satisfied", "Amused", "Delighted", "Jovial", "Blissful", "Triumphant", "Illustrious", "Eager", "Hopeful", "Excited", "Zealous", "Euphoric", "Jubilation", "Enchanted", "Raptured"]
let sadness = ["Sadness", "Suffering", "Disappointed", "Shameful", "Neglected", "Despair", "Agony", "Hurt", "Depressed", "Sorrow", "Dismayed", "Displeased", "Regretful", "Guilty", "Isolated", "Lonely", "Grief", "Powerless"]
let surprise = []


function dialog() {    
    let dialog = document.getElementById('emotionWheel');

    document.getElementById('show').onclick = function() {    
        dialog.show();    
    };    
    document.getElementById('hide').onclick = function() {    
        dialog.close();    
    };    
};   

