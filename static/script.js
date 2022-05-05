let sadList = [' sad',
' guilty',
' ashamed',
'depressed ',
'lonely ',
'bored ',
'sleepy ',
'bashful ',
'stupid ',
'miserable ',
'inadequate ',
'inferior ',
'apathetic ',
]
let angerList =['mad ',
'critical ',
'hateful ',
'rage ',
'angry ',
'hostile ',
'hurt ',
'jealous ',
'selfish ',
'frustrated ',
'furious ',
'irritated ',
'skeptical ',
]
let fearList = ['scared ',
'rejected ',
'confused ',
'helpless ',
'submissive ',
'insecure ',
'anxious ',
'bewildered ',
'discouraged ',
'insignificant ',
'weak ',
'foolish ',
'embarassed ',
]
let joyList = ['joyful ',
'excited ',
'vibrant ',
'energetic ',
'playful ',
'creative ',
'aware ',
'daring ',
'fascinating ',
'stimulating ',
'amused ',
'extravagant ',
'delightful ',
]
let powerfulList = ['powerful ',
'proud ',
'respected ',
'appreciated ',
'hopeful ',
'important ',
'faithful ',
'cheerful ',
'satisfied ',
'valuable ',
'worthwhile ',
'intelligent ',
'confident ',
]
let peacefulList = ['peaceful ',
'content ',
'thoughtful ',
'intimate ',
'loving ',
'trusting ',
'nurturing ',
'pensive ',
'relaxed ',
'responsive ',
'serene ',
'sentimental ',
'thankful ',
]

listOutput = document.getElementById("listOutput")
listOutput1 = document.getElementById("listOutput1")
listOutput2 = document.getElementById("listOutput2")
listOutput3 = document.getElementById("listOutput3")
listOutput4 = document.getElementById("listOutput4")
listOutput5 = document.getElementById("listOutput5")

//function to print Bandlist
function printSadList() {
    listOutput.innerHTML = "";

    for (const feeling of sadList) {

        let checkbox = document.createElement("INPUT");
        checkbox.setAttribute("type", "checkbox");
        
        let label = document.createElement('label');

        //variable called element that makes a new list item
        let listElement = document.createElement('li');
        
        //the checkbox text content is every item in this for-loop
        label.innerHTML = feeling;

        //give every element a class of emotion
        listElement.classList.add('emotions', 'listElement');
        checkbox.name = 'emotions';
        checkbox.value = feeling;
       

        //append the new bandName into the listOutput div
        listOutput.appendChild(listElement);
        listElement.appendChild(checkbox);
        listElement.appendChild(label);
        
        

    }

}
function printFearList() {
    listOutput1.innerHTML = "";

    for (const feeling of fearList) {

        let checkbox = document.createElement("INPUT");
        checkbox.setAttribute("type", "checkbox");
        
        let label = document.createElement('label');

        //variable called element that makes a new list item
        let listElement = document.createElement('li');
        
        //the checkbox text content is every item in this for-loop
        label.innerHTML = feeling;

        //give every element a class of emotion
        listElement.classList.add('emotions', 'listElement');
        checkbox.name = 'emotions';
        checkbox.value = feeling ;
       

        //append the new bandName into the listOutput div
        listOutput1.appendChild(listElement);
        listElement.appendChild(checkbox);
        listElement.appendChild(label);
        
        

    }

}

function printAngerList() {
    listOutput2.innerHTML = "";

    for (const feeling of angerList) {

        let checkbox = document.createElement("INPUT");
        checkbox.setAttribute("type", "checkbox");
        
        let label = document.createElement('label');

        //variable called element that makes a new list item
        let listElement = document.createElement('li');
        
        //the checkbox text content is every item in this for-loop
        label.innerHTML = feeling;

        //give every element a class of emotion
        listElement.classList.add('emotions', 'listElement');
        checkbox.name = 'emotions';
        checkbox.value = feeling;
       

        //append the new bandName into the listOutput div
        listOutput2.appendChild(listElement);
        listElement.appendChild(checkbox);
        listElement.appendChild(label);
        
        

    }

}



function printJoyList() {
    listOutput3.innerHTML = "";

    for (const feeling of joyList) {

        let checkbox = document.createElement("INPUT");
        checkbox.setAttribute("type", "checkbox");
        
        let label = document.createElement('label');

        //variable called element that makes a new list item
        let listElement = document.createElement('li');
        
        //the checkbox text content is every item in this for-loop
        label.innerHTML = feeling;

        //give every element a class of emotion
        listElement.classList.add('emotions', 'listElement');
        checkbox.name = 'emotions';
        checkbox.value = feeling;
       

        //append the new bandName into the listOutput div
        listOutput3.appendChild(listElement);
        listElement.appendChild(checkbox);
        listElement.appendChild(label);
        
        

    }

}

function printPowerfulList() {
    listOutput4.innerHTML = "";

    for (const feeling of powerfulList) {

        let checkbox = document.createElement("INPUT");
        checkbox.setAttribute("type", "checkbox");
        
        let label = document.createElement('label');

        //variable called element that makes a new list item
        let listElement = document.createElement('li');
        
        //the checkbox text content is every item in this for-loop
        label.innerHTML = feeling;

        //give every element a class of emotion
        listElement.classList.add('emotions', 'listElement');
        checkbox.name = 'emotions';
        checkbox.value = feeling;
       

        //append the new bandName into the listOutput div
        listOutput4.appendChild(listElement);
        listElement.appendChild(checkbox);
        listElement.appendChild(label);
        
        

    }

}

function printPeacefulList() {
    listOutput5.innerHTML = "";

    for (const feeling of peacefulList) {

        let checkbox = document.createElement("INPUT");
        checkbox.setAttribute("type", "checkbox");
        
        let label = document.createElement('label');

        //variable called element that makes a new list item
        let listElement = document.createElement('li');
        
        //the checkbox text content is every item in this for-loop
        label.innerHTML = feeling;

        //give every element a class of emotion
        listElement.classList.add('emotions', 'listElement');
        checkbox.name = 'emotions';
        checkbox.value = feeling;
       

        //append the new bandName into the listOutput div
        listOutput5.appendChild(listElement);
        listElement.appendChild(checkbox);
        listElement.appendChild(label);
        
        

    }

}


printSadList();
printFearList();
printAngerList();
printJoyList();
printPowerfulList();
printPeacefulList();
