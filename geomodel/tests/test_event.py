from typing import Any, Dict, List
import unittest

from mozdef_util.query_models import SearchQuery

import mozdef_geomodel.query as query


def query_interface(results: List[Dict[str, Any]]) -> query.QueryInterface:
    '''Produce a `QueryInterface` that just returns the provided results.
    '''

    def closure(q: SearchQuery, esi: str) -> List[str, Any]:
        return results

    return closure
