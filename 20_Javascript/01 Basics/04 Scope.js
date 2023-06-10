// var keyword
var medicine;   // global scope
function doExperiment() {
    medicine = "Cough Syrup";   // can use medicine here as it is global
    console.log(medicine);
}

// Block scope
let medicine = "Aspirin";   // global scope
function doExperiment() {
    let medicine = "Cough Syrup";   
    if (medicine != 'Aspirin') {
        const medicine = "not aspirin";
        console.log(medicine);    // not aspirin
    }
    console.log(medicine);    // Cough Syrup
}
doExperiment();
// not aspirin
// Cough Syrup
console.log(medicine);    // Aspirin

// Hoisting
var temp = 100;
tempC();
console.log(temp);      // 100

function tempC() {
    // var temp;    // hoisted, this is the effect
    console.log(temp);  // undefined, as temp is hoisted but not assigned a value yet
    var temp = 50;
    temp = (temp - 32) * 5 / 9;     
    console.log(temp);  // 10
}

// undefined
// 10
// 100