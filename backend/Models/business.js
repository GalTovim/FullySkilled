const mongoose = require("mongoose");

const { User, userSchema } = require("./user");
const { Job, jobSchema } = require("./job");

const businessSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  address: {
    type: String,
    required: true
  },
  owner: {
    type: String,
    required: true
  },
  phone: {
    type: String,
    required: true
  },
  openJobs: [jobSchema]
});

const Business = mongoose.model("Business", businessSchema);
module.exports = { Business };
