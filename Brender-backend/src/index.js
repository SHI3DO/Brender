const express = require('express');
const app = express();
const mongoose = require('mongoose');
require('dotenv').config();

mongoose
   .connect(process.env.MONGO_URI)
   .then(() => console.log('MongoDB connected'))
   .catch(err => console.log(err));

app.get('/', (req, res) => {
   res.send('Hello World!');
});

app.listen(5000, function () {
   console.log('start! express server on port 3000');
});
