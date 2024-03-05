import warnings
from unittest.mock import Mock, patch

def test_verbose_get_before_set():
    from langchain_core.globals import get_verbose

    with warnings.catch_warnings(record=True) as w:
        with patch.dict('sys.modules', {'langchain': Mock(spec=[])}):
            assert get_verbose() == False
        assert len(w) > 0
