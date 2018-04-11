var my_module = require('./mathlib')();     //notice the extra invocation parentheses!

my_module.add(5,6);
my_module.multiply(3,5);
my_module.square(3);
my_module.random(1,10)