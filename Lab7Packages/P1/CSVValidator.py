import pandas as pd
import os
class Validator:
    def __init__(self, file_path):

        try:
            assert (os.path.isfile(file_path)),"That is not a file"
        except Exception as opsie:
            print(opsie)
        else:
            self.file_path = file_path
            self.df = pd.read_csv(file_path)

    def check_missing_values(self):
        return self.df.isnull().any()

    def check_data_types(self, rules):
        for column, expected_type in rules.items():
            actual_type = self.df[column].dtype
            if actual_type != expected_type:
                return f"Column '{column}' has incorrect data type. Expected: {expected_type}, Actual: {actual_type}"
        return None