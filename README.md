# Django x Elasticsearch

## Requirements
    
1. Python > 3.7
2. Django >= 3
3. Elasticsearch 7.15


## Setup Elasticsearch

### Install via brew

* **Install**

    ```
    brew tap elastic/tap
    brew install elasticsearch
    ```

* **Running Elasticsearch**
    ```
    brew services start elasticsearch
    ```

### Manual Installation

1. Download from https://www.elastic.co/downloads/elasticsearch
2. Extract file

    `$ tar -xvf elasticsearch-7.15.0-darwin-x86_64.tar.gz`

3. [Optional] Change port
    This is an optional step, if need different multiple version of elasticsearch running in single machine:
    - `$ nano config/elasticsearch.yml`
    - Uncoment/Add `http.port: 9201`

3. Runing Elasticsearch:

    `$ bin/elasticsearch`


## Setup Apps

* **Installation**

    ```
    pip install -r requirements.txt
    ```

* **Runing Django**

    ```
    ./manage.py migrate
    ./manage.py runserver
    ```

* **Rebuild Index Django**

    ```
    ./manage.py search_index --rebuild
    ```
