# AI Assistant – OpenAI (ChatGPT) Powered Python Automation Chatbot

A command-line AI assistant that leverages ChatGPT (via OpenAI API) for conversational interaction and **safe, on-demand automation**. This assistant can generate, save, and run Python scripts based on user requests—with explicit user confirmation for every action. Perfect for developers, power users, and anyone interested in safe, auditable AI-powered task automation on their local machine.

---

## Features

* **Conversational AI**: Interact with ChatGPT (gpt-4-turbo or gpt-3.5-turbo) from the terminal
* **Script Generation**: Ask for automations; the assistant will generate Python scripts as needed
* **Safety First**: User must confirm before any script is saved or executed
* **Script Management**: Unique filenames, script history, list and rerun any created script
* **Memory**: Keeps short conversation context for more relevant answers
* **No GUI, No Bloat**: Minimal dependencies, pure Python experience

---

## Requirements

* Python 3.8+
* [OpenAI API key](https://platform.openai.com/account/api-keys)
* `openai` Python package:
  `pip install openai`

---

## Usage

1. **Set Your API Key**

   * Open the script and set your `OPENAI_API_KEY` at the top.

2. **Run the Script**

   ```bash
   python deepseek_asistant.py
   ```

3. **Start Chatting**

   * Type your request/question.
   * To list all generated scripts, type: `list scripts`
   * To exit: `exit` or `quit`

4. **Script Creation & Execution**

   * If your request requires a script ("download all files from a URL", etc.), ChatGPT will generate Python code.
   * You will see the code and be asked for confirmation to save and (optionally) run it.
   * No script is run or saved without your explicit permission.

---

## Example Workflow

```
User: create a script that lists files in the current directory
Assistant: (shows script code)
Assistant: Do you want to save and run this script? (yes/no)
> yes
Assistant: Script 'script_list_files_xxxxxx.py' created successfully.
Assistant: Do you want to execute this script? (yes/no)
> yes
Assistant: (prints script output)
```

---

## Commands

* `list scripts` : Show all scripts generated in this session
* `exit` / `quit` : End the session

---

## Security Notes

* **Scripts only run with your explicit approval**
* Each script is saved with a unique name, and you can review code before executing
* No scripts are executed automatically

---

## Customization

* **Model:** Change `MODEL_NAME` to `gpt-4-turbo` or `gpt-3.5-turbo`
* **System Prompt:** Adjust the system prompt in `chat_with_gpt()` for custom behavior
* **History Depth:** Edit the number of history items retained (`history[-5:]`)

---

## License

MIT (c) Emir Baycan

---

## Author

Developed by [Emir Baycan](https://emirbaycan.com.tr/)
