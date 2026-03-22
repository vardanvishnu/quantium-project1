import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

import pytest
from app import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Dashboard"


def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_radio_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None