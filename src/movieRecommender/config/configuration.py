from movieRecommender.components.fetch_data import DataDownloader
from movieRecommender.constants import *
from movieRecommender.utils.common import load_config, create_directories



class ConfigHandler:
    def __init__(self, file_path=CONFIG_FILE_PATH, params_path = PARAMS_FILE_PATH):
        self.config = load_config(file_path)
        self.params = load_config(params_path)

    
    def get_fetch_data_config(self) -> DataDownloader:
        config = self.config.download_config
        fetch_data_config = DataDownloader(
            filepath = config.filepath,
            extract_path= config.extract_path,
            url= config.url
        )
        return fetch_data_config