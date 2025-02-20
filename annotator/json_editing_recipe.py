from pathlib import Path

import prodigy
from prodigy import set_hashes
from prodigy.components.stream import get_stream

CWD = Path(__file__).parent
HTML_TEMPLATE = """<button onClick="copyAllItems()">Copy data</button>
<p id="text" style="margin-top: 10px;">{{text}}</p>
<br />
<p id="annotation">{{annotated_texts_and_labels}}</p>
<br />
<pre id="json" style="margin-top: 10px;">{{orig_json}}</pre>"""


@prodigy.recipe("fix-json-outputs")
def fix_json_outputs(dataset, file_path):
    stream = get_stream(file_path)
    stream = (set_hashes(eg, input_keys=("text", "annotated_texts_and_labels")) for eg in stream)

    return {
        "dataset": dataset,
        "stream": stream,
        "view_id": "blocks",
        "config": {
            "blocks": [
                {"view_id": "html", "html_template": HTML_TEMPLATE},
                {"view_id": "text_input", "field_rows": 5},
            ],
            "javascript": (CWD / "copy.js").read_text(),
        }
    }
