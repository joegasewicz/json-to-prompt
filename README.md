# JSON To Prompt
A lightweight Python utility for converting structured JSON data into formatted prompt text.

This project is designed to transform dictionaries or JSON inputs into readable, structured text prompts suitable for LLM workflows, templating systems, or downstream processing.

## Features
-Convert Python dictionaries to formatted prompt strings
-Read JSON strings directly
-Load JSON from file
-Write generated prompts to file
-Simple, predictable formatting
-Fully unit tested with pytest

### Usage

### Convert a Dictionary to a Prompt
```python
from json_to_prompt import JSONToPrompt

data = {
    "Title": "Hello...",
    "Subtitle": "Goodbye...",
    "Cards": [
        {
            "ID": 1,
            "Title": "I'm a card...",
        }
    ]
}

jtp = JSONToPrompt(debug=True)
prompt = jtp.add_dict(data).parse().get_prompt()
print([prompt])
```
**Output**:
```text
Title: Hello...
Subtitle: Goodbye...
Cards:
    - ID: 1
    - Title: I'm a card... 
```
### Read from a JSON string
```python
json_str = '{"pet": "cat"}'

jtp = JSONToPrompt()
prompt = jtp.read_json(json_str).parse().get_prompt()

```

### Read from a JSON file
```python
jtp = JSONToPrompt()
prompt = jtp.read_json_file("example.json").parse().get_prompt()
```

### Write Prompt To file
```python
jtp.write_prompt_to_file("prompt.txt")
```