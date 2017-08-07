# ssence-crawler
code challenge from JACL Omicron Technology

## setup
working environment : OSX 10.12.5

python env
```bash
conda create -name scrapy python=3
source activate scrapy
pip install -r requirements.txt
```

postgresql env
```bash
brew install postgresql
postgres -D /usr/local/var/postgres
psql postgres
# in psql shell
CREATE DABASE ssense;
CREATE TABLE category ( id    interger, name    varchar(1000), seokeyword    varchar(1000));
