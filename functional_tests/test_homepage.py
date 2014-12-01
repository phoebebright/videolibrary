from .base import FunctionalTest


class HomePageTest(FunctionalTest):

    def test_home_page_content(self):

        # Vince goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # He sees a table showing current list of videos
        vtable = self.get_video_list()
        self.assertEqual(vtable.tag_name, "table")

        # And a button to add more
        addbtn = self.getid('add_video')
        self.assertEqual(addbtn.tag_name, "a")

    def test_add_page(self):

        # From the home page Vince clicks the add button and it goes to the Add Video Page


        # Vince goes to the home page
        self.browser.get(self.server_url)
        addbtn = self.getid('add_video')


        addbtn.click()
        self.assertEquals(self.browser.title, "Add Video")

