"""
Matches a value that falls within the range specified by the given delta.
"""

from hamcrest import close_to

from .base_resolution import BaseResolution


class IsCloseTo(BaseResolution):
    """Matches a value that falls within the range specified by the given delta.

    Examples::

        the_actor.should(
            See.the(Element(MONEY_COUNT), IsCloseTo(MONEY_PREDICTED_COUNT, delta=25))
        )
    """

    line = "a value close to {expectation}."
    matcher_function = close_to
