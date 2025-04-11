# MarkItDown Web Server

This project is a simple web server application built using FastAPI that receives binary data from a file, converts it to Markdown format using the MarkItDown library, and returns the Markdown content.

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

## Endopoints

## Testing the application

You can quickly test that the application is running by uploading a file via cUrl, like so:

```sh
url -X POST -F "file=@;path/to/mypdf.pdf" http://localhost:8490/process_file
```

The result should be a string encoding a JSON object like:

```json
{ "markdown": "Your content written in markdown..." }
```

## Dependencies

- FastAPI
- MarkItDown

## License

This project is licensed under the MIT License.
