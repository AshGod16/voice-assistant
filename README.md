# Voice Assistant with NLP

A Python-based voice assistant that uses natural language processing for intent classification and speech recognition for voice commands.

## Features

- Voice input/output capabilities
- NLP-based intent classification
- Basic command handling:
  - Greetings
  - Time queries
  - Web searches
  - Weather information (placeholder)
  - Music control (placeholder)

## Prerequisites

- Python 3.7+
- PortAudio
- Working microphone

## Installation

### 1. Install PortAudio

**macOS:**
```bash
brew install portaudio
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev  # Ubuntu/Debian
sudo dnf install portaudio-devel      # Fedora
```

**Windows:**
Download and install PyAudio wheel from unofficial binaries.

### 2. Install Python Dependencies

```bash
pip install SpeechRecognition pyttsx3 transformers torch pyaudio tqdm
```

## Usage

1. Clone the repository
2. Run the assistant:
```bash
python assistant.py
```

3. Speak commands when "Listening..." appears

Example commands:
- "What time is it?"
- "Search for weather forecast"
- "Hello"

## Configuration

Models are cached in `~/.voice_assistant_cache` to prevent repeated downloads.

## Troubleshooting

### Microphone Permissions

**macOS:**
- System Settings → Privacy & Security → Microphone
- Enable for Terminal/IDE

**Windows:**
- Settings → Privacy → Microphone
- Enable "Allow apps to access your microphone"

**Linux:**
```bash
sudo usermod -a -G audio $USER
```
Log out and back in.

### Common Errors

1. "Could not understand audio"
   - Check microphone connection
   - Speak clearly and closer to microphone

2. "Could not request results"
   - Verify internet connection
   - Check microphone permissions

## Extending Functionality

Add new intents in the `intents` dictionary:
```python
self.intents = {
    "new_intent": ["keyword1", "keyword2"]
}
```

Implement corresponding handler in `handle_intent()`.

## License

MIT

## Contributing

1. Fork the repository
2. Create feature branch
3. Submit pull request

## Acknowledgments

- HuggingFace Transformers
- SpeechRecognition
- PyTTSx3