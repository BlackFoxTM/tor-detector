prompt = require("prompt-sync")();
color = require("cli-color");
tor = require("istorexit");


console.log(color.green("Welcome to this script \n\nCoded By : Maximum Radikali"));

var ip = process.argv.slice(2)[0];

tor(ip).then(console.log);



