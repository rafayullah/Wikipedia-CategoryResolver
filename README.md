# Wikipedia Category Resolver

Entity Recognition has a pivotal role in Natural Language Processing. It is a process in which a subject/object present in a textual sentence has to be identified and then resolved to provide a better understanding of the text.

The project uses Wikipedia's search API to parse the categories of identified verbs/nouns to their categories in an unsupervised manner. By default, every page that exists on Wikipedia has a category associated with it. The purpose of this project is to programmatically fetch the information, to be used in NLP pipelines.

Using this information, we can identify entities that are similar to each other rather than manually tagging all entities by human supervision.

Let's take a look at an example:
When the word 'IBM' is searched on Wikipedia, we get the following webpage:
https://en.wikipedia.org/wiki/IBM

While navigating, the bottom of the webpage has a section of categories the searched entity belongs to. This is what now you can fetch programmatically using this project.

## Setup
* The project is available as a Python Package at [PyPi - Wikipedia Category Resolver] (https://pypi.org/project/WikipediaCategoryResolver/)
```
pip install WikipediaCategoryResolver
```

OR

* You can use the Python file WikipediaCategoryResolver.py provided in the projects directory which uses:
```
pip install requests
pip install json
pip install re
```
These packages are by default already installed.


## Usage
In the projects directory, the module can be used by using the following lines in your code:
```
from WikipediaCategoryResolver import Wiki
wiki = Wiki()
wiki.get_category('IBM')  #Example
```

See the Usage.ipynb for more details


## Results
* Output of single category resolution:
![Image 1](WCR Category.png)
* Finding common attributes between multiple entities:
![Image 2](WCR Similarity.png)


## Authors
* [Rafay Ullah Choudhary](https://github.com/rafayullah)


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Acknowledgements
* [Wikipedia](https://www.wikipedia.org) 

