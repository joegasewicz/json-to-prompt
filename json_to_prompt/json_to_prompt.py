import json

from json_to_prompt.logger import logger


class JSONToPrompt:

    _prompt: str

    def __init__(
        self,
        context_data: dict,
        debug: bool = False,
    ):
        self.context_data = context_data
        self.debug = debug

    def add_dict(self, context_data: dict) -> "JSONToPrompt":
        """
        Add a Python Dict to parse to a formatted prompt.
        :param context_data:
        :return:
        """
        self.context_data = context_data
        return self

    def read_json(self, json_str: str) -> "JSONToPrompt":
        """
        Add a JSON string to be parsed to a formatted prompt.
        :param json_str:
        :return:
        """
        self.context_data = json.loads(json_str)
        return self

    def read_json_file(self, json_file: str) -> "JSONToPrompt":
        """
        Read form a JSON file to be parsed to then be parsed to a formatted prompt
        :param json_file:
        :return:
        """
        json_str = ""
        with open(json_file, "r") as f:
            f.write(json_str)
        self.read_json(json_str)
        return self

    def parse(self) -> "JSONToPrompt":
        """
        Parses a formated template string compatible with
        an LLM's context format from JSON.
        :return: JSONToPrompt
        """
        context_str = ""
        dict_len = len(self.context_data.keys())
        self._prompt = JSONToPrompt._parse(
            dict_part=self.context_data,
            context_str=context_str,
            dict_len=dict_len,
        )
        if self.debug:
            print(
                f"\n================== PROMPT START ================\n"
                f"{self._prompt}"
                f"\n================== PROMPT END ==================\n"
            )
        return self

    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, value: str):
        self._prompt = value

    def write_prompt_to_file(self, filename: str) -> None:
        """
        Writes the formatted & converted prompt to a file.
        :param filename: The name of the file.
        :return: None
        """
        if self._prompt == "":
            raise Exception("Error: No prompt to write. You must first call the 'parse' method!")
        if filename is None:
            raise Exception("You must pass in a filename!")
        if self.debug:
            logger.info(f"Writing prompt to file named: {filename}")
        with open(filename, "w") as f:
            f.write(self._prompt)

    @staticmethod
    def _parse(
        *,
        dict_part: dict,
        context_str: str,
        dict_len: int,
        is_list: bool = False,
    ):
        count = 1
        for k, v in dict_part.items():
            # Check if the value is a key
            if isinstance(v, list):
                context_str += f"{k}:"
                for item in v:
                    context_str = JSONToPrompt._parse(
                       dict_part=item,
                       context_str=context_str,
                       dict_len=len(item),
                       is_list=True,
                    )
                continue
            else:
                if not is_list:
                    context_str += f"{k}: {v}"
                else:
                    if count == 1:
                        context_str += "\n"
                    context_str += f"\t- {k}: {v}"
            if count < dict_len:
                # Add a line break if this is not the last key
                context_str += "\n"
            count += 1
        return context_str
