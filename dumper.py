import os
import datetime

import biothings, config
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT

import biothings.hub.dataload.dumper


class BiotoolsDumper(biothings.hub.dataload.dumper.DummyDumper):

    SRC_NAME = "biotools"
    __metadata__ = {
        "src_meta": {
            "author":{
                "name": "Ginger Tsueng",
                "url": "https://github.com/gtsueng"
            },
            "code":{
                "branch": "main",
                "repo": "https://github.com/outbreak-info/biotools.git"
            },
            "url": "https://bio.tools/t?domain=covid-19",
            "license": "https://biotools.readthedocs.io/en/latest/license.html"
        }
    }
    # override in subclass accordingly
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    
    SCHEDULE = "30 10 * * *"  # daily at 10:30PT

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_release()

    def set_release(self):
        self.release = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
