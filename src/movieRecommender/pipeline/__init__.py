
class FetchDataPipeline:
    def __init__(self, config):
        self.config = config

    def main(self):
        fetch_data_config = self.config.get_fetch_data_config()
        fetch_data_config.download_file()
        fetch_data_config.unzip_file()

