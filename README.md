# JARVIS MARK 7

An advanced AI control system that combines face authentication, voice commands, and automated task execution. The project consists of a React-based client interface, a Python-based server for code execution (CodeBrew), and an Android bridge server for device control.

## 🌟 Features

### Core System
- Face authentication with liveness detection
- Voice command processing
- Real-time code execution engine
- Android device control bridge
- WebSocket-based real-time communication
- Modern React-based GUI with Tailwind CSS

### CodeBrew Engine
- Asynchronous code execution with timeout handling
- Real-time output capture and streaming
- Memory-safe execution environment
- Automatic dependency management
- Command history and caching
- Comprehensive error handling

### Android Bridge Server
- WebSocket-based real-time communication
- Secure device authentication
- Command queueing and rate limiting
- Automatic resource cleanup
- Response caching
- Compression support

### LLM Integration
- Support for multiple LLM providers (OpenAI, Groq, Cohere, etc.)
- Streaming responses
- Message history management
- Retry mechanism with exponential backoff
- Concurrent request handling

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 18+
- Android Studio (for mobile app development)
- Docker (optional, for containerized deployment)

### Client Setup
1. Clone the client repository:
```bash
git clone https://github.com/Likhithsai2580/JARVIS-MARK7-CLIENT.git
cd JARVIS-MARK7-CLIENT
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

### Server Setup
1. Clone the server repository:
```bash
git clone https://github.com/Likhithsai2580/JARVIS-MARK7-SERVER.git
cd JARVIS-MARK7-SERVER
```

2. Set up the Python environment:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r codebrew/requirements.txt
```

3. Set up the Android Bridge Server:
```bash
cd android_bridge_server
npm install
```

4. Configure environment variables:
```bash
# Copy example env files
cp .env.example .env
cp android_bridge_server/.env.example android_bridge_server/.env
```

## 🛠️ Development

### Project Structure
```
.
├── client/                 # React client application
│   ├── src/               # Source code
│   └── public/            # Static assets
├── server/                # Main server components
│   ├── codebrew/         # Python code execution engine
│   ├── android_bridge/   # Android bridge server
│   └── face_auth/        # Face authentication service
└── docs/                 # Documentation
```

### Running with Docker
```bash
# Build and run all services
docker-compose up -d

# Development environment
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

## 🧪 Testing

```bash
# Run all tests
npm test        # Client tests
pytest          # Server tests

# Run specific test categories
pytest -m unit
pytest -m integration
```

## 📚 Documentation

- [Client Documentation](./client/README.md)
- [Server Documentation](./server/README.md)
- [API Documentation](./docs/API.md)
- [Development Guide](./DEVELOPERS.md)
- [HTML Documentation](./docs/index.html)

## 🔐 Security

- Face authentication with liveness detection
- API key authentication
- Rate limiting
- Request validation
- Secure WebSocket connections
- Resource isolation
- Input sanitization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Support

For support, please:
1. Check the [Issues](https://github.com/Likhithsai2580/JARVIS-MARK7/issues) page
2. Join our Discord community
3. Email support at support@your-domain.com

## 🌟 Acknowledgments

- OpenAI for GPT models
- Groq for LLM hosting
- The FastAPI team
- Socket.IO contributors
- Android development community
