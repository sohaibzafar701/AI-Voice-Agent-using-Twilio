# AI Voice Calling Agent

A powerful integration of OpenAI's Realtime API with Twilio's Voice services to enable real-time, interactive voice conversations between humans and AI. This project is ideal for applications like AI sales agents, customer support automation, cold calling, and compliance monitoring.

## Features
- Real-time voice streaming between Twilio and OpenAI
- Automatic speech detection and response cancellation
- Configurable voice settings and system prompts
- Environment-based configuration
- WebSocket-based communication
- Support for G711 ULAW audio format
- Interrupt handling for natural conversation flow
- Session management and real-time updates

## Prerequisites
Before you begin, ensure you have:
- Python 3.8 or higher
- An OpenAI API key with Realtime API access
- A Twilio account with:
  - Account SID
  - Auth Token
  - Phone Number
- [ngrok](https://ngrok.com/) or a similar tool to expose your local server to the internet

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-voice-calling-agent.git
   cd ai-voice-calling-agent
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory with your credentials:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   NGROK_URL=your_ngrok_url
   PORT=5050
   ```

5. **Create a system prompt**:
   - Create a `prompts` directory in the project root.
   - Add a `system_prompt.txt` file with AI instructions, e.g.:
     ```text
     You are a helpful AI assistant for customer support. Respond politely and concisely to user queries.
     ```

## Usage
1. **Start the server**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 5050
   ```

2. **Expose your local server with ngrok**:
   ```bash
   ngrok http 5050
   ```
   Copy the ngrok URL (e.g., `https://your-ngrok-url.ngrok-free.app`) and update:
   - The `NGROK_URL` in your `.env` file.
   - The Twilio webhook for your phone number in the Twilio Console to `https://your-ngrok-url.ngrok-free.app/outgoing-call` (HTTP method: POST).

3. **Configure Twilio webhook**:
   - Log in to the [Twilio Console](https://console.twilio.com/).
   - Go to **Phone Numbers** > **Manage** > **Active Numbers**.
   - Select your phone number.
   - Under **Voice**, set **A Call Comes In** to:
     - **Webhook**: `https://your-ngrok-url.ngrok-free.app/outgoing-call`
     - **HTTP Method**: `POST`
   - Save the configuration.

4. **Initiate a call**:
   - **Using the API**:
     ```bash
     curl -X POST "http://localhost:5050/make-call" -H "Content-Type: application/json" -d '{"to_phone_number": "+1234567890"}'
     ```
     Replace `+1234567890` with the target phone number in E.164 format.

   - **Using the Python script**:
     Edit `make_call.py` to set the `to_phone` variable to your target number, then run:
     ```bash
     python make_call.py
     ```

5. **Test the call**:
   - Answer the call on the target phone.
   - You should hear: "This call may be recorded for compliance purposes," followed by a pause, then "Connecting with Compliance Agent," and finally the AI’s response.

## Project Structure
```
ai-voice-calling-agent/
├── app.py               # Main FastAPI application
├── make_call.py        # Script to initiate calls via Twilio SDK
├── prompts/
│   └── system_prompt.txt # System instructions for AI
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

## Configuration
### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key with Realtime API access
- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number (e.g., `+1234567890`)
- `NGROK_URL`: Your ngrok URL (e.g., `https://your-ngrok-url.ngrok-free.app`)
- `PORT`: Server port (default: `5050`)

### System Prompt
Customize the AI’s behavior by editing `prompts/system_prompt.txt`.

## API Endpoints
- **GET /**: Health check endpoint
  - Response: `{"message": "Twilio Media Stream Server is running!"}`
- **POST /make-call**: Initiate a new call
  - Body: `{"to_phone_number": "+1234567890"}`
  - Response: `{"call_sid": "CAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}`
- **POST /outgoing-call**: Webhook for Twilio voice calls
  - Returns TwiML to connect to the WebSocket stream
- **WebSocket /media-stream**: WebSocket endpoint for media streaming

## Scripts
- **make_call.py**: A utility script to initiate calls using the Twilio SDK. Edit the `to_phone` variable to specify the target number, then run:
  ```bash
  python make_call.py
  ```

## Troubleshooting
- **Geo Permissions Error** (Twilio Error 21215):
  - Enable international calling for the target country in the Twilio Console (**Settings** > **General** > **Geo Permissions** > **Voice**).
  - See [Twilio Error 21215](https://www.twilio.com/docs/errors/21215).
- **Webhook Issues**:
  - Ensure the ngrok URL is active and matches the Twilio webhook.
  - Check Twilio’s debugger (**Monitor** > **Logs** > **Errors**).
- **No AI Response**:
  - Verify your OpenAI API key has Realtime API access.
  - Ensure `prompts/system_prompt.txt` exists and is valid.
  - Check server logs for WebSocket errors.
- **Call Fails**:
  - Confirm the target phone number is valid and reachable.
  - Verify your Twilio account has sufficient funds.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request.

For major changes, please open an issue first to discuss your proposed changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
