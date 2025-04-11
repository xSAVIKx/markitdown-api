# MarkItDown Web Server

This project is a lightweight REST API server built using FastAPI that receives binary data from a file, converts it to Markdown format using the MarkItDown library, and returns the Markdown content.

This project started as a fork of [elbruno/MarkItDownServer](https://github.com/elbruno/MarkItDownServer).

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

1. Navigate to the project directory:

   ```bash
   cd <the folder where you cloned the repo>
   ```

1. Build the docker image

   ```bash
   docker build -t markitdownserver .
   ```

1. Run the docker container

   ```bash
   docker run -d --name markitdownserver -p 8490:8490 markitdownserver
   ```

## Endpoints

The API offers two main endpoints:

### `/docs`

Provides an interactive documentation interface where you can:

- Explore the API capabilities
- Test the conversion feature directly in your browser
- View request/response schemas and examples

### `/process_file`

Accepts a POST request containing a file to convert to markdown.

- **Method**: POST
- **Content-Type**: multipart/form-data
- **Parameter**: file (binary)
- **Accepted file types**: doc, docx, ppt, pptx, pdf, xls, xlsx, odt, ods, odp, txt
- **Returns**: JSON object with the converted markdown content

## Testing the application

You can quickly test that the application is running by uploading a file via cUrl, like so:

```sh
curl -X POST -F "file=@path/to/mypdf.pdf" http://localhost:8490/process_file
```

The result should be a string encoding a JSON object like:

```json
{ "markdown": "Your content written in markdown..." }
```

## Main Dependencies

- FastAPI
- MarkItDown
- Uvicorn

## License

This project is licensed under the MIT License.
