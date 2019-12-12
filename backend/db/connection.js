const monk = require("monk");

const connectionString =
  "mongodb+srv://tar:FullySkilled@cluster0-byfy8.mongodb.net/test?retryWrites=true&w=majority";
const db = monk(connectionString);

module.exports = db;
