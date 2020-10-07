console.log("this is tutorial 7");

// ==== function declaration ====
function greet(name, greetText="greetings from javascript"){
    let name1 = "tom";                              // local variable
    console.log(greetText+" "+name)
    console.log(name1+" is a good boy");
}

function sum(a, b, c){
    let d = a + b + c;
    return d;
    // this line will never execute (unreachable code)
    // console.log("function is returned");
}

// ==== variable declaration ====
let name = "hari";
let name1 = "bob";
let name2 = "rohan";
let name3 = "jack";
greetText = "good morning"

// ==== function calling ====
greet(name, greetText);
greet(name1, greetText);
greet(name2, greetText);
greet(name3);

let result = sum(4, 5, 8);
console.log(result);


// console.log(name+" is a good boy");
// console.log(name1+" is a good boy");
// console.log(name2+" is a good boy");
// console.log(name3+" is a good boy");