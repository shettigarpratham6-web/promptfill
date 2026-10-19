
# PromptFill

[![PyPI version](https://img.shields.io/pypi/v/promptfill-pratham.svg)](https://pypi.org/project/promptfill-pratham/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PromptFill is a lightweight, zero-dependency Python utility designed for AI engineers. It helps you manage prompt templates separately from your application code by loading and formatting prompts from external Markdown and text files.

---

## Live Links

- **GitHub Repository:** [PromptFill on GitHub](https://github.com/YOUR_USERNAME/promptfill)
- **PyPI Package:** [promptfill-pratham on PyPI](https://pypi.org/project/promptfill-pratham/)

---


## Why PromptFill?

In real-world AI applications, writing long prompts directly inside Python files can make the code difficult to read and maintain.

PromptFill solves this problem by allowing you to store prompts in external files and fill in their variables dynamically.

### Key Features

- **External Prompt Files:** Store prompts in Markdown (`.md`) or text (`.txt`) files.
- **Dynamic Formatting:** Replace placeholders with values supplied from Python.
- **Reusable Templates:** Reuse the same prompt template across multiple scripts and projects.
- **Missing Variable Detection:** Raise a helpful `ValueError` when a required placeholder is missing.
- **Lightweight:** Designed to work without third-party runtime dependencies.
- **LLM Integration:** Use formatted prompts with Gemini, OpenAI, or other LLM providers.
- **Cleaner Code:** Keep prompt templates separate from application logic.

---

## Installation

Install PromptFill using pip:

```bash
pip install promptfill
```

To upgrade to the latest published version:

```bash
pip install --upgrade promptfill
```

---

## How It Works

PromptFill follows three simple steps:

1. Write your prompt in a `.md` or `.txt` file.
2. Add placeholders wherever you need dynamic values.
3. Load the file from Python and provide values for those placeholders.

PromptFill replaces the placeholders and returns the completed prompt as a Python string.

---

## Quick Start

### Step 1: Create a Prompt Template

Create a file named `reviewer.md` in your project directory.

Add the following content:

```text
You are an expert $role.

Review the following code written in $language for bugs,
security vulnerabilities, and performance issues.

Code to review:

$code_snippet

Provide your findings and suggest improvements.
```

In this template:

- `$role` represents the role of the AI.
- `$language` represents the programming language.
- `$code_snippet` represents the code to review.

These placeholders will be replaced with values provided by your Python application.

### Step 2: Load and Format the Prompt

Create a Python file named `main.py`:

```python
from promptfill import load_prompt

prompt = load_prompt(
    file_path="reviewer.md",
    role="Senior Security Engineer",
    language="Python",
    code_snippet="print('Hello, World!')"
)

print(prompt)
```

### Step 3: Get the Formatted Output

PromptFill replaces each placeholder with its corresponding value.

The resulting prompt will look like this:

```text
You are an expert Senior Security Engineer.

Review the following code written in Python for bugs,
security vulnerabilities, and performance issues.

Code to review:

print('Hello, World!')

Provide your findings and suggest improvements.
```

The returned value is a regular Python string that you can pass to your LLM client.

---

## Example Project Structure

A typical project using PromptFill can look like this:

```text
my-ai-project/
|
├── prompts/
│   ├── reviewer.md
│   ├── summarizer.md
│   └── chatbot.txt
|
├── main.py
├── requirements.txt
└── README.md
```

This structure keeps your prompt templates separate from your application logic.

You can organize your prompts into different files based on their purpose.

---

## Usage Examples

### 1. Using a Text File

Create a file named `summarizer.txt`:

```text
Summarize the following $content_type in $max_words words.

Content:
$content
```

Load the template:

```python
from promptfill import load_prompt

prompt = load_prompt(
    file_path="summarizer.txt",
    content_type="technical article",
    max_words=100,
    content="Python is a popular programming language..."
)

print(prompt)
```

### 2. Reusing a Prompt Template

You can load the same template multiple times with different values.

```python
from promptfill import load_prompt

template_path = "reviewer.md"

python_prompt = load_prompt(
    file_path=template_path,
    role="Python Developer",
    language="Python",
    code_snippet="print(10 + 20)"
)

javascript_prompt = load_prompt(
    file_path=template_path,
    role="JavaScript Developer",
    language="JavaScript",
    code_snippet="console.log(10 + 20)"
)

print(python_prompt)
print(javascript_prompt)
```

The same prompt file can be used for different tasks without duplicating the template.

### 3. Handling Missing Variables

PromptFill helps identify missing values when a required placeholder is not provided.

For example, suppose `reviewer.md` contains:

```text
You are an expert $role.

Review this $language code:

$code_snippet
```

Now, consider the following Python code, where the `language` argument is missing:

```python
from promptfill import load_prompt

prompt = load_prompt(
    file_path="reviewer.md",
    role="Developer",
    code_snippet="x = 1"
)
```

PromptFill is designed to raise a `ValueError` when a required variable is missing. The error message may look like this:

```text
ValueError: Missing prompt variable for placeholder: 'language'
```

This helps you identify incomplete prompts before sending them to an LLM.

Note: The exact error message depends on the package implementation.

---

## Using PromptFill with an LLM

PromptFill formats prompts, but it does not call an LLM by itself.

You can use the formatted output with your preferred LLM provider.

For example, you can use an OpenAI-compatible client:

```python
from promptfill import load_prompt
from openai import OpenAI

client = OpenAI()

prompt = load_prompt(
    file_path="reviewer.md",
    role="Python Expert",
    language="Python",
    code_snippet="print('Hello, World!')"
)

response = client.chat.completions.create(
    model="YOUR_MODEL_NAME",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)
```

Install the OpenAI SDK separately if you want to run this example:

```bash
pip install openai
```

Replace `YOUR_MODEL_NAME` with a model supported by your configured API provider.

Important: The OpenAI SDK is an optional dependency for this example. PromptFill itself is designed to work without third-party runtime dependencies.

---

## API Reference

### `load_prompt()`

The `load_prompt()` function loads a prompt template from a file and formats it using the values you provide.

Example:

```python
from promptfill import load_prompt

prompt = load_prompt(
    file_path="reviewer.md",
    role="Security Engineer",
    language="Python",
    code_snippet="x = 10"
)
```

**Parameters**

| Parameter | Description |
|---|---|
| `file_path` | Path to the prompt template file. |
| Keyword arguments | Values used to replace the corresponding placeholders. |

**Returns:** A formatted Python string.

**Missing variables:** A `ValueError` is expected when a required placeholder is not supplied.

The supported arguments and exceptions should match the implementation of your installed PromptFill version.

---

## Testing Your Installation

After installing PromptFill, you can run the following example to check whether it works correctly.

```python
from promptfill import load_prompt

prompt = load_prompt(
    file_path="reviewer.md",
    role="Developer",
    language="Python",
    code_snippet="print('PromptFill works!')"
)

assert "Developer" in prompt
assert "Python" in prompt
assert "PromptFill works!" in prompt

print("PromptFill is working correctly!")
```

If the script runs successfully, the prompt has been loaded and formatted.

---

## Who Is PromptFill For?

PromptFill can be useful for:

- **AI Engineers** building applications powered by large language models.
- **Generative AI Developers** managing reusable prompt templates.
- **RAG Developers** maintaining prompts for retrieval and question-answering systems.
- **Agentic AI Developers** managing prompts for different agents and tasks.
- **Python Developers** who want to keep their code clean and maintainable.

---

## PromptFill vs. Hardcoded Prompts

| Hardcoded Prompts | PromptFill |
|---|---|
| Prompts are written directly inside Python code. | Prompts are stored in separate files. |
| Long prompts can make application code difficult to read. | Application code stays cleaner. |
| Reusing prompts may require copying code. | Templates can be reused across scripts. |
| Missing values may go unnoticed until runtime. | Missing required variables can raise an error. |

---

## Security Considerations

PromptFill formats text. It does not automatically make prompts or inserted values safe.

- Avoid storing API keys, passwords, or other secrets directly in prompt files.
- Treat user-provided values as untrusted input.
- Review formatted prompts before using them in sensitive applications.
- Remember that sending a prompt to an external LLM provider may transmit its contents to that provider.

---

## Roadmap

Potential future improvements include:

- [ ] Better error messages for invalid templates.
- [ ] Support for nested prompt directories.
- [ ] Prompt template validation.
- [ ] Prompt version management.
- [ ] Integration examples for LangChain and other LLM frameworks.
- [ ] Unit tests and continuous integration.
- [ ] Support for additional template formats.

---

## Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and add tests.
4. Submit a pull request explaining your changes.

Please test new functionality and make sure existing behavior continues to work.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for the complete license text.

---

## Support the Project

If PromptFill helps you build cleaner AI applications, consider giving the repository a star on GitHub.

**PromptFill: Keep your prompts clean, reusable, and ready for AI.**
