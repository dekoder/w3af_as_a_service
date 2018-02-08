"""
addreq.py

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
from w3af.core.data.request.fuzzable_request import FuzzableRequest
from w3af.core.data.dc.cookie import Cookie
from w3af.core.data.dc.factory import dc_from_hdrs_post
from w3af.core.data.dc.headers import Headers

from w3af import urllist

import Queue
urllist.req_queue = Queue.Queue()

@app.route('/scans/addreq', methods=['POST'])
def add_req():
    url = request.form.get('url')
    method = request.form.get('method')
    post_data = request.form.get('post_data')
    cookie_string = request.form.get('cookie')
    
    headers = request.form.get('headers')
    headers = Headers(json.loads(headers).items())   

    freq = FuzzableRequest(url, method, headers,
            Cookie(cookie_string),
            dc_from_hdrs_post(headers, post_data))
    urllist.req_queue.put_nowait(freq)   

    return jsonify({"status": True})

