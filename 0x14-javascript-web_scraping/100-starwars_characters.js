#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dataChar = data.characters;
  for (const i of dataChar) {
    request.get(i, (err, res, b) => {
      if (err) {
        console.log(err);
      }
      const data = JSON.parse(b);
      console.log(data.name);
    });
  }
});
