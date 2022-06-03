from jsonschema import validate
from json import load
from jsonschema.exceptions import ValidationError
from os.path import exists
from typing import Union


class JsonValidator:

    def main(
            self,
            json_file_path: str,
            schema_file_path: str
    ) -> Union[bool, FileNotFoundError]:
        """
        Return True/False if schema validate with json file. Else raising FileNotFound error if json_file or schema
        file not exists.
        :param json_file_path: json data to validate with schema.
        :param schema_file_path: schema file for validation of json file.
        :return: True/False or FileNotFoundError
        """
        if self.is_file_exits(json_file_path,
                              schema_file_path):
            with open("json_file.json") as json_file_data, open("schema.json") as schema_file_data:
                json_data = load(json_file_data)
                schema_data = load(schema_file_data)
            return self.validate_schema(json_data,
                                        schema_data)
        else:
            raise FileNotFoundError("File not found")

    def validate_schema(
            self,
            json_file: str,
            schema_file: str
    ) -> bool:
        """
        Validating schema, return True if json file validated else False
        :param json_file: json file to validate
        :param schema_file: schema file for validation
        :return: True or False
        """
        try:
            validate(json_file,
                     schema_file)
            return True
        except ValidationError:
            return False

    def is_file_exits(self,
                      *args: Union[str]
                      ) -> bool:
        """
        Checking file existence, return True if all file exists else false
        :param args: file paths
        :return: True or False
        """
        file_exists = []
        for file_path in args:
            if exists(file_path):
                file_exists.append(True)
            else:
                file_exists.append(False)
        return all(file_exists)


if __name__ == '__main__':
    json_validator = JsonValidator()
    print(json_validator.main("json_file.json", "schema.json"))
