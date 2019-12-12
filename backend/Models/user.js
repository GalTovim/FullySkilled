const mongoose = require("mongoose");

const userSchema = mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: 1
  },
  password: {
    type: String,
    required: true,
    minlength: 6
  },
  userType: {
    type: String
  }
});

const User = mongoose.model("User", userSchema);

module.exports = { User };
