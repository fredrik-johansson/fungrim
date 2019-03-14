const katex = require('katex');

// https://katex.org/docs/options.html

var display = (process.argv[2] == 'display');
var instring = process.argv[3];

var html = katex.renderToString(instring, {
    throwOnError: false,
    displayMode: display,
});

process.stdout.write(html + '\n');

