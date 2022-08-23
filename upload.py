import biothings.hub.dataload.uploader
import os

import requests
import biothings
import config
biothings.config_for_app(config)

MAP_URL = "https://raw.githubusercontent.com/SuLab/outbreak.info-resources/master/outbreak_resources_es_mapping_v3.json"
MAP_VARS = ["@type", "date", "author", "citedBy", "curatedBy", "dateModified", "datePublished", "doi", "funding", "identifier", "citedBy", "license", "name", "doi", "isRelatedTo", "evaluations","topicCategory"]

# when code is exported, import becomes relative
try:
    from biotools.parser import load_annotations as parser_func
except ImportError:
    from .parser import load_annotations as parser_func


class BiotoolsUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    main_source="biotools"
    name = "biotools"
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
    idconverter = None
    storage_class = biothings.hub.dataload.storage.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("No data to load from file for biotools")
        return parser_func()

    @classmethod
    def get_mapping(klass):
        r = requests.get(MAP_URL)
        if(r.status_code == 200):
            mapping = r.json()
            mapping_dict = { key: mapping[key] for key in MAP_VARS }
            return mapping_dict
