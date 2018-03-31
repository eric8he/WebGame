const path = require('path');

module.exports = {
  entry: './app/src/index_handler.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  }
};