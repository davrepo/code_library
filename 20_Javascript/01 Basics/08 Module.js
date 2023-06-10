// https://www.coursera.org/learn/react-basics/supplement/KGYDt/javascript-modules-imports-exports

// 1. Default export
// 2. Named export

// You can have ONE default export per module
// You can have MULTIPLE named exports per module


// 1. Default export (when the function name is the same as the file name)
// Syntax 1:
export default function add(x, y) {
  return x + y;
}

// Syntax 2:
function add(x, y) {
  return x + y;
}
export default add;



// 2. Named export (when the function name is different from the file name)
// Syntax 1:
export function addTwo(a, b) {
    console.log(a + b);
}

export function addThree(a + b + c) {
    console.log(a + b + c);
}

// Syntax 2:
export { addTwo, addThree };


// 3. Importing
// Syntax 1: (from add.js) - file name extension is not required
import add from './add';               // add is default export

// Syntax 2: (from add.js)
import { addTwo, addThree } from './add';   // addTwo and addThree are named exports