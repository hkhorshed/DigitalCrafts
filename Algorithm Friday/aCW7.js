// Algorithm Challenge
// Given a list of numbers find the number of pairs that add to 0. Numbers are unique and will not repeat.
//      Example: [-2, 1, 0, 2] => 1 pair since only -2 + 2 = 0

var numberPairs = [-5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5];
var pairsZero = [];

function zerosum(numberPairs) {
   sum = 0;

    for (i = 0; i < numberPairs.length; i++) {
        for (j = i + 1; j < numberPairs.length; j++) {
            sum = numberPairs[i] + numberPairs[j];
            if (sum == 0) {
                pairsZero.push('a');
            } else {

            }
        }
        }
        console.log(pairsZero.length);
    };

zerosum(numberPairs);




