# Insure BOT (Conversation Bot)

This is an intelligent voice/text-based chatbot built to assist users in [brief use case: e.g., resolving insurance policy queries]. It leverages natural language processing (NLP) for understanding queries and returns accurate, real-time responses.

---

## Features

<ul>
<li>Generate Accuraqte Question according to User Response</li>
<li>Voice Interaction</li>
<li>Response Generate based on content and user profile</li>
<li>Class Based Architecture</li>
<li>Generate a text file of all communication so that text file can be used further for Deep Learning Model Training</li>
</ul>

## Project Structure

InsureBot/
│
├── main.py # Main execution file
├── CustomerData.py # include Customer Data
├── README.me   # Project Documentation
├── requirement.txtx    # Include text file for required python library
├── Helper
|   ├── CheckQuestionExist.py # Check that DB is Compatible or NOT
|   ├── Similarity.py   # Find Similarity of user response with default response
|   ├── voiceRecognition.py # Include Voice Input File
├── MOdelTrainData
|   ├──textData.txt # conatain data of all communication between user and BOT
├── TrainingData
|   ├── AllResponses.py  #Inlcude All Possible Response of user
|   ├── AnserResponse.py    # Include User Response based on Question 
|   ├── Script.py   # Include Rule Base for Make Decision
├── Voice Data  # Inlcude Voice Data Provided audio format

## Setup

### 1. Clone GitRepo

```bash
https://github.com/akashkumar80/InsureBot.git
```

### 2. change directory to project Directory

```bash
cd InsureBot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run ChatBot

```bash
python main.py
```

# Author 

## Akash Kumar
