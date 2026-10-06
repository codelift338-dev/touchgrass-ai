🌱 TouchGrass AI

A local AI-powered outdoor companion that helps people put their screens down and spend time outside.

🌳 What is TouchGrass AI?

TouchGrass AI generates simple outdoor missions using a locally running open-weight AI model.

Instead of asking users to spend more time chatting with AI, the goal is the opposite:

Use AI briefly, then put the screen away and go outside.

Choose an activity such as:

🚶 Walking

🥾 Exploring

🌻 Gardening

🐦 Birdwatching

📷 Nature photography

Choose how much time you have, and TouchGrass AI creates a small outdoor challenge.

After going outside, users can write a reflection about what they noticed.

🤖 Open-Source AI

TouchGrass AI runs AI locally using:

Qwen 2.5 0.5B Instruct — an open-weight language model

llama.cpp — local inference

Python

Flask

The AI does not need to send the user's prompt to a cloud AI provider.

The model runs on the user's own computer.

🔒 Why Local AI?

Privacy was one of the main reasons for choosing a local AI approach.

Outdoor reflections can be personal. TouchGrass AI does not require an account or cloud database.

The application is designed around:

No user account

No cloud database

No tracking

Local AI inference

Local browser history

The reflections are stored in the browser's local storage on the user's device.

💻 Built on Modest Hardware

This project was intentionally built to work with lightweight local AI.

The development machine used for this project has:

Windows

8 GB RAM

Intel Pentium processor

Integrated Intel HD Graphics

Because the hardware is modest, the project uses a small quantized model rather than depending on a large cloud-hosted model.

🏗️ How It Works
User
  │
  ▼
TouchGrass AI Web Interface
  │
  ▼
Flask Backend
  │
  ▼
llama.cpp
  │
  ▼
Qwen 2.5 0.5B
  │
  ▼
Short Outdoor Idea
  │
  ▼
Outdoor Mission
  │
  ▼
User goes outside
  │
  ▼
Local Reflection

✨ Features

Generate AI-powered outdoor missions

Activity-specific suggestions

Walking mode

Exploring mode

Gardening mode

Birdwatching mode

Nature photography mode

Outdoor countdown timer

Personal reflections

Local mission history

Local browser storage

No account required

No cloud database

Local AI inference

🚀 Running the Project
Requirements

You need:

Windows, Linux, or macOS

Python

Git

llama.cpp

A compatible GGUF model

Install Python dependencies
pip install -r requirements.txt

Start llama.cpp

Download a compatible GGUF model and start the local server.

Example:

llama-server -m ./your-model.gguf --host 127.0.0.1 --port 8081


The application expects the AI server at:

http://127.0.0.1:8081

Start TouchGrass AI

In another terminal:

python app.py


Open:

http://127.0.0.1:5000

🌱 Design Philosophy

TouchGrass AI is intentionally different from an ordinary AI assistant.

The goal is not to maximize screen time.

The goal is to make the screen interaction as short as possible.

The AI provides the idea.

The user provides the real experience.

🏕️ Hacktoberfest 2026

This project was created for the Hacktoberfest 2026 DEV Challenge — Week 1: Touch Grass.

The challenge asks participants to build something with open-source AI at its core that encourages people to spend time outside.

TouchGrass AI approaches that idea by using a lightweight local model to generate short outdoor missions while keeping the user's reflections on their own device.

🔮 Future Ideas

Possible future improvements include:

Local weather-aware missions

Nature difficulty levels

Seasonal challenges

More outdoor activities

Streaks stored locally

Printable mission cards

Offline-first improvements

Better support for very low-powered computers

📄 License

This project is intended to be open source.