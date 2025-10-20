
# PUBLIC TRANSIT GUIDANCE

An unified public transit guidance platform for enhancing the experience of the commuters who use public transport.


## MODULES

 - Journey Experience
 - My Journey
 - Chatbot
 - Live Updates


## STEPS TO RUN

### :clipboard: CLONE THE REPOSITORY

Run `git clone https://github.com/Thiru17398/Final_Year_Project.git` to clone this repository


### START THE MAIN APPLICATION
:arrow_forward: Run the Backend of Main App

- Change the directory  `cd 'Main App\backend'`
- Install the dependencies `npm install` (Not Everytime, Only once after cloning) 
- Start the server `nodemon index.js`

:arrow_forward: Run the Frontend of Main App

- Chnage the directory `cd 'Main App\frontend'`
- Install the dependencies `npm install` (Not Everytime, Only once after cloning)
- Run the frontend `npm start`

:link: Main application will be running on [http://localhost:3000](http://localhost:3000)

### START THE CHATBOT

:arrow_forward: Run the Backend of Chatbot

- Change the directory `cd 'ChatBot\Backend'`
- Create a Virtual Environment `python -m venv venv` (Only once)
- Start the Virtual Environment `venv/Scripts/activate` (Whenever running backend run this command)
- Install the packages `pip install -r requirements.txt`
- Run the chatbot backend `python main.py`
- Deactivate Virtual Environment after stopping the backend `venv/Scripts/deactivate.bat`

:arrow_forward: Run the Frontend of Chatbot

- Change the directory `cd 'Chatbot-UI'`
- Run the frontend for the chatbot `npm run dev`

:link: Click here to navigate to Chatbot [http://localhost:3000/chatbot](http://localhost:3000/chatbot)
