import shutil
import os

from json_to_prompt import JSONToPrompt


class TestConvertDictToContext:

    def setup_method(self):
        pass

    def teardown_method(self):
        if os.path.exists("prompt.txt"):
            shutil.rmtree("prompt.txt")

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

    def test_write_prompt_to_file(self, tmp_path):
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
        convert_dict_to_context.parse()
        expected = (
            "Title: Hello...\n"
            "Subtitle: Goodbye...\n"
            "Cards:\n"
            "\t- ID: 1\n"
            "\t- Title: I'm a card..."
        )
        # test the output file
        file_path = tmp_path / "prompt.txt"

        convert_dict_to_context.write_prompt_to_file(str(file_path))

        assert file_path.exists()
        actual = file_path.read_text()
        assert expected == actual

    def test_add_dict(self):
        pass

    def test_read_json(self):
        pass

    def test_read_json_file(self):
        pass

