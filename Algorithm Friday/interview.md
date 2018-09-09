## 1. What makes Javascript an Object Oriented Language?
- Encapsulation & inheritance.

## 2. What is Object Oriented Programming?

## 3. What are classes?
- The blueprint to build code.

## 4. What is an Object or and Instance?
-Attributes to describe those certain classes.

## 5. How does Javascript differ from other Object Oriented Programming Languages?
- JavaScript is a prototype-based programming language (probably prototype-based scripting language is more correct definition). It    employs cloning and not inheritance. A prototype-based programming language is a style of object-oriented programming without        classes. While object-oriented programming languages encourages development focus on taxonomy and relationships, prototype-based     programming languages encourages to focus on behavior first and then later classify.

## 6. What is the easiest way of defining an object in Javascript?
- Setting var = to either a value or an array.

## 7. How do you add a property to an object?
- var.index = "value";
- var["index"] = "value";

## 8. How do you delete an object property?
- delete var.index

## 9. How do you access properties in Javascript?
- console.log(var.name);
- console.log(var['name']);

## 10. What will happen if an object name starts with a number?
- It will ouptut an error

## 11. How do you access an object name that has a space, i.e. "Birth place"


## 12. What is a primative type?
- string, number, boolean, null, undefined, symbol.

## 13. Can an object be a primative type?
- no, objects can be the instances of primitive type.

## 14. What is the typeOf operator used for?
- typeOf returns which primitive type is being used.

## 15. Are functions objects in Javascript?
- Yes, They are first class objects. They have properties and methods just like any object would.

## 16. Can functions be chained in Javascript?
- Functions can be chained/cascaded (calling on a function one call after the other).

## 17. How do you invoke a function in Javascript?
- Using the call method.

## 18. What is an inner function in Javascript?

## 19. Explain a callback in Javascript.
- A callback function, also known as a higher-order function, is a function that is passed to another function.

## 20. What are the different ways that you can call a function?
- invoking the Function as a function
- using the 'this' keyword
- invoking it as a method
- using a function constructor

## 21. What scope does javascript have?
- Global
- Local

## 22. What is hoisting and how does it work?
- A JavaScript function can be invoked before its declaration. This works because the JavaScript engine implicitly hoists the          function to the top so that they are visible throughout the program.

## 23. What is a "let" variable, introduced in ES6?
- let declares a block scope local variable, optionally initializing it to a value.


## 24. What happens if a "var" or "let" keyword is not defined before a variable?
- The difference between var/function/function* declarations and let/const/class declara­tions is the initialisation.
The former are initialised with undefined or the (generator) function right when the binding is created at the top of the scope. The lexically declared variables however stay uninitialised. This means that a ReferenceError exception is thrown when you try to access it. It will only get initialised when the let/const/class statement is evaluated, everything before (above) that is called the temporal dead zone.


## 25. What is closure in javascript?
- Closures allow JavaScript programmers to write better code. Creative, expressive, and concise. We frequently use closures in JavaScript, and, no matter your JavaScript experience, you will undoubtedly encounter them time and again. Sure, closures might appear complex and beyond your scope, but after you read this article, closures will be much more easily understood and thus more appealing for your everyday JavaScript programming tasks.

## 26. What is the "new" keyword in javascript?
- The new operator creates an instance of a user-defined object type or of one of the built-in object types that has a constructor     function.

## 27. Whati is a prototype?

## 28. Give an example of a prototype.

## 29. Explain a prototype chain.

## 30. What does slice do if no argument is passed?

## 31. What is the keyword "extends"?

## 32. What is Syntatic Sugar in Harmony (ES 6)

## 33. Names some changes that were made from ES5 to ES6.