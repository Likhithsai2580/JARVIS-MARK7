# JARVIS-MARK7

## Project Overview

JARVIS-MARK7 is an advanced AI assistant designed to provide a wide range of functionalities, including a chatbot, emotion system, user notebook, and more. The project leverages multiple APIs and services to deliver a seamless and interactive user experience.

## Features

- **Chatbot**: An intelligent chatbot capable of answering queries and engaging in conversations.
- **Emotion System**: An emotion system that allows the chatbot to express emotions based on user interactions.
- **User Notebook**: A personal notebook for users to store important notes and information.
- **Voice and Text Input**: Supports both voice and text input modes for user convenience.
- **APIs and Services**: Integrates with various APIs and services, including Cohere, Groq, and Deepgram.
- **Logging System**: A robust logging system to track and monitor activities.

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/Likhithsai2580/JARVIS-MARK7.git
   cd JARVIS-MARK7
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the necessary environment variables as specified in the `example.env` file.

## Usage

To run the project, use the following command:
```bash
python main.py
```

### Voice Input Mode

1. Ensure your microphone is connected and working.
2. Start the project using the command above.
3. Speak your queries, and the AI assistant will respond with voice output.

### Text Input Mode

1. Start the project using the command above.
2. Type your queries in the console, and the AI assistant will respond with text output.

## Configuration

The project can be configured using environment variables and configuration files located in the `data/config` directory.

### Environment Variables

- `SPEECHRECOGNITION_LANGUAGE`: Language for speech recognition (default: "en-US").
- `OPENAI_API_KEY`: API key for OpenAI (optional).
- `COHERE_API_KEY`: API key for Cohere.
- `GROQ_API_KEY`: API key for Groq.
- `DEEPGRAM_API_KEY`: API key for Deepgram (optional).
- `DATA_DIR`: Directory for storing data (default: "data").
- `TMP_DIR`: Directory for storing temporary files (default: "data/tmp").
- `JARVIS_HISTORY_LIMIT`: Limit for the number of history messages (default: "20").
- `SCREENSHOT`: Enable or disable screenshot functionality (default: "true").

### Configuration Files

- `data/config/config.py`: Main configuration file for the project.
- `data/config/emotion.config.json`: Configuration file for the emotion system.
- `data/config/function.config.json`: Configuration file for function definitions.

## Contributing

We welcome contributions to the project! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them with a descriptive message.
4. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request to the main repository.

Please ensure your code follows the project's coding standards and includes appropriate tests.

