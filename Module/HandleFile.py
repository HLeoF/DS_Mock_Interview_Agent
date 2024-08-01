import time, os
from langchain.agents import tool

class HandleFile:
    
    @tool
    def create_timestamp():
        """
        Create a timestamp
        """
        timestamp = int(time.time() * 1000)
        return timestamp
    
    @tool
    def build_folder(FolderName):
        try:
            os.makedirs(os.path.join("Interview_history", FolderName))
            return os.path.abspath(FolderName)
        except OSError as e:
            print(f"文件夹创建失败：{e}")
            return None