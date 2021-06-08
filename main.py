from selenium import webdriver
from time import sleep
from secrets import pw

class InstaBot:
    # When an instance of InstaBot is created, both username and password are passed along
    # Set the driver to the browser driver: in this case "webdriver.Chrome()"
    # Set the username to a variable (for future use)
    # Call the browser to take you to the specified url : in this case instagram.com
    # Wait 4 seconds for the page to load before moving on to next step
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(4)
        # Maximize Browser Window
        self.driver.maximize_window()
        sleep(4)
        
        # On the login page, find the username element/field and pass the username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(2)
        # Find the password element/field and pass the pw
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        sleep(2)
        # Find the submit button and click
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(2)
        # Wait for home page to load completely
        sleep(6)
        # There's a notification pop-up just before the home page loads. This clicks the 'Not Now'
        # button to close the pop-up
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        # Wait some more
        sleep(6)

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()


    def get_unfollowers(self):
        # From the home page, find the 'a' tag element for user profile and click on it to load page
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        # Wait for page to load
        sleep(4)
        # Find the 'a' tag element that contains the text '/following' and click
        # This displays the list of user you follow
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
            .click()
        # Call the _get_names() private function/method to make a list of users you follow
        following = self._get_names()
        print("******************** Following ***************")
        print(following)
        # Find the 'a' tag  element that contains the text '/followers' and click
        # This displays the list of users following you
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\
            .click()
        # Call the _get_names() private function/method to make a list of users who follow you
        followers = self._get_names()
        print("********************** Followers *************")
        print(followers)
        # List comprehension to make a list of users in 'following' but not in 'followers'
        not_following_back = [user for user in following if user not in followers]
        # Print list to console
        print("********************** Not Following *********")
        print(not_following_back)

    def _get_names(self):
        # Wait for page to load
        sleep(2)
        # Find the pop-up by x-path and assign to scroll_box variable
        # Original code commented out on 05/25/2021 because it no longer works
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        # Updated on 05/25/2021 to using css selector to identify following list
        scroll_box = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP")
        last_ht, ht = 0, 1
        # Scroll to the bottom of the pop-up to allow all users to load completely
        while last_ht != ht:
            last_ht = ht
            sleep(4)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        # Each user is identified with an 'a' tag element in the pop up
        links = scroll_box.find_elements_by_tag_name('a')
        # List comprehension to make a list of users
        names = [name.text for name in links if name.text != '']
        # close button
        sleep(1)
        # Commenting out old 'close' selector as of (05/25/2021) - it no longer works
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
        #    .click()
        # New Close button (updated 05/25/2021)
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button")\
            .click()
        #Return list
        return names

    def log_out(self):
        # Find the Settings/gear-like button on the profile page and click
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')\
            .click()
        # From the pop-up list, find the 'Log Out' button and click
        # Old code no longer viable as of 05/25/2021
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[9]")\
        #    .click()
        # Updated Log Out button click (05/25/2021)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[9]')\
            .click()
        # Wait for 2 secs and then close browser window
        sleep(2)
        self.driver.close()
        

# Creating an instance of the InstaBot class (with username and pw passed as arguments)
my_bot = InstaBot('your_username', pw)
# Call the get_unfollowers() method on the my_bot instance
my_bot.get_unfollowers()
# Call the log_out() method on the my_bot instance to exit Instagram
my_bot.log_out()