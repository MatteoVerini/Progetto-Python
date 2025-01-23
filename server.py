from flask import Flask, request, render_template, redirect
import os, json

template_dir = os.path.abspath("./templates")
app = Flask(__name__, template_folder=template_dir)