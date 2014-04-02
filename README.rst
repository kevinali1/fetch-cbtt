==============
Fetch-CBTT
==============
A python module to fetch economic time-series from the 
Central Bank of Trinidad &Tobago

Contributors
============
* `Kevin Ali <https://github.com/kevinali1>`_

Installation
=============
``fetch-cbtt`` requires `numpy` and `Pandas` A its main 
requirements. Other requirements should not require compilation::

    pip install -r requirements.txt
    git clone https://github.com/kevinali1/fetch-cbtt.git


Refresh the cache
============

Run the following to refresh the cache::
    import cb_scrape
    cb_scrape.refresh_link_cache()




.. end-here