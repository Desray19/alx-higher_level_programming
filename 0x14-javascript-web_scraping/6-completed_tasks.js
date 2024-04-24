#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

// Function to handle the request and process the response
function fetchAndProcessTasks (url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }

    if (response.statusCode === 200) {
      const completedTasks = {};
      const tasks = JSON.parse(body);

      tasks.forEach(task => {
        if (task.completed) {
          const userId = task.userId;
          completedTasks[userId] = (completedTasks[userId] || 0) + 1;
        }
      });

      console.log(completedTasks);
    } else {
      console.log('An error occurred. Status code: ' + response.statusCode);
    }
  });
}

// Call the function with the provided URL
fetchAndProcessTasks(url);
