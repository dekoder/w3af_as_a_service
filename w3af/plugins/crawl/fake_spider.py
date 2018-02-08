"""
fake_spider.py

Copyright 2006 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""

from w3af.core.controllers.plugins.crawl_plugin import CrawlPlugin
from w3af.core.controllers.exceptions import RunOnce, BaseFrameworkException
from w3af.core.controllers.misc.decorators import runonce

import time

from w3af.urllist import url_queue, req_queue

class fake_spider(CrawlPlugin):
    """
    """

    def __init__(self):
        CrawlPlugin.__init__(self)
    
    @runonce(exc_class=RunOnce)
    def crawl(self, fuzzable_request):
        """
        :param fuzzable_request: A fuzzable_request instance that contains
                                    (among other things) the URL to test.
        """
        while True:
            ul = []
            rl = []
            
            while True:
                try:
                    url = url_queue.get_nowait()
                    ul.append(url)
                except Queue.Empty:
                    break
            
            while True:
                try:
                    freq = req_queue.get_nowait()
                    rl.append(freq)
                except Queue.Empty:
                    break
            
            for freq in rl:
                self.output_queue.put(freq)

            self.worker_pool.map(self.http_get_and_parse, ul)

            time.sleep(2)

