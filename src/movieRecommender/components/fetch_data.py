import os
import zipfile
import requests
from pathlib import Path
from movieRecommender.logging import logger
from dataclasses import dataclass

@dataclass(frozen=True)
class DataDownloader:
    filepath: Path
    extract_path: Path 
    filename: str
    url: str

    def download_file(self) -> None:
        """
        Downloads a file from a URL and saves it to the local file system.
        
        Args:
            url (str): The URL of the file to download.
            file_path (str): The local file path to save the downloaded file.
            logger (logging.Logger): A logger object to log the progress.
        
        Returns:
            None
        """
        try:
            file_path = os.path.join(os.getcwd(), self.filepath, self.filename)
            os.makedirs(self.filepath, exist_ok=True)
            response = requests.get(self.url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            downloaded = 0

            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=block_size):
                    if chunk:
                        file.write(chunk)
                        downloaded += len(chunk)
                        progress = round((downloaded / total_size) * 100, 2)
                        logger.info(f'Downloaded {progress}% of the file')

            logger.info('Download complete!')
        except Exception as e:
            logger.error(f'Error downloading file: {e}')
            return e

            

    def unzip_file(self):
        """
        Extracts the contents of a ZIP file to the specified directory.
        
        Args:
            file_path (str): The path to the ZIP file.
            extract_path (str): The directory where the contents will be extracted.
        
        Returns:
            None
        """
        try:
            os.makedirs(self.extract_path, exist_ok=True)
            with zipfile.ZipFile(self.filepath + '/' + self.filename, 'r') as zip_ref:
                zip_ref.extractall(self.extract_path)
            logger.info(f'Extraction complete. Files extracted to {self.extract_path}')
        except Exception as e:
            logger.error(f'Error extracting file: {e}')

