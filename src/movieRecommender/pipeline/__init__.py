
class FetchDataPipeline:
    def __init__(self, config):
        self.config = config

    def main(self):
        fetch_data_config = self.config.get_fetch_data_config()
        fetch_data_config.download_file()
        fetch_data_config.unzip_file()


class DataValidationPipeline:
    def __init__(self, config):
        self.config = config
    
    def main(self):
        validation_config_credits = self.config.get_validation_config("tmdb_5000_credits")
        validation_config_credits.validate_dataset()
        validation_config_movies = self.config.get_validation_config("tmdb_5000_movies")
        validation_config_movies.validate_dataset()