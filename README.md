# MarkItDown API Server

This project is a lightweight REST API server built using FastAPI that receives binary data from a file, converts it to Markdown format using the [MarkItDown](https://github.com/microsoft/markitdown) library, and returns the Markdown content.

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
   docker build -t markitdown-api .
   ```

1. Run the docker container

   ```bash
   docker run -d --name markitdown-api -p 8490:8490 markitdown-api
   ```

## Development Workflow

For easier development, a convenience script is included to rebuild the image and restart the container:

1. Make the script executable:

   ```bash
   chmod +x rebuild.sh
   ```

2. Run the script whenever you make changes:

   ```bash
   ./rebuild.sh
   ```

The script will:

- Stop the running container
- Remove the container
- Build a fresh image
- Start a new container
- Verify the container is running

This simplifies the development process when you're making frequent changes to the codebase.

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
- **Accepted file types**: doc, docx, ppt, pptx, pdf, xls, xlsx, txt, csv, json
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

## Acknowledgments

This project was originally based on [elbruno/MarkItDownServer](https://github.com/elbruno/MarkItDownServer)
by Bruno Capuano. We've extended it with additional features and improvements while
maintaining the core functionality.

## License

This project is licensed under the MIT License.
