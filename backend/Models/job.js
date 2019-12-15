const mongoose = require("mongoose");

const jobSchema = mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  description: String,
  qualifications: [{ type: String }]
});

const Job = mongoose.model("Job", jobSchema);

export default Job;
