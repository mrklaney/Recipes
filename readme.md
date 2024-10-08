Title: ESRE RAG from Vestal Vector book using Recipes index

Explanation:  RAG application using Elasticsearch and ELSER v2. Has good examples of how RAG can enhance search results.

Installation was done on Strigo using the ESRE Engineer V2 AMI. (However, it is easy to install on a local machine as well.)
The dataset being used are recipes from Kaggle. I checked to see that this particular dataset is under an open license. 
I used filebeat to ingest the data. Why? File Uploader continues to fail and still does with this version of Elastic stack.(version 8.11.0)

The original dataset can be downloaded from https://www.kaggle.com/datasets/nguyentuongquang/all-recipes
(page 173 of Vestal) and is called allrecipes.csv. It is included in the project file.
There are duplicate entries in this original file. I built a python script to deduplicate them.
The script is in the project folder and is called dedupecsv.py.  The deduplicated result file is called allrecipes_.csv, which is also in the project file.
If you want to run the dedupecsv.py yourself, the python library pandas needs to be installed. (e.g. pip install pandas)

Filebeat was used to ingest allrecipes_.csv into Elasticsearch. The configuration file is filebeat.yml and a copy is in the project folder. I followed the "quick install" documentation https://www.elastic.co/guide/en/beats/filebeat/8.11/filebeat-installation-configuration.html to install and use filebeat with version 8.11.4 for Linux self-managed. 
You will need to scp to Strigo both filebeat.yml and allrecipes_.csv.

Running filebeat creates an Elasticsearch index called "recipes."

Once the index is created, all the subsequent steps for the project can be performed in Kibana. See "kibana.txt"







