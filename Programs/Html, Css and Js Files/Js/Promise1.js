// A helper function that creates a delay for a given task
function delay(task, ms) {
    return new Promise((resolve) => {  // Return a promise (needed for async operations)
        setTimeout(() => {             // setTimeout simulates the delay
            console.log(task);         // Print the task name after the delay
            resolve();                 // Resolve the promise so the next task can run
        }, ms);
    });
}

/*
   -------------------
   MORNING ROUTINE FLOW
   -------------------
   Uses 'delay' to simulate a sequence of daily routine tasks.
   Each ".then()" ensures the next task starts only after the previous one finishes.
*/
delay("Wake Up", 2000)                   // Wait 2 seconds, then log "Wake Up"
    .then(() => delay("Brush Teeth", 1000))   // Wait 1 second, then log "Brush Teeth"
    .then(() => delay("Take a Shower", 3000)) // Wait 3 seconds, then log "Take a Shower"
    .then(() => delay("Get Dressed", 2000))   // Wait 2 seconds, then log "Get Dressed"
    .then(() => delay("Have Breakfast", 1500))// Wait 1.5 seconds, then log "Have Breakfast"
    .then(() => delay("Leave for Work", 2000))// Wait 2 seconds, then log "Leave for Work"
    .catch((error) => console.error("Error:", error)); // Handle any potential error


/*
   -------------------
   FOOD DELIVERY FLOW
   -------------------
   Another sequence using the same 'delay' function
   to simulate the process of preparing and delivering food.
*/
delay("Wake Up", 2000)                        // Wait 2 seconds, then log "Wake Up"
    .then(() => delay("Take Order", 1000))    // Wait 1 second, then log "Take Order"
    .then(() => delay("Get the Ingredients", 2000)) // Wait 2 seconds, then log "Get the Ingredients"
    .then(() => delay("Prepare Food", 1500))  // Wait 1.5 seconds, then log "Prepare Food"
    .then(() => delay("Pack the food", 2000)) // Wait 2 seconds, then log "Pack the food"
    .then(() => delay("Deliver the food", 3000)) // Wait 3 seconds, then log "Deliver the food"
    .catch((error) => console.error("Error:", error)); // Handle any potential error
