#!/usr/bin/env python3
"""Envuelve ~/Desktop/palabrero.html (formato artifact, sin <head>) en un
HTML completo y autonomo para servirlo en GitHub Pages."""
import io, os

SRC = os.path.expanduser("~/Desktop/palabrero.html")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

HEAD = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Palabrero">
<meta name="theme-color" content="#0B100E">
<style>
  *{-webkit-text-size-adjust:100%}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>
'''

src = io.open(SRC, encoding="utf-8").read().split("\n")
cut = next(i for i, l in enumerate(src) if l.startswith("<style>"))
out = HEAD + "\n".join(src[:cut]) + "\n</head>\n<body>\n" + "\n".join(src[cut:]) + "\n</body>\n</html>\n"
io.open(OUT, "w", encoding="utf-8").write(out)
print("index.html:", len(out), "bytes")
