FROM python:3.10-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONHASHSEED=random
ENV PYTHONUNBUFFERED=1

#FROM base AS python-deps
WORKDIR /app

# Set timezone
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Install python dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc git tree
RUN python -m venv venv
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root


#FROM base AS runtime
#WORKDIR /app

# Install application into container
# Don't forget to check the .dockerignore
#COPY --from=python-deps /app/venv venv
COPY . .

# Create and switch to a new user
RUN useradd --create-home appuser
USER appuser
RUN tree /app/hubitatcontrol
RUN tree /app/tests
# Run the executable
RUN pip freeze
CMD [ "pytest" ]
