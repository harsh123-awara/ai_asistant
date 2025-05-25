import openai
import os
import subprocess
import re
import uuid

# ✅ Set OpenAI API Key
OPENAI_API_KEY = "x"

# ✅ Configure OpenAI API
openai.api_key = OPENAI_API_KEY
MODEL_NAME = "gpt-4-turbo"  # Use "gpt-3.5-turbo" for lower cost

history = []  # ✅ Keeps conversation history
script_history = {}  # ✅ Stores script names for later use
user_name = "User"

def chat_with_gpt(user_input):
    """ ✅ Sends a message to ChatGPT and gets a response while keeping memory """
    
    messages = [{"role": "system", "content": """
    You are an AI assistant that automates tasks.
    - If the user gives a command that requires a script, generate a Python script.
    - Ask for confirmation before executing any script.
    - Generate only valid Python code inside markdown syntax.
    """}]

    # ✅ Keep last 5 interactions for memory
    for entry in history[-5:]:  
        messages.append({"role": "user", "content": entry})
    
    messages.append({"role": "user", "content": user_input})

    # 🔹 Call OpenAI API
    response = openai.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.7  
    )

    reply = response.choices[0].message.content  
    return reply

def detect_script_request(response):
    """ ✅ Detects if the assistant response contains a script request """
    return "```python" in response  # ✅ Check if GPT is returning Python code

def extract_script_code(response):
    """ ✅ Extract Python script from ChatGPT's response """
    match = re.search(r"```python(.*?)```", response, re.DOTALL)
    return match.group(1).strip() if match else None

def generate_unique_script_name(user_request):
    """ ✅ Creates a unique script name based on the user's request """
    base_name = re.sub(r'\W+', '_', user_request.lower()).strip('_')[:30]  # ✅ Sanitize name
    unique_id = str(uuid.uuid4())[:6]  # ✅ Short unique ID
    return f"script_{base_name}_{unique_id}.py"

def create_script(script_name, script_code):
    """ ✅ Saves the generated script to a file """
    script_path = os.path.join(os.getcwd(), script_name)
    with open(script_path, "w") as script_file:
        script_file.write(script_code)
    
    # ✅ Store script in history
    script_history[len(script_history) + 1] = script_name
    return f"✅ Script '{script_name}' created successfully."

def list_scripts():
    """ ✅ Lists all generated scripts """
    if not script_history:
        return "No scripts have been created yet."
    return "\n".join([f"{idx}. {name}" for idx, name in script_history.items()])

def run_script(script_name, *args):
    """ ✅ Runs a script with optional arguments and returns output """
    if not os.path.exists(script_name):
        return f"❌ Script '{script_name}' not found."

    try:
        cmd = ["python", script_name] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.stdout else f"⚠️ Error:\n{result.stderr}"
    except Exception as e:
        return f"❌ Error running script: {str(e)}"

# 🔹 Interactive Chat Loop
while True:
    user_input = input(f"\n{user_name}: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # ✅ Handle script listing
    if "list scripts" in user_input.lower():
        response = list_scripts()
        print(f"\nAssistant: {response}")
        continue

    # ✅ Use ChatGPT to analyze user request
    response = chat_with_gpt(user_input)

    # ✅ If a script is detected in the response, ask to create and run it
    if detect_script_request(response):
        script_code = extract_script_code(response)
        script_name = generate_unique_script_name(user_input)
        
        print(f"\nAssistant: I have generated a script for your request.\n")
        print(f"📜 **Script Preview:**\n{script_code}\n")
        print(f"Do you want to save and run this script? (yes/no)")

        confirm = input("> ").strip().lower()
        if confirm == "yes":
            create_script(script_name, script_code)
            print(f"\nAssistant: ✅ Script '{script_name}' created successfully.")
            
            print(f"\nAssistant: Do you want to execute this script? (yes/no)")
            run_confirm = input("> ").strip().lower()
            if run_confirm == "yes":
                output = run_script(script_name)
                print(f"\nAssistant: {output}")
        continue

    # ✅ Otherwise, just respond normally
    print(f"\nAssistant: {response}")

    # ✅ Save to history for context
    history.append(user_input)
