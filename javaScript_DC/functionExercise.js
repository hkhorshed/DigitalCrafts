//   Positive Numbers

var myArray = [-5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5];

function positiveNmubers(num) {
    return num > 0;
}

function positiveNmubersOutput() {
    var posArray = myArray.filter(positiveNmubers);
    console.log('The positive values: ' + posArray);
}

positiveNmubersOutput();

var evenArray = [-5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5];


function evenNumber(num) {
    return num % 2 == 0;
}

function evenNumbersOutput() {
    var evArray = evenArray.filter(evenNumber);
    console.log('The even numbers: ' + evArray);
}

evenNumbersOutput()


console.log(positiveNmubers(myArray));

// square the Numbers

var squareArray = [-5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5];

function squareNumberOutput(num) {
    return num * num;
}
arraySquare = squareArray.map(squareNumberOutput);
console.log(arraySquare);



//   Cites I

var cities = [ { name: 'Los Angeles', temperature: 60.0}, { name: 'Atlanta', temperature: 52.0 }, { name: 'Detroit', temperature: 48.0 }, { name: 'New York', temperature: 80.0 } ];

    var arrayTemp = cities.filter(function(tempRat) {
        if (tempRat ["temperature"] < 70) {
            return tempRat;}   
        }
    );

console.log(arrayTemp);

    var citiesArray = cities.map(function(city) {
        return (city['name']);
        }
    );

console.log(citiesArray);

// Good Job

var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];

function goodJob(name) {
    people.map(function(name) {     
    console.log('Good Job ' + name + '!');
});
}
goodJob()

// Sort an Array

var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];

function inOrderList() {
    people = people.sort();
    console.log(people);
};

inOrderList();

// Sort an Array 2

function incOrder(people) {
    return people.sort(function(a , b) {
        return a.length - b.length;
    });
}

console.log(incOrder(people));

// Sort an Array 3

var mats = [ [1 , 3 , 4] , [2 , 4 , 6 , 8], [3 , 6] ];

function sortArray3(mats) {
    return mats.reduce(function(a, b){
        return a+b;
        });
    
}

console.log(sortArray3(mats));

// Call Three Times

function fun() {
    console.log('Hello World')
}

function call3Times(fun) { 
    fun();
    fun();
    fun();
}

call3Times(fun);

// n Times
function fun() {
    console.log('Hello World')
}

function callNTimes(n , fun) {
    var x = n;
    for (n = 0; n < x; n++) {
        fun();
    }
}

callNTimes(8 , fun);

// Sum Array

var arraySum = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10];

function sum() {  
    var sumArray = arraySum.reduce(function(a , b) {
        return a + b;
    });
    console.log(sumArray);
};

sum();

// Acronym
var wordsArray = ['Hello' , 'ugly' , 'self' , 'sacrificing' , 'egotistical' , 'intellectual' , 'ned' ];

function acr() {  
    var acrArray = wordsArray.reduce(function(a , b) {
        return {x : a.x  + b[0]};
    });
    console.log(acrArray);
};

acr();

