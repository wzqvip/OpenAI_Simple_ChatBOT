# OpenAI_Simple_ChatBOT

This is generated by GPT-4 Model.

If you are in restricted country, you'll neen to use global proxy and uncomment the setting for Disable SSL verify( in the python file ).

#### Get you API


To get an API key from OpenAI, you need to sign up for their API access. Please follow these steps:

1. Visit the OpenAI signup page: [https://beta.openai.com/signup/](https://beta.openai.com/signup/)
2. Fill in the required information, such as your name, email, and password.
3. After signing up, you will receive an email to confirm your account. Click the link in the email to confirm your registration.
4. Log in to your OpenAI account: [https://beta.openai.com/login/](https://beta.openai.com/login/)
5. Once logged in, navigate to the API Keys section: [https://beta.openai.com/account/api-keys/](https://beta.openai.com/account/api-keys/)
6. Click the "Create" button to generate a new API key. You can now use this key to access the OpenAI API.

> Keep your API key ***secure***, and ***don't share it with anyone***. When using the key in your Python program, as shown in the previous example, it is recommended to *set the key as an environment variable rather than hardcoding it in your code*. This way, your key remains protected, and you can easily update or revoke it as needed.

#### Setup the chat bot

1. Set up a Python virtual environment and install the `openai` package:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate  # For Windows
pip install openai
</code></div></div></pre>

2. Set your API key as an environment variable:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">export OPENAI_API_KEY="your_api_key_here"  # For Linux and macOS
set OPENAI_API_KEY="your_api_key_here"  # For Windows
</code></div></div></pre>

3. Run the `main.py` script:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python main.py
</code></div></div></pre>

This program will allow you to interact with the GPT model. Type your input and press enter to get a response from the model. Type 'quit' and press enter to exit the program.

Please note that this example uses the `text-davinci-002` engine. You can replace it with other engines, depending on your API access and requirements.
