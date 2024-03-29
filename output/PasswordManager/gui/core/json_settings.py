# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////

    
    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self,settings_path="default"):
        super(Settings, self).__init__()

        self.json_file = "settings.json"
        self.app_path = os.path.abspath(os.getcwd())
        if settings_path=="default":
            self.settings_path = os.path.normpath(os.path.join(self.app_path, self.json_file))
        elif settings_path=="global":
            self.settings_path=os.path.join(self.get_project_path(),self.json_file)
        else:
            self.settings_path=os.path.join(os.path.join(self.get_project_path(),settings_path),self.json_file)
        if not os.path.isfile(self.settings_path):
            print(f"[WARNING]: \"settings.json\" not found! check in the folder {self.settings_path}")



        # DICTIONARY WITH SETTINGS
        # Just to have objects references
        self.items = {}

        # DESERIALIZE
        self.deserialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # READ JSON FILE
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings

    def get_project_path(self):
        # 项目名称
        p_name = "\gui\core"
        # 获取当前文件的绝对路径
        p_path = os.path.abspath(os.path.dirname(__file__))
        # 通过字符串截取方式获取
        return p_path[:p_path.index(p_name)]
