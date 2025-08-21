// Asynchronous callback function

setTimeout(() => {console.log("Task 1");
setTimeout(() => {console.log("Task 2");
setTimeout(() => {console.log("Task 3");
setTimeout(() => {console.log("Task 4");
}, 8000) // Timeout for Task 4
}, 6000) // Timeout for Task 3
}, 4000) // Timeout for Task 2
}, 2000); // Timeout for Task 1

setTimeout(() => {console.log("Wake Up");
setTimeout(() => {console.log("Brush");
setTimeout(() => {console.log("Bath");
setTimeout(() => {console.log("Get ready");
setTimeout(() => {console.log("Go to College");
}, 10000); // Timeout for Go to College
}, 8000) // Timeout for Get ready
}, 6000) // Timeout for Bath
}, 4000) // Timeout for Brush
}, 2000); // Timeout for Wake Up