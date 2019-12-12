const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const mongoose = require("mongoose");

//mongo connection string
const MONGOURL =
  "mongodb+srv://tar:FullySkilled@cluster0-byfy8.mongodb.net/test?retryWrites=true&w=majority";

const app = express();

//connecting to database
mongoose
  .connect(MONGOURL)
  .then(() => console.log("MongoDB Connected!"))
  .catch(error => console.log(error));

//importing models
const { User } = require("./Models/user");

app.use(morgan("tiny"));
app.use(cors());
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.json({
    message: "Behold The MEVN Stack!"
  });
});

app.post("/register", (req, res) => {
  const user = new User({
    username: req.body.username,
    password: req.body.password,
    userType: req.body.type
  }).save((err, response) => {
    if (err) res.status(400).send(err);
    else res.status(200).send(response);
  });
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`listening on ${port}`);
});
