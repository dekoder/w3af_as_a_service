"""
addurl.py

Copyright 2015 Andres Riancho

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
from flask import jsonify, request
from w3af.core.ui.api import app
from w3af import urllist
from w3af.core.data.parsers.doc.url import URL

import Queue
urllist.url_queue = Queue.Queue()

@app.route('/scans/addurl', methods=['POST'])
def add_url():
    url = request.json["url"]
    if url:
        urllist.url_queue.put_nowait(URL(url))
   
    return jsonify({"status": True})

