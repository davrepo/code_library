// in package.json, correct   "scripts": {"test": "jest"}, to "jest"

const { default: TestRunner } = require('jest-runner');
const addFive = require('./07a UnitTest.js');

test('adds 5 to 3 to equal 8', () => {
    expect(addFive(3)).toBe(8);
});

// then in command line run:
// npm run test
