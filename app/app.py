import datetime
import random
import hashlib
from flask import Flask, request, send_from_directory
from flask_stache import render_view, render_template


app = Flask(
    __name__,
    root_path="/Users/michael/Projects/flake-explorer/src/templates",
    template_folder="/Users/michael/Projects/flake-explorer/src/templates",
    static_url_path="")

app.debug = True


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("css", path)


@app.route("/")
def home():
    html = render_template(
        "header",
        {"file_extension": "html"},
        refresh=False,
        # css_styles=[open(
        #     "/Users/michael/Projects/flake-explorer/src/templates/css/style.css").read()]
    )
    html += render_template(
        "index",
        {"file_extension": "html"},
        server_timestamp=datetime.datetime.utcnow(),
        refresh=False,
        is_page_zero=True,
        blocks=[
            dict(
                height=random.randint(1, 1000000),
                age=datetime.datetime.utcnow().strftime("%H:%m:%S"),
                time_delta="",
                hash=hashlib.md5(str(random.random()).encode()).hexdigest(),
                notx=random.randint(1, 10),
                fees=random.random(),
                outputx=random.random(),
                mixin_range=random.randint(1, 12),
                blksize=random.random()),
        ],
        page_no=0,
        total_page_no=1)
    html += render_template(
        "footer",
        {"file_extension": "html"},
        **dict(
            git_branch_name="git-branch",
            last_git_commit_date=datetime.datetime.utcnow(),
            last_git_commit_hash=hashlib.md5(
                str(random.random()).encode()).hexdigest(),
            api="API",
            monero_version_full="v0-14-1"
        )
    )
    return html


app.run()
