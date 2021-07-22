from tethys_sdk.base import TethysAppBase, url_map_maker


class Vic(TethysAppBase):
    """
    Tethys app class for Vic.
    """

    name = 'Vic'
    index = 'vic:home'
    icon = 'vic/images/icon.gif'
    package = 'vic'
    root_url = 'vic'
    color = '#2c3e50'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='vic',
                controller='vic.controllers.home'
            ),
        )

        return url_maps