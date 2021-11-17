# KtimaStatusEmail
Sends a notification email about the status of the Greek Cadastre in a specific area.

We use requests and BeautifulSoup libraries to get the information we need from the official Greek Cadastre website. The smtplib library handles the sending of the email.

One should first find the exact url of the area he's interested in. In the example the area of interest is ΕΡΕΤΡΙΑ ΕΥΒΟΙΑΣ.
We then get three components from the website. Perfecture, Ota-Name and the Status. We use the first two elements in the subject of the email and the third in the body.

We use gmail as the sender email provider.

Google is not allowing us to log in via smtplib because it has flagged this sort of login as "less secure", so what we have to do is go to this link while we're logged in to our google account, and allow the access: https://www.google.com/settings/security/lesssecureapps

Once that is set, it should work.

We can create a batch file that runs every week or daily via Task Scheduler on Windows, so that we always stay tuned about the status. Of course we could easily send this email to multiple emails, enrich the body of the email with other information etc.
