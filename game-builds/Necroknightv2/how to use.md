How to use
Android (install the APK):
Copy builds/android/necro-knight-debug.apk to your phone and install (enable “install unknown apps” if needed), or use adb install.
Web (embed on your website):
Upload the entire builds/web/ folder to your server and serve it (can’t be file://).
Then embed:

<iframe src="/path/to/builds/web/index.html" style="width:100%;height:720px;border:0"></iframe>
<iframe src="/path/to/builds/web/index.html" style="width:100%;height:720px;border:0"></iframe>
Note: the web folder includes .htaccess for the required COOP/COEP headers (Apache). If you use Nginx/Cloudflare/etc, you’ll need to set those headers there.
