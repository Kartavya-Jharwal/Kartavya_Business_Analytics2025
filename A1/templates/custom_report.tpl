{%- extends 'lab/index.html.j2' -%}

{%- block html_head -%}
{{ super() }}

<style type="text/css">
    /* Custom styling for beautiful PDF output */
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #2c3e50;
        background-color: #ffffff;
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Header styling */
    h1 {
        color: #2c3e50;
        border-bottom: 4px solid #3498db;
        padding-bottom: 10px;
        margin-top: 30px;
        font-size: 2.2em;
        font-weight: 700;
    }
    
    h2 {
        color: #34495e;
        border-left: 5px solid #3498db;
        padding-left: 15px;
        margin-top: 25px;
        font-size: 1.8em;
        font-weight: 600;
    }
    
    h3 {
        color: #2c3e50;
        margin-top: 20px;
        font-size: 1.4em;
        font-weight: 600;
    }
    
    h4 {
        color: #34495e;
        margin-top: 15px;
        font-size: 1.2em;
        font-weight: 600;
    }
    
    /* Horizontal rules */
    hr {
        border: none;
        border-top: 2px solid #bdc3c7;
        margin: 30px 0;
    }
    
    /* Code cells */
    .jp-InputArea {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        padding: 10px;
        margin: 15px 0;
        border-radius: 4px;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 9pt;
    }
    
    .jp-InputPrompt {
        color: #3498db;
        font-weight: bold;
    }
    
    .jp-OutputPrompt {
        color: #27ae60;
        font-weight: bold;
    }
    
    /* Code syntax highlighting */
    pre {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #e1e4e8;
        overflow-x: auto;
        font-size: 9pt;
        line-height: 1.4;
    }
    
    code {
        background-color: #f1f3f5;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 9pt;
        color: #e74c3c;
    }
    
    /* Output cells */
    .jp-OutputArea {
        background-color: #ffffff;
        border-left: 4px solid #27ae60;
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
    }
    
    .jp-OutputArea-output {
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 9pt;
        line-height: 1.5;
    }
    
    /* Tables */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        font-size: 10pt;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    th {
        background-color: #3498db;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
        border: 1px solid #2980b9;
    }
    
    td {
        padding: 10px;
        border: 1px solid #ddd;
        background-color: #ffffff;
    }
    
    tr:nth-child(even) td {
        background-color: #f8f9fa;
    }
    
    tr:hover td {
        background-color: #e8f4f8;
    }
    
    /* Markdown content */
    .jp-MarkdownOutput {
        padding: 10px 0;
    }
    
    .jp-MarkdownOutput p {
        margin: 10px 0;
        text-align: justify;
    }
    
    .jp-MarkdownOutput ul, .jp-MarkdownOutput ol {
        margin: 10px 0 10px 20px;
    }
    
    .jp-MarkdownOutput li {
        margin: 5px 0;
        line-height: 1.6;
    }
    
    /* Blockquotes */
    blockquote {
        border-left: 4px solid #f39c12;
        padding-left: 20px;
        margin: 15px 0;
        color: #7f8c8d;
        font-style: italic;
        background-color: #fef9e7;
        padding: 15px 20px;
        border-radius: 4px;
    }
    
    /* Links */
    a {
        color: #3498db;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: #2980b9;
        text-decoration: underline;
    }
    
    /* Images and plots */
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 20px auto;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Math equations */
    .MathJax {
        font-size: 1.1em;
    }
    
    /* Page breaks for PDF */
    @media print {
        h1, h2 {
            page-break-after: avoid;
        }
        
        pre, blockquote, table {
            page-break-inside: avoid;
        }
        
        .jp-Cell {
            page-break-inside: avoid;
        }
    }
    
    /* Header banner */
    .header-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .header-banner h1 {
        color: white;
        border: none;
        margin: 0;
        font-size: 2.5em;
    }
    
    .header-banner p {
        margin: 10px 0 0 0;
        font-size: 1.1em;
        opacity: 0.9;
    }
    
    /* Metadata footer */
    .metadata-footer {
        margin-top: 40px;
        padding: 20px;
        background-color: #ecf0f1;
        border-radius: 8px;
        font-size: 0.9em;
        color: #7f8c8d;
    }
    
    /* Success/Info/Warning boxes */
    .alert-success {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
        color: #155724;
    }
    
    .alert-info {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
        color: #0c5460;
    }
    
    .alert-warning {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
        color: #856404;
    }
    
    /* Statistical highlights */
    .stat-box {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Cell spacing */
    .jp-Cell {
        margin-bottom: 20px;
    }
</style>
{%- endblock html_head -%}

{%- block body_header -%}
<div class="header-banner">
    <h1>Business Analytics Assignment A1</h1>
    <p>GDP per Capita, CO₂ Emissions, and Net-Zero Targets Analysis</p>
    <p style="font-size: 0.9em; margin-top: 15px;">
        <strong>Student:</strong> Kartavya Jharwal | 
        <strong>Course:</strong> BAN-0200 | 
        <strong>Institution:</strong> Hult International Business School
    </p>
</div>
{%- endblock body_header -%}

{%- block body_footer -%}
<div class="metadata-footer">
    <p><strong>Generated:</strong> {{ resources.metadata.get('date', 'N/A') }}</p>
    <p><strong>Notebook:</strong> assignment.ipynb</p>
    <p><strong>Export Format:</strong> HTML/PDF via nbconvert</p>
    <p style="margin-top: 10px; font-size: 0.85em;">
        Data sources: World Bank, Our World in Data, Net Zero Tracker<br>
        Statistical analysis performed using Python (pandas, numpy, scipy, matplotlib, seaborn)
    </p>
</div>
{%- endblock body_footer -%}
