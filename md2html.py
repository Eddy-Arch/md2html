#!/usr/bin/env python3
import os
import io


try:
    os.remove("index.html")
except:
    print("cleaned index.html")


def process(file):
    bruh = file
    processing = bruh.replace("/#b", "</body>").replace("# ", "<h1>").replace(
        "#<h1>", "<h2>").replace("#<h3>", "<h4>").replace("#<h2>", "<h3>").replace("/#", "</h1>").replace("</h1>#", "</h2>").replace("</h2>#", "<h3>").replace("#b", " <body>")

    return processing


mdfile = open("index.md", "r")
process_string = mdfile.read()
processed_string = str(process(process_string))

print(processed_string)

with open("index.html", 'a') as out:
    out.write("<DOCTYPE html>" + '\n' +
              "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">" + '\n' + processed_string)
