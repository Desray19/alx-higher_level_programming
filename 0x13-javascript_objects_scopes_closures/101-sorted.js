#!/usr/bin/node
const dict = require('./101-data').dict;

const totlst = Object.entries(dict);
const val = Object.values(dict);
const valq = [...new Set(val)];
const newdict = {};
for (const j in valq) {
  const list = [];
  for (const k in totlst) {
    if (totlst[k][1] === valq[j]) {
      list.unshift(totlst[k][0]);
    }
  }
  newdict[valq[j]] = list;
}
console.log(newdict);
