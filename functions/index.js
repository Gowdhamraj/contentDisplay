const functions = require('firebase-functions');
const express = require('express');
const app = express();

// Import your Flask app and mount it at a specific route
const flaskApp = require('./flask-app'); // Create flask-app.js

app.use('/flask', flaskApp);

exports.app = functions.https.onRequest(app);