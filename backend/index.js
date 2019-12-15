const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const mongoose = require("mongoose");

//mongo connection string
const MONGOURL =
  "mongodb+srv://tar:FullySkilled@cluster0-byfy8.mongodb.net/FullySkilled?retryWrites=true&w=majority";

const app = express();

//connecting to database
mongoose
  .connect(MONGOURL)
  .then(() => console.log("MongoDB Connected!"))
  .catch(error => console.log(error));

//importing models
const { User } = require("./Models/user");
const { Business } = require("./Models/business");

app.use(morgan("tiny"));
app.use(cors());
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.json({
    message: "FullySkilled!"
  });
});

//register route
app.post("/api/register", (req, res) => {
  const user = new User({
    username: req.body.username,
    password: req.body.password,
    role: req.body.role
  }).save((err, response) => {
    if (err) res.status(400).send(err);
    else res.status(200).send(response);
  });
});

//login route
app.post("/api/login", (req, res) => {
  //check for username
  User.findOne({ username: req.body.username }, (err, user) => {
    if (!user) res.json({ message: "Login failed, user not found." });

    //if exists compare passwrods
    user.comparePassword(req.body.password, (err, isMatch) => {
      if (err) throw err;
      if (!isMatch) return res.status(400).json({ message: "Wrong password" });
      res.status(200).send("Logged in successfully");
    });
  });
});

//route to add business
app.post("/api/addbusiness", (req, res) => {
  const business = new Business({
    name: req.body.name,
    address: req.body.address,
    owner: req.body.owner,
    phone: req.body.phone
  }).save((err, response) => {
    if (err) res.status(400).send(err);
    else res.status(200).send(response);
  });
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`listening on ${port}`);
});
