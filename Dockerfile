# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --upgrade pip && pip install .

# Copy source and test files
COPY src ./src
COPY tests ./tests

# Expose app port (if needed)
EXPOSE 8000

# Default command: run tests
CMD ["pytest", "-v"]
