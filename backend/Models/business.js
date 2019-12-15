const mongoose = require("mongoose");

const User = require("./user");
const Job = require("./job");

const businessSchema = new mongoose.Schema({
  name: {
    type: String,
    require: true
  },
  address: {
    type: String,
    require: true
  },
  owner: {
    type: User,
    require: true
  },
  phone: {
    type: String,
    require: true
  },
  openJobs: [
    {
      type: Job
    }
  ]
});

const Business = mongoose.model("Business", businessSchema);
export default Business;
