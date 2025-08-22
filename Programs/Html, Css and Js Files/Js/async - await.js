// An asynchronous function to fetch data from the GitHub Users API
async function fetchDataFormApi(params) {
    
    // Send an HTTP GET request to GitHub's public Users API
    // 'await' pauses execution until the response is received
    var res = await fetch('https://api.github.com/users');
    
    // Convert the raw response (which is a ReadableStream) into JSON format
    // Again, 'await' waits until the JSON data is fully parsed
    var data = await res.json();
    
    // Log the fetched data (array of GitHub users) to the console
    console.log(data);
}

// Call the function to actually run it
fetchDataFormApi();
