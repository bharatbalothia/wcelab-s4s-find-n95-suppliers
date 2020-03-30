# S4S - Find Suppliers on IBM SCBN and VAN network


This project leverages popular data science tools to find N95 suppliers whose SCBN or EDI transactions are going through IBM Supply Chain networks. S4S project team leverages this knowledge to approach suppliers with ready for market supply chain technology.

## Setup

Refer to "Get Started" section on [pandas-amex-match](https://github.ibm.com/wcelab/pandas-amex-match) project on how to set up the environment for a Jupyter Notebook development environment.

## Development

search_suppliers.ipynb is the main document with overall process. 

1. It expects two Excel spreads with IBM's SCBN and VAN customers and their transactions.
2. It download N95 supplier list from [CDC NIOSH N95 page](https://www.cdc.gov/niosh/npptl/topics/respirators/disp_part/N95list1-h.html) and its child pages for each letter. 
3. It compares the CDC list with IBM list based with limited naming aproximation capability (see the **matching value** section in search_suppliers.ipynb).
4. It produce an Excel report on the matching result.
