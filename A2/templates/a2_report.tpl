{%- extends 'lab/index.html.j2' -%}

{%- block html_head -%}
{{ super() }}

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style type="text/css">
    /* =====================================================
       A2 LONDON AIRBNB REPORT TEMPLATE
       Color Profile: Dark Teal with Coral Accent
       PDF-Optimized with explicit colors for print
       ===================================================== */
    
    /* Force background colors in print */
    * {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        color-adjust: exact !important;
    }
    
    html {
        background-color: #001d1c !important;
    }
    
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-size: 11pt !important;
        line-height: 1.7 !important;
        color: #ffffff !important;
        background-color: #001d1c !important;
        max-width: 950px !important;
        margin: 0 auto !important;
        padding: 30px !important;
    }
    
    /* Header styling */
    h1 {
        color: #ffffff !important;
        border-bottom: 4px solid #FF385C !important;
        padding-bottom: 12px !important;
        margin-top: 35px !important;
        font-size: 2.2em !important;
        font-weight: 700 !important;
    }
    
    h2 {
        color: #e4e4e4 !important;
        border-left: 5px solid #00A699 !important;
        padding-left: 15px !important;
        margin-top: 30px !important;
        font-size: 1.7em !important;
        font-weight: 600 !important;
    }
    
    h3 {
        color: #ffffff !important;
        margin-top: 25px !important;
        font-size: 1.4em !important;
        font-weight: 600 !important;
    }
    
    h4 {
        color: #e4e4e4 !important;
        margin-top: 18px !important;
        font-size: 1.15em !important;
        font-weight: 600 !important;
    }
    
    h5, h6 {
        color: #c2dcc8 !important;
    }
    
    /* Horizontal rules */
    hr {
        border: none !important;
        border-top: 2px solid #013f3a !important;
        margin: 35px 0 !important;
    }
    
    /* All paragraph and text elements */
    p, span, div, li, td, th, label {
        color: #e4e4e4 !important;
    }
    
    /* Code cells */
    .jp-InputArea {
        background-color: #01332b !important;
        border-left: 4px solid #00A699 !important;
        padding: 12px !important;
        margin: 18px 0 !important;
        border-radius: 6px !important;
    }
    
    .jp-InputArea pre, .jp-InputArea code, .jp-InputArea span {
        color: #e4e4e4 !important;
    }
    
    .jp-InputPrompt {
        color: #00A699 !important;
        font-weight: bold !important;
        font-family: 'Space Mono', monospace !important;
    }
    
    .jp-OutputPrompt {
        color: #FF385C !important;
        font-weight: bold !important;
        font-family: 'Space Mono', monospace !important;
    }
    
    /* Code syntax highlighting - force light text */
    pre {
        background-color: #01332b !important;
        padding: 18px !important;
        border-radius: 8px !important;
        border: 1px solid #013f3a !important;
        overflow-x: auto !important;
        font-size: 9pt !important;
        line-height: 1.5 !important;
        color: #e4e4e4 !important;
        font-family: 'Space Mono', monospace !important;
    }
    
    pre * {
        color: #e4e4e4 !important;
    }
    
    code {
        background-color: #002b27 !important;
        padding: 3px 8px !important;
        border-radius: 4px !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 9pt !important;
        color: #FF385C !important;
    }
    
    /* Syntax highlighting overrides for dark theme */
    .highlight .c, .highlight .c1, .highlight .cm { color: #6a9955 !important; } /* Comments - green */
    .highlight .k, .highlight .kn, .highlight .kd { color: #569cd6 !important; } /* Keywords - blue */
    .highlight .s, .highlight .s1, .highlight .s2 { color: #ce9178 !important; } /* Strings - orange */
    .highlight .n, .highlight .na, .highlight .nb { color: #9cdcfe !important; } /* Names - light blue */
    .highlight .nf, .highlight .nc { color: #dcdcaa !important; } /* Functions/Classes - yellow */
    .highlight .o, .highlight .p { color: #d4d4d4 !important; } /* Operators - light gray */
    .highlight .mi, .highlight .mf { color: #b5cea8 !important; } /* Numbers - light green */
    .highlight .bp { color: #4ec9b0 !important; } /* Built-in - teal */
    
    /* Output cells */
    .jp-OutputArea {
        background-color: #002b27 !important;
        border-left: 4px solid #FF385C !important;
        padding: 12px !important;
        margin: 12px 0 !important;
        border-radius: 6px !important;
    }
    
    .jp-OutputArea-output {
        font-family: 'Space Mono', monospace !important;
        font-size: 9pt !important;
        line-height: 1.6 !important;
        color: #e4e4e4 !important;
    }
    
    .jp-OutputArea-output * {
        color: #e4e4e4 !important;
    }
    
    /* Tables */
    table {
        border-collapse: collapse !important;
        width: 100% !important;
        margin: 25px 0 !important;
        font-size: 10pt !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }
    
    th {
        background: linear-gradient(135deg, #00A699 0%, #008577 100%) !important;
        color: #ffffff !important;
        padding: 14px !important;
        text-align: left !important;
        font-weight: 600 !important;
        border: 1px solid #013f3a !important;
    }
    
    td {
        padding: 12px !important;
        border: 1px solid #013f3a !important;
        background-color: #002b27 !important;
        color: #e4e4e4 !important;
    }
    
    tr:nth-child(even) td {
        background-color: #01332b !important;
    }
    
    /* Markdown content */
    .jp-MarkdownOutput {
        padding: 12px 0 !important;
    }
    
    .jp-MarkdownOutput p {
        margin: 12px 0 !important;
        text-align: justify !important;
        color: #e4e4e4 !important;
    }
    
    .jp-MarkdownOutput ul, .jp-MarkdownOutput ol {
        margin: 12px 0 12px 25px !important;
        color: #e4e4e4 !important;
    }
    
    .jp-MarkdownOutput li {
        margin: 6px 0 !important;
        line-height: 1.7 !important;
        color: #e4e4e4 !important;
    }
    
    /* Strong and emphasis */
    strong, b {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    em, i {
        color: #c2dcc8 !important;
    }
    
    /* Blockquotes */
    blockquote {
        border-left: 4px solid #F5A623 !important;
        padding-left: 20px !important;
        margin: 18px 0 !important;
        color: #c2dcc8 !important;
        font-style: italic !important;
        background-color: rgba(245, 166, 35, 0.1) !important;
        padding: 18px 22px !important;
        border-radius: 6px !important;
    }
    
    /* Links */
    a {
        color: #00A699 !important;
        text-decoration: none !important;
        font-weight: 500 !important;
    }
    
    a:hover {
        color: #FF385C !important;
        text-decoration: underline !important;
    }
    
    /* Images and plots */
    img {
        max-width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 25px auto !important;
        border-radius: 10px !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important;
        border: 1px solid #013f3a !important;
    }
    
    /* DataFrame / pandas output */
    .dataframe {
        background-color: #01332b !important;
        color: #e4e4e4 !important;
    }
    
    .dataframe th {
        background: linear-gradient(135deg, #00A699 0%, #008577 100%) !important;
        color: #ffffff !important;
    }
    
    .dataframe td {
        background-color: #002b27 !important;
        color: #e4e4e4 !important;
    }
    
    .dataframe tr:nth-child(even) td {
        background-color: #01332b !important;
    }
    
    /* Rendered HTML output (like df.to_html()) */
    .rendered_html table {
        background-color: #01332b !important;
    }
    
    .rendered_html th {
        background: #00A699 !important;
        color: #ffffff !important;
    }
    
    .rendered_html td {
        background-color: #002b27 !important;
        color: #e4e4e4 !important;
    }
    
    /* Page breaks for PDF */
    @media print {
        html, body {
            background-color: #001d1c !important;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        
        h1, h2 {
            page-break-after: avoid !important;
        }
        
        pre, blockquote, table {
            page-break-inside: avoid !important;
        }
        
        .jp-Cell {
            page-break-inside: avoid !important;
        }
    }
    
    /* Header banner */
    .header-banner {
        background: linear-gradient(135deg, #01332b 0%, #002b27 50%, #01332b 100%) !important;
        border: 2px solid #013f3a !important;
        color: #ffffff !important;
        padding: 40px !important;
        text-align: center !important;
        border-radius: 16px !important;
        margin-bottom: 40px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .header-banner::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 4px !important;
        background: linear-gradient(90deg, #FF385C, #00A699, #FF385C) !important;
    }
    
    .header-banner h1 {
        color: #ffffff !important;
        border: none !important;
        margin: 0 !important;
        font-size: 2.4em !important;
        font-weight: 700 !important;
    }
    
    .header-banner .subtitle {
        margin: 15px 0 0 0 !important;
        font-size: 1.2em !important;
        color: #c2dcc8 !important;
    }
    
    .header-banner .group-tag {
        display: inline-block !important;
        margin-top: 20px !important;
        padding: 8px 20px !important;
        background: #FF385C !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: 600 !important;
        font-size: 0.95em !important;
    }
    
    .header-banner .meta-info {
        margin-top: 25px !important;
        font-size: 0.95em !important;
        color: #c2dcc8 !important;
    }
    
    .header-banner .meta-info strong {
        color: #00A699 !important;
    }
    
    /* Metadata footer */
    .metadata-footer {
        margin-top: 50px !important;
        padding: 25px !important;
        background-color: #01332b !important;
        border: 1px solid #013f3a !important;
        border-radius: 12px !important;
        font-size: 0.9em !important;
        color: #c2dcc8 !important;
    }
    
    .metadata-footer p {
        margin: 8px 0 !important;
        color: #c2dcc8 !important;
    }
    
    .metadata-footer strong {
        color: #00A699 !important;
    }
    
    /* Alert/Info boxes */
    .alert-success {
        background-color: rgba(0, 166, 153, 0.15) !important;
        border-left: 4px solid #00A699 !important;
        padding: 18px !important;
        margin: 18px 0 !important;
        border-radius: 6px !important;
        color: #e4e4e4 !important;
    }
    
    .alert-info {
        background-color: rgba(0, 166, 153, 0.1) !important;
        border-left: 4px solid #00A699 !important;
        padding: 18px !important;
        margin: 18px 0 !important;
        border-radius: 6px !important;
        color: #e4e4e4 !important;
    }
    
    .alert-warning {
        background-color: rgba(245, 166, 35, 0.15) !important;
        border-left: 4px solid #F5A623 !important;
        padding: 18px !important;
        margin: 18px 0 !important;
        border-radius: 6px !important;
        color: #e4e4e4 !important;
    }
    
    /* Cell spacing */
    .jp-Cell {
        margin-bottom: 25px !important;
    }
    
    /* Notebook cell container */
    .jp-Notebook {
        background-color: #001d1c !important;
    }
    
    /* Override any default black text */
    .jp-RenderedText, .jp-RenderedText pre {
        color: #e4e4e4 !important;
    }
    
    /* Stream output (print statements) */
    .jp-OutputArea-output pre {
        color: #e4e4e4 !important;
        background-color: #002b27 !important;
    }
</style>
{%- endblock html_head -%}

{%- block body_header -%}
<div class="header-banner">
    <h1>🏠 London Airbnb Pricing Analysis</h1>
    <p class="subtitle">Multiple Linear Regression Model for Nightly Price Prediction</p>
    <span class="group-tag">Group 5 • BAN-0200</span>
    <p class="meta-info">
        <strong>Course:</strong> Business Analytics | 
        <strong>Institution:</strong> Hult International Business School | 
        <strong>Term:</strong> 2024-2025
    </p>
</div>
{%- endblock body_header -%}

{%- block body_footer -%}
<div class="metadata-footer">
    <p><strong>📅 Generated:</strong> {{ resources.metadata.get('date', 'December 2024') }}</p>
    <p><strong>📓 Notebook:</strong> Grp_5_BAN_0200_Regression_project_Final.ipynb</p>
    <p><strong>📄 Export Format:</strong> PDF via nbconvert (webpdf)</p>
    <p style="margin-top: 15px; font-size: 0.85em; border-top: 1px solid #013f3a; padding-top: 15px;">
        <strong>Data Source:</strong> Inside Airbnb — London Dataset (2024)<br>
        <strong>Statistical Analysis:</strong> Python (pandas, numpy, statsmodels, scipy, matplotlib, seaborn)<br>
        <strong>Model:</strong> OLS Multiple Linear Regression with Log-transformed Price
    </p>
</div>
{%- endblock body_footer -%}
