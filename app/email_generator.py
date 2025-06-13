from jinja2 import Template
import re

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        background-color: #f4f4f4;
        padding: 20px;
      }
      .email-container {
        max-width: 700px;
        margin: auto;
        background: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      }
      ul, ol {
        padding-left: 25px;
        margin: 15px 0;
      }
      li {
        margin-bottom: 8px;
        line-height: 1.5;
      }
      p {
        margin: 15px 0;
        line-height: 1.6;
      }
      .footer {
        margin-top: 40px;
        border-top: 2px solid #e2e8f0;
        padding-top: 20px;
        font-size: 14px;
        color: #718096;
        text-align: center;
      }
      .signature {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
      }
      .signature strong {
        color: #2d3748;
        font-size: 16px;
      }
      .company {
        color: #667eea;
        font-weight: 600;
      }
    </style>
  </head>
  <body>
    <div class="email-container">
      <p>Hi {{ name }},</p>

      <div>{{ body | safe }}</div>

      <div class="signature">
        <p>Best regards,</p>
        <p><strong>Dave Chatpar</strong><br><span class="company">NetWit.ca</span></p>
      </div>

      <div class="footer">
        <p>This message was sent to {{ name }} via NetWit Email Assistant.</p>
      </div>
    </div>
  </body>
</html>
"""

def render_email(name, domain, body):
    template = Template(HTML_TEMPLATE)
    return template.render(name=name, domain=domain, body=body)

def format_llm_output(llm_text):
    """
    Enhanced formatting function that handles multiple list types and better text processing
    """
    # Clean up the text first
    llm_text = llm_text.strip()
    
    # Handle numbered lists (1. 2. 3. etc.)
    numbered_pattern = r'^\s*(\d+)\.\s+(.+)$'
    numbered_matches = re.findall(numbered_pattern, llm_text, re.MULTILINE)
    
    if numbered_matches:
        # Create ordered list
        ol_items = ''.join(f"<li>{item.strip()}</li>" for _, item in numbered_matches)
        ol = f"<ol>{ol_items}</ol>"
        
        # Remove the numbered items from original text
        llm_text = re.sub(numbered_pattern, '', llm_text, flags=re.MULTILINE)
        
        # Split text and insert the list where appropriate
        parts = re.split(r'\n\s*\n', llm_text.strip())
        formatted_parts = []
        list_inserted = False
        
        for part in parts:
            part = part.strip()
            if part:
                formatted_parts.append(f"<p>{part}</p>")
                # Insert list after the first substantial paragraph
                if not list_inserted and len(part) > 50:
                    formatted_parts.append(ol)
                    list_inserted = True
        
        if not list_inserted:
            formatted_parts.append(ol)
            
        return ''.join(formatted_parts)
    
    # Handle bullet points (* or - bullets)
    bullet_pattern = r'^\s*[*-]\s+(.+)$'
    bullet_matches = re.findall(bullet_pattern, llm_text, re.MULTILINE)
    
    if bullet_matches:
        # Create unordered list
        ul_items = ''.join(f"<li>{item.strip()}</li>" for item in bullet_matches)
        ul = f"<ul>{ul_items}</ul>"
        
        # Remove the bullet items from original text
        llm_text = re.sub(bullet_pattern, '', llm_text, flags=re.MULTILINE)
        
        # Split text and insert the list where appropriate
        parts = re.split(r'\n\s*\n', llm_text.strip())
        formatted_parts = []
        list_inserted = False
        
        for part in parts:
            part = part.strip()
            if part:
                formatted_parts.append(f"<p>{part}</p>")
                # Insert list after the first substantial paragraph
                if not list_inserted and len(part) > 50:
                    formatted_parts.append(ul)
                    list_inserted = True
        
        if not list_inserted:
            formatted_parts.append(ul)
            
        return ''.join(formatted_parts)
    
    # No lists found, just convert to paragraphs
    paragraphs = re.split(r'\n\s*\n', llm_text)
    html_paragraphs = ''.join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())
    return html_paragraphs