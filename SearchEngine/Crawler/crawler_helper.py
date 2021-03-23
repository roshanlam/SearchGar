from urllib.parse import urljoin, urlparse 
    
def url_is_valid(link):
    if not link or any(i in link for i in ('.pdf', '.docx', '.py', '.java', '.exe')) \
        or link.startswith('mailto:') or ('#' in link):
        return False
    else: 
        return True
    