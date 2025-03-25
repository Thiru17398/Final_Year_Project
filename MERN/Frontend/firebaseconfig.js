// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyARN3JCrDdQ44LjA5EtUDLpBgYy7whmXJE",
  authDomain: "transit-simplified.firebaseapp.com",
  projectId: "transit-simplified",
  storageBucket: "transit-simplified.firebasestorage.app",
  messagingSenderId: "995369226319",
  appId: "1:995369226319:web:96289e9e7c6c34f2279a3a",
  measurementId: "G-XT9FDN4B0N"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);