
from app import app


def test_header_exists():
    """
    Test if the header element with ID "header" exists in the app layout.
    """
    layout = app.layout
    assert layout is not None, "App layout is missing."

    header = layout.children[0]
    assert header.id == "header", "Header element with ID 'header' is missing."


def test_visualization_exists():
    """
    Test if the visualization (graph) with ID "visualization" exists in the app layout.
    """
    layout = app.layout
    assert layout is not None, "App layout is missing."

    graph = layout.children[2]
    assert graph.id == "visualization", "Graph element with ID 'visualization' is missing."


def test_region_picker_exists():
    """
    Test if the region picker (radio button) with ID "region-filter" exists in the app layout.
    """
    layout = app.layout
    assert layout is not None, "App layout is missing."
    region_picker = layout.children[1]
    assert region_picker.id == "region-filter", "Region picker with ID 'region-filter' is missing."











