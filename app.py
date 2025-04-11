import logging
import os
import tempfile

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from markitdown import MarkItDown

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MarkItDown Server",
    description="API endpoint to extract text and convert it to markdown, using MarkItDown (https://github.com/microsoft/markitdown).",
)

ALLOWED_EXTENSIONS = {
    "doc",
    "docx",
    "ppt",
    "pptx",
    "pdf",
    "xls",
    "xlsx",
    # "odt",
    # "ods",
    # "odp",
    "txt",
    "csv",
    "json"
}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def convert_to_md(filepath: str) -> str:
    logger.info(f"Converting file: {filepath}")
    markitdown = MarkItDown()
    result = markitdown.convert(filepath)
    logger.info(f"Conversion result: {result.text_content[:100]}")
    return result.text_content


@app.get("/")
def read_root():
    return {"MarkItDown Server": "hit /docs for endpoint reference"}


@app.post("/process_file")
async def process_file(file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        return JSONResponse(content={"error": "File type not allowed"}, status_code=400)

    try:
        # Save the file to a temporary directory
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name
            logger.info(f"Temporary file path: {temp_file_path}")

        # Convert the file to markdown
        markdown_content = convert_to_md(temp_file_path)
        logger.info("File converted to markdown successfully")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

    finally:
        # Ensure the temporary file is deleted
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            logger.info(f"Temporary file deleted: {temp_file_path}")

    return JSONResponse(content={"markdown": markdown_content})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8490)
