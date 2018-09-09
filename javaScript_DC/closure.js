// Problem 1

var counter = 0;

function incOne() {
        counter++;
        return counter;
    };

console.log(incOne());
console.log(incOne());
console.log(incOne());
console.log(incOne());


// Problem 2



class Counter {
    constructor(x = 0) {
        this.count = 0;
        this.x = x;
    }
    incOne() {
        this.count++;
        return this.x + this.count;
    }
    incNeg() {
        this.count--;
        return this.x + this.count;
    }
};

let countOne = new Counter(10);
let countTwo = new Counter(10);


console.log(countOne.incOne());
console.log(countOne.incOne());
console.log(countOne.incOne());

// Problem 3

console.log(countTwo.incNeg());
console.log(countTwo.incNeg());
console.log(countTwo.incNeg());



function counter(x) {
    var count = 0;
    var x = x;
    function addOne() {
        count++;
        return x + count;
    }
    return addOne;
    function subOne() {
        count--;
        return this.x + this.count;
    }
    return subOne;
};

var countOne = counter(5);
console.log(countOne());


console.log(countOne);
console.log(countOne.incOne());
console.log(countOne.incOne());



