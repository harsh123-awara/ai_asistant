# AI Assistant: Your Terminal-Based Companion 🤖

![GitHub release](https://img.shields.io/github/release/harsh123-awara/ai_asistant.svg)
![GitHub issues](https://img.shields.io/github/issues/harsh123-awara/ai_asistant.svg)
![GitHub stars](https://img.shields.io/github/stars/harsh123-awara/ai_asistant.svg)

Welcome to the **AI Assistant** repository! This project serves as a terminal-based AI assistant that leverages the ChatGPT API. It allows you to generate, save, and run Python scripts securely, all from your command line. With this tool, you can automate tasks with ease and confidence.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features

- **ChatGPT Integration**: Interact with the powerful ChatGPT API to generate Python scripts.
- **Script Management**: Save scripts directly to your local machine for future use.
- **User Approval**: Ensure security by requiring user approval before executing any script.
- **Task Automation**: Automate repetitive tasks directly from the command line.
- **Secure Execution**: Run scripts in a controlled environment to prevent unauthorized access.

## Installation

To get started with the AI Assistant, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/harsh123-awara/ai_asistant.git
   cd ai_asistant
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   You need to set your OpenAI API key as an environment variable. Add the following line to your `.bashrc` or `.bash_profile`:
   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

4. **Download the Latest Release**:
   Visit the [Releases](https://github.com/harsh123-awara/ai_asistant/releases) section to download the latest version. Execute the file after downloading to get started.

## Usage

Once you have installed the AI Assistant, you can start using it directly from your terminal.

1. **Launch the Assistant**:
   Run the following command:
   ```bash
   python ai_assistant.py
   ```

2. **Interact with the Assistant**:
   Type your request, and the assistant will generate a Python script based on your input.

3. **Review the Script**:
   The generated script will be displayed. You can choose to save it or run it immediately.

4. **Execute the Script**:
   If you approve the script, you can run it with a simple command. The assistant will execute the script in a secure environment.

## Commands

Here are some common commands you can use with the AI Assistant:

- **Generate a Script**:
   ```bash
   generate_script "Your task description"
   ```

- **Save the Script**:
   ```bash
   save_script "script_name.py"
   ```

- **Run the Script**:
   ```bash
   run_script "script_name.py"
   ```

- **List Saved Scripts**:
   ```bash
   list_scripts
   ```

## Contributing

We welcome contributions to improve the AI Assistant. If you want to contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the top right of the page.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make Your Changes**: Edit the code as needed.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Branch**:
   ```bash
   git push origin feature/YourFeature
   ```
6. **Create a Pull Request**: Go to the original repository and click "New Pull Request."

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or issues, feel free to open an issue on GitHub. You can also check the [Releases](https://github.com/harsh123-awara/ai_asistant/releases) section for updates and downloads.

## Conclusion

The AI Assistant is designed to make your life easier by automating tasks and providing a secure way to run scripts. We hope you find this tool useful and encourage you to contribute to its development. Happy coding!