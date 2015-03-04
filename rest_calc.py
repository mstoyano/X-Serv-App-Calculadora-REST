#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp

operaciones = ["suma", "resta", "mult", "div"]

class calc_rest(webapp.webApp):

    def parse(self, request):

        recurso = request.split()[0]
        operacion = request.split()[1][1:]

        if recurso == "PUT":
            body = request.split()[-1]
        else:
            body = ""

        response = (recurso, operacion, body)

        return response

    def process(self, parsedRequest):

        (recurso, operacion, body) = parsedRequest

        if recurso == "PUT":
            operandos = body.split(',')

            if len(operandos) == 2:
                html = "Operacion realizada con exito!"
                codigo = "200 OK"

                operando1 = float(operandos[0])
                operando2 = float(operandos[1])

                if operacion == "suma":
                    self.resultado = operando1 + operando2
                    self.answer = str(operando1) + " + " + str(operando2) + " = " + str(self.resultado)
                elif operacion == "resta":
                    self.resultado = operando1 - operando2
                    self.answer = str(operando1) + " - " + str(operando2) + " = " + str(self.resultado)
                elif operacion == "mult":
                    self.resultado = operando1 * operando2
                    self.answer = str(operando1) + " * " + str(operando2) + " = " + str(self.resultado)
                elif operacion == "div":
                    try:
                        self.resultado = operando1 / operando2
                        self.answer = str(operando1) + " / " + str(operando2) + " = " + str(self.resultado)
                    except ZeroDivisionError:
                        html = "Estas intentando dividir por cero."
                        codigo = "400 Bad Request"
                else:
                    html = "Operacion no permitida. Intentalo de nuevo."
                    codigo = "400 Bad Request"
            else:
                html = "Error! Solo se admiten dos operandos."
                codigo = "400 Bad Request"

        elif recurso == "GET":
            try:
                html = self.answer
                codigo = "200 OK"
            except AttributeError:
                html = "Primero debes realizar la operacion con PUT"
                codigo = "400 Bad Request"
        else:
            html = "Solo se permite hacer PUT o GET."
            codigo = "400 Bad Request"

        return(codigo, "<html><body><h1> " + html +" </h1></body></html>")

if __name__ == "__main__":
    server = calc_rest("localhost", 1234)
