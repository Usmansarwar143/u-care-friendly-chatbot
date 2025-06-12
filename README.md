# U-Care Bot 🩺

Welcome to **U-Care Bot**, a friendly and safe health query chatbot built with Streamlit and powered by the Mistral-7B-Instruct model via the OpenRouter API. U-Care Bot provides general health information in a clear, empathetic, and patient-friendly manner, ensuring users feel supported while prioritizing safety. 😊

![U-Care Bot Animation](https://assets5.lottiefiles.com/packages/lf20_vpjqyzdt.json)

## Features 🌟

- **Friendly Responses**: Answers health-related questions with a warm, approachable tone using emojis like 🩺 and 🚑.
- **Safety First**: Filters unsafe keywords (e.g., "heart attack", "suicide") and advises users to seek professional help for serious concerns.
- **Conversation History**: Displays past questions and answers in styled chat bubbles for easy reference.
- **Attractive Interface**: Built with Streamlit, featuring custom CSS and Lottie animations for a modern, engaging look.
- **Prompt Engineering**: Uses a carefully crafted system prompt to ensure clear, accurate, and general health information.
- **No Harmful Advice**: Avoids personalized diagnoses or treatments, always reminding users to consult a healthcare professional.

## Installation ⚙️

To run U-Care Bot locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/u-care-bot.git
   cd u-care-bot
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed, then install the required packages:
   ```bash
   pip install streamlit requests streamlit-lottie
   ```

3. **Get an OpenRouter API Key**:
   - Sign up at [OpenRouter](https://openrouter.ai/) to obtain a free API key.
   - Replace `"your_openrouter_api_key_here"` in `health_chatbot_streamlit.py` with your actual API key.

## Usage 🚀

1. **Run the Application**:
   ```bash
   streamlit run health_chatbot_streamlit.py
   ```
   This will launch the U-Care Bot in your default web browser.

2. **Ask Health Questions**:
   - Enter queries like "What causes a sore throat?" or "Is paracetamol safe for children?" in the text input.
   - The bot responds with general information and a reminder to consult a doctor.
   - If your question contains sensitive terms (e.g., "heart attack"), U-Care Bot will display a warning to seek immediate professional help.

3. **View Conversation History**:
   - Scroll up to see previous questions and answers in styled chat bubbles.

## Example Queries ❓

- **Query**: "What causes a sore throat?"
  - **Response**: Explains common causes (e.g., viral infections, allergies) and general remedies like staying hydrated, with a reminder to see a doctor if symptoms persist.
- **Query**: "Is paracetamol safe for children?"
  - **Response**: Provides general guidance on paracetamol use for children, emphasizing the need to follow pediatrician advice.
- **Query**: "I have a heart attack"
  - **Response**: ⚠️ "Sorry, your question contains sensitive terms related to serious medical emergencies. Please consult a healthcare professional immediately or contact emergency services."

## Safety Features 🔒

- **Unsafe Keyword Filter**: Checks for terms like "suicide", "overdose", or "stroke" and responds with a safety warning.
- **General Information Only**: Avoids specific medical advice, diagnoses, or treatments.
- **Professional Guidance**: Every response includes a reminder to consult a healthcare professional for personalized advice.

## Technologies Used 🛠️

- **Streamlit**: For the interactive web interface.
- **OpenRouter API**: To access the Mistral-7B-Instruct model for natural language processing.
- **Streamlit-Lottie**: For health-themed animations.
- **Python**: Core programming language.
- **Custom CSS**: For a patient-friendly, modern UI with chat bubbles.

## Contributing 🤝

We welcome contributions to make U-Care Bot even better! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your changes align with the bot's focus on safety and user-friendliness.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [OpenRouter](https://openrouter.ai/) for providing access to the Mistral-7B-Instruct model.
- [LottieFiles](https://lottiefiles.com/) for the awesome health-themed animations.
- Built with ❤️ to support users seeking general health information safely.

---

**U-Care Bot**: Your friendly health companion! Always consult a doctor for personalized advice. 🩺
