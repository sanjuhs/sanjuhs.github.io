Necro Knight — Web build (love.js)

Serve this folder with a real web server (opening index.html as a file:// URL won't work).

IMPORTANT: love.js needs Cross-Origin-Opener-Policy + Cross-Origin-Embedder-Policy headers.
- For Apache, this folder includes .htaccess.
- For other servers, configure:
  COOP: same-origin
  COEP: require-corp

Open:
  /index.html

Embed on your site:
  <iframe src="/path/to/builds/web/index.html" style="width:100%;height:720px;border:0"></iframe>


