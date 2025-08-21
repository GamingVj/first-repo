
let marks1 = [50,60,70,80,90];

//Destructuring
let [a,b,c,d,e] = marks1;
console.log(a,b,c,d,e);

// Object Destructuring
let person={uuname:"John", age:30, city:"New York"};
let {uuname, age, city} = person;
console.log(uuname, age, city);


// rest Operator 
let marks = [1,2,3]
function add(a,b,c)
{
    return a+b+c;
}

console.log(add(marks[0],marks[1],marks[2]))
console.log(add(...marks)); //this is a rest operator which allows us to pass an array as arguments

let a1 = [1, 2, 3,];
let b1 = [4, 5, 6];

let merged = [a1,b1]; //this is a nested array
let merged1 = [...a1, ...b1]; //this gets all the values from a and b and stores them in a new array as one .

console.log(merged);
console.log(merged1);

// Spread Operator

let person1 = {uname: "John", age1: 30, email: "john@example.com", phone: "123-456-7890", address: "123 Main St"};
let {uname, age1, ...other} = person1; // "other" will contain the remaining properties and keys .

console.log(uname);
console.log(age1);
console.log("Other is:",other);



