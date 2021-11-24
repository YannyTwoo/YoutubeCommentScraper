# YoutubeCommentScraper

Python code to scrape YouTube comments of a given URL via the Selenium library. The code was written to gather up data for some NLP exploration. Hope this helps you out in your projects too.


NOTE:
1. The code only scrapes initial comments, meaning the replies to a comment are not scraped(This code was written for an NLP project and thus is structured in this manner)
2. The CSV sheet exported would include special characters. As of the current iteration, the special characters aren't cleaned up

NOTE : After sharing this code I've been made aware that a better way to gather the data is to use the API provided by YouTube. The only drawback to it is that the API key you create must be run every 90 days or else YouTube will render it invalid.
