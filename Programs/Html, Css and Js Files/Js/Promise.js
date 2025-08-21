// Variable to store admin status; initially set to true
let isAdmin = true;

// Function that returns a Promise to check if user is an admin
function checkAdmin() {
  return new Promise((resolve, reject) => {
    if (isAdmin) {
      // If user is admin, resolve the promise and call greet()
      resolve(greet());
    } else {
      // If user is NOT admin, log message and reject the promise
      // reject() gets called with the return value of console.log (undefined)
      reject(console.log("User is not an admin"));
    }
  });
}

// Function to greet the admin user by logging a welcome message
function greet() {
  console.log("Welcome Admin");
}

// Call checkAdmin to check admin status
// If promise resolves (user is admin), then log "Checking All User status"
// If promise rejects (user is not admin), then log "He is not Admin"
checkAdmin()
  .then(() => {
    console.log("Checking All User status");
  })
  .catch(() => {
    console.log("He is not Admin");
  });
