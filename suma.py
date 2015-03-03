#!/usr/bin/python


class suma:

    def parse(self, request, rest):
        #request /suma y rest /op1/op2 -- /suma/op1/op2
        try:
            op1 = int(rest.split('/')[1])
            op2 = int(rest.split('/')[2])
        except ValueError:
            return None
        except TypeError:
            return None
        return (op1, op2)

    def process(self, parsedRequest):

        if not parsedRequest:
            return("404 Not found", "<html>" +
                   "<body><h1>Error, introducir numeros</h1>" +
                   "</body></html>")

        result = parsedRequest[0] + parsedRequest[1]
        return("200 OK", "<html><body>" + str(parsedRequest[0]) +
               "+" + str(parsedRequest[1]) + "=" + str(result) +
               "</body></html>")
