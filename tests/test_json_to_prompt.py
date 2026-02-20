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
        jtp = JSONToPrompt(debug=True)
        jtp.add_dict(context_data=example)
        jtp.parse()
        expected = "Title: Hello...\nSubtitle: Goodbye...\nCards:\n\t- ID: 1\n\t- Title: I'm a card..."
        assert jtp.prompt == expected

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
        jtp = JSONToPrompt(debug=True)
        jtp.add_dict(context_data=example)
        jtp.parse()
        expected = (
            "Title: Hello...\n"
            "Subtitle: Goodbye...\n"
            "Cards:\n"
            "\t- ID: 1\n"
            "\t- Title: I'm a card..."
        )
        # test the output file
        file_path = tmp_path / "prompt.txt"

        jtp.write_prompt_to_file(str(file_path))

        assert file_path.exists()
        actual = file_path.read_text()
        assert expected == actual

    def test_add_dict(self):
        example = {
            "pet": "cat",
        }
        jtp = JSONToPrompt()
        jtp.add_dict(example)
        assert jtp.context_data == example

    def test_read_json(self):
        expected = {
            "pet": "cat",
        }
        json_str = '{"pet": "cat"}'
        jtp = JSONToPrompt()
        jtp.read_json(json_str)
        assert jtp.context_data == expected

    def test_read_json_file(self):
        expected = {
            "Title": "Hello...",
            "Subtitle": "Goodbye...",
            "Cards": [
                {
                    "ID": 1,
                    "Title": "I'm a card...",
                }
            ]
        }
        jtp = JSONToPrompt()
        jtp.read_json_file("tests/example.json")
        jtp.parse()
        assert expected == jtp.context_data