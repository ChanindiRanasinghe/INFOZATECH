# Task 1 - Rule-Based Chatbot

## Overview

InfozaBot is a simple rule-based chatbot developed using Python. It uses keyword matching and predefined responses to interact with users.

## Features

* Responds to common greetings
* Handles simple small-talk questions
* Provides information about services
* Provides contact information
* Handles goodbye messages
* Provides a fallback response for unknown inputs

## Technologies Used

* Python 3
* Rule-based keyword matching

## How It Works

The chatbot converts the user's input to lowercase and checks for predefined keywords or phrases.

For example:

* `hello` → Greeting response
* `how are you` → Small-talk response
* `services` → Services information
* `contact` → Contact information
* `bye` → Goodbye response
* Unknown input → Fallback response

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Run:

```bash
python Task1_Rule_Based_Chatbot/chatbot.py
```

4. Enter a message when prompted.
5. Type `bye` or `goodbye` to exit the chatbot.

## Example

```text
===================================
       Welcome to InfozaBot
===================================
Type 'bye' to exit.

You: hello
Bot: Hello! How can I help you?

You: what services do you provide?
Bot: We provide software development and AI solutions.

You: bye
Bot: Goodbye! Have a great day.
```

## Project Structure

```text
Task1_Rule_Based_Chatbot/
├── chatbot.py
├── README.md
└── requirements.txt
```
