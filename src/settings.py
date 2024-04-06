import json
import os

class Settings:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        else:
            return {"exclusions": ["settings.json", "main.py"], "use_gitignore": True}

    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def add_exclusion(self, exclusion):
        self.settings['exclusions'].append(exclusion)
        self.save_settings()

    def get_exclusions(self):
        return self.settings.get('exclusions', [])

    def toggle_setting(self, setting_name):
        self.settings[setting_name] = not self.settings.get(setting_name, False)
        self.save_settings()
