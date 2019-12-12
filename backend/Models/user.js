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
  role: {
    type: String,
    required: true,
    enum: ["employer", "employee"]
  }
});

const bcrypt = require("bcrypt");
let SALT = 10;

//hashing the password before saving
userSchema.pre("save", function(next) {
  var user = this;

  if (user.isModified("password")) {
    bcrypt.genSalt(SALT, function(err, salt) {
      if (err) return next(err);
      bcrypt.hash(user.password, salt, function(err, hash) {
        if (err) return next(err);
        user.password = hash;
        next();
      });
    });
  } else {
    next();
  }
});

userSchema.methods.comparePassword = function(candidate, check) {
  bcrypt.compare(candidate, this.password, function(err, isMatch) {
    if (err) return check(err);
    check(null, isMatch);
  });
};

const User = mongoose.model("User", userSchema);

module.exports = { User };
