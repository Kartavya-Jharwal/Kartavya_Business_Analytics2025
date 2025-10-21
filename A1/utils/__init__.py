# Utils package
from .data_loader import (
    load_gdp_data,
    load_co2_data,
    load_netzero_data,
    merge_gdp_co2,
    create_gdp_categories,
    create_commitment_strength,
    get_latest_year_data,
    format_large_number,
)

from .styling import (
    get_custom_css,
    get_plotly_theme,
    create_metric_card_html,
    render_navbar,
    render_page_header,
    render_breadcrumbs,
    render_sticky_footer,
    render_sidebar_resources,
)

__all__ = [
    "load_gdp_data",
    "load_co2_data",
    "load_netzero_data",
    "merge_gdp_co2",
    "create_gdp_categories",
    "create_commitment_strength",
    "get_latest_year_data",
    "format_large_number",
    "get_custom_css",
    "get_plotly_theme",
    "create_metric_card_html",
    "render_navbar",
    "render_page_header",
    "render_breadcrumbs",
    "render_sticky_footer",
    "render_sidebar_resources",
]
