const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const mongoose = require("mongoose");

//mongo connection string
const MONGOURL =
  "mongodb+srv://tar:FullySkilled@cluster0-byfy8.mongodb.net/test?retryWrites=true&w=majority";

const app = express();

mongoose
  .connect(MONGOURL)
  .then(() => console.log("MongoDB Connected!"))
  .catch(error => console.log(error));

app.use(morgan("tiny"));
app.use(cors());
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.json({
    message: "Behold The MEVN Stack!"
  });
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`listening on ${port}`);
});
