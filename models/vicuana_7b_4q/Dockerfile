FROM python:3.10-slim-bullseye
EXPOSE 8000

RUN apt update && apt install -y libopenblas-dev ninja-build build-essential wget
RUN python -m pip --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org install --upgrade pip pytest cmake scikit-build setuptools

WORKDIR /usr/src/app/

COPY requirements.txt ./

RUN pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org --no-cache-dir -r ./requirements.txt --upgrade pip

COPY . .

CMD python main.py