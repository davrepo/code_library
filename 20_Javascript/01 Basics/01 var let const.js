// ------------- Primitive Data Types -------------
String, Number, Boolean, Null, Undefined, BigInt, Symbol

// when variable is not initialized, it is Undefined type
var foo;    // foo is undefined type
// function returns undefined type if no return value is specified

// ------------- var let const -------------
var foo1 = 1;
var foo1 = 2;   // var can be redeclared
foo1 = 3;       // var can be reassigned

let foo2 = 1;
let foo2 = 2;   // SyntaxError: let can't be redeclared
foo2 = 3;       // let can be reassigned

const foo3 = 1;
const foo3 = 2; // SyntaxError: const can't be redeclared
foo3 = 3;       // TypeError: const can't be reassigned

// ------------- Hoisting -------------
var temp = 1;

tempC();    // 4

console.log(temp);  // 1

function tempC() {
    console.log(temp);      // undefined
    var temp = 2;
    temp = (temp - 1) * 4;
    console.log(temp);      // 4
}


