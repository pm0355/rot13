#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import string
import codecs

form ="""
<html><head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text" style="height: 100px; width: 400px;">%(rot13)s</textarea>
      <br>
      <input type="submit">
    </form>
  

</body></html>

"""


def escape_html(s):
    return cgi.escape(s,quote=True)

def rot13(s):
    return codecs.encode(s,'rot13')


class Rot13Handler(webapp2.RequestHandler):
    def write_form(self,rot13=""):
	self.response.out.write(form %{"rot13":escape_html(rot13)})

    def get(self):
        self.write_form()

    def post(self):
        user_input= self.request.get('text')
        input_changed=rot13(user_input)
        self.write_form(input_changed)

      
app= webapp2.WSGIApplication([('/',Rot13Handler)], debug=True)
