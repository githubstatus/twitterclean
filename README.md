# Twitter Clean

Inspired from https://github.com/brunocassol/twitterwipe

Deletes your tweets, retweets and favorites.

# Usage
1. Make sure your have Python 3 installed by running this in console:

        python3 --version

2. Install required python library:
    
        pip3 install python-twitter
        pip3 install python-dotenv
    
3. Download twitterwipe script:

        git clone https://github.com/valentinourbano/twitterclean
        cd twitterclean
    
4. Create a temporary twitter app:

- Open https://apps.twitter.com
- Sign up with your account.
- Create a new app. The details can be bogus, your app will be private.
- Make sure the app has read/write permission and click `Regenerate My Access Token and Token Secret` button. **This step is easy to miss**.

5. Edit the downloaded twitterclean.py file:

- Open `twitterclean.py` with your favorite text editor

        code twitterclean.py

- Rename the file "envDefault" in ".env"

- Copy these values from your created Twitter app and paste into `KEY` placeholders in .env:

        consumer_key=KEY
        consumer_secret=KEY
        access_token_key=KEY
        access_token_secret=KEY

6. Configure:

        - REMOVE_TWEETS:

        Choose if you want to delete your tweets (doesn't delete retweets)

        - REMOVE_RETWEETS:

        Choose if you want to delete your retweets

        - REMOVE_FAVORITES:

        Choose if you want to delete your favorites

        - DRY_RUN: 

        It will run the script without actually deleting anything. Always run the script FIRST using "DRY_RUN = True" and take a look at what it would delete before actually running it.

7. Run the script:

        python3 twitterclean.py

# Credits
Based on: https://github.com/brunocassol/twitterwipe

## Techical note
Twitter implements rate limiting on its API so we need to pause execution for a few moments every once in a while.
