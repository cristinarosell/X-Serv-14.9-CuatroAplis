#!/usr/bin/python

import random


class aleat:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 OK", "<html><body><h1>Hola</h1>" +
               "<a href='" + str(random.randrange(10000000)) +
               "'>Dame otra</a>" + "</body></html>")
