// ---------------- Parse JSON ----------------
// JSON.parse() method parses a JSON string, constructing the JavaScript value or object described by the string.
const jsonStr = '{"result":true, "count":42}';
const obj = JSON.parse(jsonStr);
console.log(obj.count);    // 42

// ---------------- convert Object to JSON ----------------
// JSON.stringify() method converts a JavaScript object or value to a JSON string
const data = {firstName: 'John', lastName: 'Doe'};
JSON.stringify(data);   // '{"firstName":"John","lastName":"Doe"}'