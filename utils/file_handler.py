def save_temp_file(binary_data: bytes, filename: str) -> str:
    import os
    import tempfile

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)

    with open(file_path, "wb") as temp_file:
        temp_file.write(binary_data)

    return file_path


def delete_file(file_path: str) -> None:
    import os

    if os.path.exists(file_path):
        os.remove(file_path)
