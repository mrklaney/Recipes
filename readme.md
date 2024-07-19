Title: ESRE RAG from Vestal Vector book using Recipes index

Explanation:  RAG application using Elasticsearch and ELSER v2. Has good examples of how a RAG app can enhance search results.

Installation: Strigo using ESRE Engineer V2. 
The dataset being used are recipes from Kaggle. I checked and see that this particular dataset is under an open license. 
I used filebeat to ingest the data. Why? File Uploader continues to fail and still does with this version of Elastic stack.(version 8.11.0)

The original dataset can be downloaded from https://www.kaggle.com/datasets/nguyentuongquang/all-recipes
(page 173 of Vestal) and is called allrecipes.csv. It is included in the project file.
There are duplicate entries in this original file. I built a python script to deduplicate them.
The script is in the project folder and is called dedupecsv.py.  The deduplicated result file is called allrecipes_2.csv, which is also in the project file.

In order to run the dedupecsv.py some python libraries are required. As preferred by many data science practitioners, I use Conda to create environments to isolate and run python projects.  
conda install anaconda::numpy
conda install anaconda::pandas

Filebeat was used to ingest allrecipes_2.csv into Elasticsearch. The configuration file is filebeat.yml aand a copy is in the project folder. I followed the "quick install" documentation https://www.elastic.co/guide/en/beats/filebeat/8.11/filebeat-installation-configuration.html to install and use filebeat with version 8.11.4 for Linux self-managed. 
Need to scp to Strigo both filebeat.yml and allrecipes_2.csv.

Running filebeat creates an index called "recipes."







