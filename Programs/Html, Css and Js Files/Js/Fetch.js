// Make a GET request to GitHub's public Users API
fetch('https://api.github.com/users')

  // Handle the response (fetch gives a Response object, not JSON directly)
  .then(response => response.json())  
  // Convert the raw response body into JavaScript object/array

  // Now 'data' is the parsed JSON (an array of users), so we can use it
  .then(data => console.log(data))    
  // Print the list of users in the console

  // If something goes wrong (like no internet or server error), handle it here
  .catch(error => console.error('Error fetching users:', error));
