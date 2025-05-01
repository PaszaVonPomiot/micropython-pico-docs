import gc
import os


class LoggerCSV:
    def __init__(
        self, file_name: str, csv_headers: list[str], buffer_size: int = 60
    ) -> None:
        self.file_name = file_name
        self.folder_name = "data"
        self.file_path = f"{self.folder_name}/{self.file_name}"
        self.csv_headers = csv_headers
        self.buffer_size = buffer_size  # max. 180
        self.buffer: list[str] = []
        self._post_init()

    def _post_init(self) -> None:
        self._create_data_folder()
        self._create_csv_file()

    def _create_data_folder(self) -> None:
        try:
            os.mkdir(self.folder_name)
        except OSError:  # Folder already exists
            pass

    def _create_csv_file(self) -> None:
        if self._file_exists():
            return
        else:
            with open(self.file_path, mode="w") as file:
                file.write(";".join(self.csv_headers) + "\n")

    def _file_exists(self) -> bool:
        try:
            os.stat(self.file_path)
        except OSError:
            return False
        return True

    def _buffer_full(self) -> bool:
        return len(self.buffer) >= self.buffer_size

    def _add_record_to_buffer(self, record: str) -> None:
        """Use buffer to reduce flash wear"""
        # record = self.sensor.get_record()
        print(record)
        self.buffer.append(record)

    def _serialize_buffer(self) -> str:
        buffer_serialized = "\n".join(self.buffer) + "\n"
        self.buffer.clear()
        return buffer_serialized

    def _save_buffer_to_file(self) -> None:
        serialized_buffer = self._serialize_buffer()
        with open(self.file_path, mode="a") as file:
            file.write(serialized_buffer)
        gc.collect()

    def process_record(self, record: str) -> None:
        self._add_record_to_buffer(record)
        if self._buffer_full():
            self._save_buffer_to_file()
