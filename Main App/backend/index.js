const express = require("express");
const cors = require("cors");
const path = require("path");
const admin = require("firebase-admin");

const app = express();

app.use(express.json())
app.use(cors())



const serviceAccount = require("./firebase-adminsdk.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://console.firebase.google.com/project/transit-simplified/firestore/databases/-default-/data?fb_gclid=Cj0KCQjws-S-BhD2ARIsALssG0ZVwbSGVDvCgG4YvFsPIPvpFeek4l5JK7eR3OfRaJmvJ7zKaWBk-fMaAroREALw_wcB" // Change to your Firestore URL
});

const db = admin.firestore();

const PORT = 5000;

app.get("/", (req , res) => {
  res.send("Hello World!");
})

app.get("/getAllJourneys" , async (req , res) => {

  var data = [];
  db.collection("journeys").get().then((querySnapshot) => {
    querySnapshot.forEach(async (doc) => {
      data.push(doc.data());
      });
      res.status(200).send(data);
    }).catch(err => {
      console.log('Error getting documents', err);
    })
});

app.post("/postJourney" , (req , res) => {

  const collectionRef = db.collection("journeys");

  var id = null;

  collectionRef.count().get().then(
    (count) => {
      id = count.data().count + 1;
      collectionRef.add({
        id: id,
        ...req.body
      }).then((docRef) => {
        console.log("Document written with ID: ", docRef.id);
        return res.status(200).send({"message " : "inserted"});
    }).catch((error) => {
      return res.status(201).send({"message" : "Unsuccessful"});
      });
      })
  
    });
 


const server = app.listen(PORT,()=>{

    console.log(`Server running on port  ${PORT}`)

});

module.exports = app;