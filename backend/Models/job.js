const mongoose = require("mongoose");

const jobSchema = mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  description: String,
  qualifications: [String]
});

const Job = mongoose.model("Job", jobSchema);

module.exports = { Job, jobSchema };
