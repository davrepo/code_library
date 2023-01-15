// ------------- Selectors -------------
document.querySelector("h1").style.color = "red";
document.querySelectorAll("button")[1].style.color = "yellow";
document.getElementById("btn").style.color = "green";
document.getElementsByClassName("btn")[0].style.color = "blue";

// ------------- Events -------------
// addEventListener
// add an event listener to the body element that will log "clicked the body" to the console when the body is clicked
const target = document.querySelector("body");

function handleClick() {
    console.log("clicked the body");
}

target.addEventListener("click", handleClick);

// onclick attribute (not recommended)
// add an event listener to the h1 element that will log "clicked the h1" to the console when the h1 is clicked
<h1 onclick="handleClick2()">Example</>
function handleClick2() {
    console.log("clicked the h1");
}

// ------------- Create Element -------------
// method 1
let answer = prompt('What is your name?');
if (typeof(answer) === 'string') {
    var h1 = document.createElement('h1')
    h1.innerText = answer;
    document.body.innerText = '';
    document.body.appendChild(h1);
}

// method 2, better
var h1 = document.createElement('h1')
h1.innerText = "Type into the input to make this text change"

var input = document.createElement('input')
input.setAttribute('type', 'text')

document.body.innerText = '';
document.body.appendChild(h1);
document.body.appendChild(input);

input.addEventListener('change', function() {
    h1.innerText = input.value
})