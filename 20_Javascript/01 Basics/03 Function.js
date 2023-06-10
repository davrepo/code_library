function add(a, b){
    let c = a + b;
    console.log(c);
}

add(2, 3);  // 5

// Definition expression (Anonymous function)
let add = function(a, b){
    let c = a + b;
    console.log(c);
}

add(2, 3);  // 5

// IIFE (Immediately Invoked Function Expression)
(function(a, b){
    let c = a + b;
    console.log(c);
})(2, 3);  // 5

// Arrow function
let add = (a, b) => {
    let c = a + b;
    console.log(c);
}

// Arrow function (single line)
let add = (a, b) => console.log(a + b);

// Arrow function (single parameter)
let add = a => console.log(a + 2);

// Arrow function (no parameter)
let add = () => console.log(2 + 2);

// Arrow function (this)
let add = {
    a: 2,
    b: 3,
    sum: function(){
        console.log(this.a + this.b);
    }
}

add.sum();  // 5

// Arrow function (this)
let add = {
    a: 2,
    b: 3,
    sum: () => {
        console.log(this.a + this.b);
    }
}

add.sum();  // NaN

// function arguments
function add(){
    let sum = 0;
    for(let i = 0; i < arguments.length; i++){
        sum += arguments[i];
    }
    console.log(sum);
}
output = add(2, 3, 4, 5);  // 14

// Rest parameter (ES6) (array) (single parameter) (last parameter) (optional) 
function add(...args){
    let argSum = args.reduce(function(sum, val) {return sum + val;});
    return argSum;
}
output = add(2, 3, 4, 5);  // 14

// Function constructor
let Dog = function() {let name;};
let firstDog = new Dog();   // firstDog is an instance of Dog
let secondDog = new Dog();  // secondDog is an instance of Dog
firstDog.name = "Fido";
secondDog.name = "Rex";
console.log(firstDog.name); // Fido
console.log(secondDog.name); // Rex

// Prototype, can be used to add properties to all instances of a function
Dog.prototype = {
    speak: function(what) {
        return (console.log(this.name + " says " + what));
    }
}
let thirdDog = new Dog();
thirdDog.name = "Spot";
thirdDog.speak("Woof"); // Spot says Woof


// ---------------- Async, Await, Promise ---------------- //

async function doIt() {
    return console.log("I'm doing it");     // return a promise
}
doIt().then( item => console.log("Glad you did it!") );     // then() is called when the promise is resolved


async function prep() {
    return console.log("Preparing");
}
async function doIt() {
    await prep();   // await is used to wait for the promise to be resolved
    return console.log("Doing it");
}
doIt();     // "Preparing" "Doing it"


// fetching example
async function getSocial() {
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await res.json();
    return data;
}