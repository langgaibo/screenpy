"""
An action to refresh the browser page. An actor must possess the ability to
BrowseTheWeb to perform this action. An actor performs this action like so:

    the_actor.attempts_to(RefreshPage())
"""


from ..abilities import BrowseTheWeb
from ..actor import Actor
from .base_action import BaseAction


class RefreshPage(BaseAction):
    """
    Refreshes the browser page! A RefreshPage action is expected to be
    instantiated on its own. A typical invocation looks like:

        RefreshPage()

    It can then be passed along to the |Actor| to perform the action.
    """

    def perform_as(self, the_actor: Actor) -> None:
        """
        Asks the actor to refresh the page.

        Args:
            the_actor: the |Actor| who will perform this action.

        Raises:
            |UnableToPerform|: the actor does not have the ability to
                |BrowseTheWeb|.
        """
        browser = the_actor.ability_to(BrowseTheWeb).browser
        browser.refresh()
