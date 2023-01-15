function counter() {
    var count = 0;
    return function () {
        console.log(++count);
    }
}

let steps = counter();
steps();    // 1
steps();    // 2

// ------------------------------------ //

function myObject() {
    let myValue = 1;
    return {
        display: () => console.log(myValue),
        increment: () => myValue++,
    }
}

let obj = myObject();
obj.display();  // 1
obj.increment();
obj.display();  // 2

let obj2 = myObject();  // new object
obj2.display(); // 1