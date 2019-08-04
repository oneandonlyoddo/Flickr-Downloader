# A Flickr Image Downloader
In order to use this you will need to obtain an API key and secret from Flickr.

This can be done here: <https://www.flickr.com/services/apps/create/>.

Please keep in mind and respect the respective licenses for the images.

### Setup:

1. Obtain API keys from Flickr
2. Save the keys in a **keys.txt** next to the **flickrDownloader.py**. Key goes in the first line, secret in a new second line.
3. Run: **pip install -r requirements.txt** in your shell.



### Usage:

```bash
python flickrDownloader [search term] [max amount of images] [output folder]
```

e.g.:

```bash
python flickrDownloader "bird" 100 "./birds"
```

