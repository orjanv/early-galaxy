# Early Galaxy
Simple command-line tool for posting to Blogger. This script was written to enable posting to a blogger.com blog from the command line automatically. It is really a part of an earlier project which stopped working due to Google pulled the support for OAuth1.0 and the googlecl tool stopped working. To my suprise, no one has rewritten that tool as of March 2016 and therefore the need for this specific script. 

# Requirements
You will need to install the google-api using pip:

```bash
$ pip install --upgrade google-api-python-client
```

# Blogger API v3
The Blogger API v3 allows client applications to view and update Blogger content. Your client application can use Blogger API v3 to create new blog posts, edit or delete existing posts, and query for posts that match particular criteria.

To use this script with the Blogger API v3, you need to a generate OAuth 2.0 client ID. Refer to the API documentation for details. 

# Get started

Follow these steps to get up and running with the script.

1. Go to: https://console.developers.google.com/apis/credentials?project=_
2. Create a new project

![](assets/blogger-1.png =550x)

3. Enable Blogger API

![](assets/blogger-2.png =550x)
![](assets/blogger-3.png =550x)

4. Create credentials (OAuth client ID)

![](assets/blogger-4.png =550x)
![](assets/blogger-5.png =550x)
![](assets/blogger-6.png =550x)
![](assets/blogger-7.png =550x)
![](assets/blogger-8.png =550x)
![](assets/blogger-9.png =550x)

5. Download JSON and save as client_secrets.json in the same folder as the script

![](assets/blogger-10.png =550x)

If you want, you can format the JSON code using: http://www.jsoneditoronline.org

![](assets/blogger-11.png =550x)
![](assets/blogger-12.png =550x)

# Usage

To use the script, you need to run the script with a couple of arguments:

```bash
 --title "Your blog post title"
 --src <file containing your blogpost written in html>
```

an optional argument can be used

```bash
 --label "labels, separated, by, comma" 
```

# Example

```bash
$ python blogger.py --title "Five nice haiku poems" --labels "haiku" --src haiku.html 
``` 

Enjoy posting from the command line.

