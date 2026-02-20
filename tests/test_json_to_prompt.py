from json_to_prompt import JSONToPrompt


class TestConvertDictToContext:

    def test_parse(self):
        example = {
            "Title": "Hello...",
            "Subtitle": "Goodbye...",
            "Cards": [
                {
                    "ID": 1,
                    "Title": "I'm a card...",
                }
            ]
        }
        convert_dict_to_context = JSONToPrompt(context_data=example, debug=True)
        result = convert_dict_to_context.parse()
        expected = "Title: Hello...\nSubtitle: Goodbye...\nCards:\n\t- ID: 1\n\t- Title: I'm a card..."
        assert result.prompt == expected

    def test_write_prompt_to_file(self):
        example = {
            "Title": "Hello...",
            "Subtitle": "Goodbye...",
            "Cards": [
                {
                    "ID": 1,
                    "Title": "I'm a card...",
                }
            ]
        }
        convert_dict_to_context = JSONToPrompt(context_data=example, debug=True)
        result = convert_dict_to_context.parse()
        expected = "Title: Hello...\nSubtitle: Goodbye...\nCards:\n\t- ID: 1\n\t- Title: I'm a card..."
        convert_dict_to_context.write_prompt_to_file("prompt.txt")
