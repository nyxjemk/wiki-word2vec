#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
USAGE: %(program)s WIKI_XML_DUMP OUTPUT

Converts articles from a Wikipedia dump to a file containing the texts from the
articles. A single line is an article, articles are separted by a newline.

Note: doesn't support lemmatization.

Adapted from:
- http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim

See also:
- https://github.com/piskvorky/gensim/blob/develop/gensim/scripts/make_wikicorpus.py
"""

import logging
import os.path
import sys
from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("Running %s" % ' '.join(sys.argv))

    # Check and process input arguments.
    if len(sys.argv) < 3:
        printgl(globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "

    i = 0
    # Lemmatization is only available for English.
    # Don't construct a dictionary because we're not using it.
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    with open(outp, 'w') as output:
        for text in wiki.get_texts():
            output.write(space.join(text) + "\n")
            i = i + 1
            if (i % 10000 == 0):
                logger.info("Saved " + str(i) + " articles")

    logger.info("Finished saving " + str(i) + " articles")
