#!/usr/bin/env python3
import os
import io


def process(file):
    bruh = file
    processing = bruh.replace("# ", "<h1>").replace(
        "#<h1>", "<h2>").replace("/#", "</h1>")
    return processing


mdfile = open("index.md", "r")
process_string = mdfile.read()
processed_string = str(process(process_string))

print(processed_string)

with open("index.html", 'a') as out:
    out.write("<DOCTYPE html>" + '\n' + processed_string)
