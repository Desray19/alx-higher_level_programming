#!/usr/bin/node
const Arg = process.argv[2];
if (Arg) {
	console.log(Arg);
} else {
	console.log('No argument');
}
