// making a copy of an object in javascript without dereferencing

var obj1 = {a:1, b:2, c:3};
var obj2 = obj1;
obj2.a = 4;
obj1.a;     // 4

var obj3 = {a:1, b:2, c:3};
var obj4 = JSON.parse(JSON.stringify(obj3));
obj4.a = 4;
obj3.a;     // 1

const obj5 = structuredClone(obj3);
obj5.a = 4;
obj3.a;     // 1

