class FileManager:

    @staticmethod
    def save_html(html, filepath):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(html)