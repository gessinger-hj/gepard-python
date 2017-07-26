#!/bin/sh

pandoc README.md -o README.rst
sed -i '' '/\.\. raw:: html/,/<!-- \/MarkdownTOC -->/d' README.rst;

