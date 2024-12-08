Title: Semantic, Vector, and Hybrid Search all in Kibana Console

Explanation:  Enhance existing Elasticsearch searches with ELSER. This demo has good examples of how semantic vectors can enhance regular "keyword" search results.

Installation was done on Strigo using the "ESRE Engineer V2" AMI. However, it is easy to install on a locally running or cloud Elasticsearch and Kibana as well.

The dataset being used are recipes from Kaggle. I checked to see that this particular dataset is under an open license. 

The original dataset can be downloaded from [here](https://www.kaggle.com/datasets/nguyentuongquang/all-recipes)
(which is discussed on page 173 of Vestal's book, [Vector Search for Practitioners with Elastic](https://www.amazon.com/Vector-Search-Practitioners-Elastic-observability/dp/1805121022) ) and is called allrecipes.csv. It is included in the project file.


There are duplicate entries in this original file. I built a python script to deduplicate them.
The script is in the project folder and is called dedupecsv.py.  The deduplicated result file is called allrecipes_dedupe.csv, which is also in the project file.
If you want to run the dedupecsv.py yourself, the python library pandas needs to be installed. (e.g. pip install pandas)

I was able to use both Filebeat and (even easier) the File Uploader in Kibana to ingest the data into an index in Elasticsearch, most recently using version 8.13.4 but in older versions as well. If you use Filebeat to ingest allrecipes_.csv into Elasticsearch, the configuration file is filebeat.yml and a copy is in the project folder. I followed the "quick install" [documentation](https://www.elastic.co/guide/en/beats/filebeat/8.11/filebeat-installation-configuration.html) to install and use filebeat for Linux self-managed. 
If you are using Strigo,  scp  both filebeat.yml and allrecipes_.csv to your instance.

Running filebeat creates an Elasticsearch index called "recipes."  Be sure to use this name if you opt to use File Uploader.

Once the index is created, all the subsequent steps for the project can be performed in Kibana. See "kibana.txt" in the project folder.







