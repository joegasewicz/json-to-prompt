# JSON To Prompt

### Quick Start

```python
from json_to_prompt import JSONToPrompt

convert_dict_to_context = JSONToPrompt(context_data=example, debug=True)
result = convert_dict_to_context.parse() 
```


### Writing The Prompt Output To a File
For examples if we have the following JSON file
```python
{
    "Title": "Hello...",
    "Subtitle": "Goodbye...",
    "Cards": [
        {
            "ID": 1,
            "Title": "I'm a card...",
        }
    ]
} 
```
```text
Title: Hello...
Subtitle: Goodbye...
Cards:
	- ID: 1
	- Title: I'm a card... 
```