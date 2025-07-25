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

```bash
InsureBot/
├── main.py                        # Main execution file
├── CustomerData.py                 #Conatins Data Of User from whom we want to connect
├── CustomerData.py               # Includes Customer Data
├── README.md                     # Project documentation
├── requirements.txt              # Required Python libraries
│
├── Helper/                       
│   ├── CheckQuestionExist.py     # Checks if DB is compatible
│   ├── Similarity.py             # Finds similarity between user and default responses
│   └── voiceRecognition.py       # Handles voice input
│
├── ModelTrainData/
│   └── textData.txt              # Logs all communication between user and bot
│
├── TrainingData/
│   ├── AllResponses.py           # All possible user responses
│   ├── AnserResponse.py          # Responses based on specific questions
│   └── Script.py                 # Rule-based decision-making engine
│
└── VoiceData/                    # Folder for storing voice data (audio files)
```

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

### 4 Save Data of Customer

```bash
customer_data = {
    "policy_holder_name" : "Akash Kumar",
    "policy_number" : "21201",
    "product_name" : "InsureBot",
    "policy_start_date" : "21 march 2025",
    "total_premium_paid" : "0",
    "premium_due_date" : "21 March 2025",
    "sum_assured" : "100",
    "fund_value" : "one lakh",
    "outstanding_amount": "one Lakh",
    "percent": "10",
}
```

### 5. Run ChatBot

```bash
python main.py
```

# Author 

## Akash Kumar
