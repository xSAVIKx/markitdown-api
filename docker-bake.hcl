group "default" {
  targets = ["markitdown-api"]
}

variable "TIMESTAMP" {
  default = "${timestamp()}"
}
variable "BUILD_DATE" {
  default = "${formatdate("YYYYMMDD", "${TIMESTAMP}")}"
}

target "markitdown-api" {
  dockerfile = "Dockerfile"
  tags = [
    "docker.io/xsavikx/markitdown-api:latest",
    "docker.io/xsavikx/markitdown-api:${BUILD_DATE}"
  ]
  labels = {
    "org.opencontainers.image.created"     = "${TIMESTAMP}"
    "org.opencontainers.image.title"       = "MarkItDown API server"
    "org.opencontainers.image.description" = "Provides REST API on top of the MarkItDown markdown convertion library"
  }
  annotations = [
    "org.opencontainers.image.created=${TIMESTAMP}",
    "org.opencontainers.image.title=MarkItDown API server",
    "org.opencontainers.image.description=Provides REST API on top of the MarkItDown markdown convertion library"
  ]
}
