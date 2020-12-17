from fontbakery.message import Message 
from fontbakery.callable import check
from fontbakery.checkrunner import (PASS, FAIL)
from fontbakery.fonts_profile import profile_factory

profile_imports = [
    ('fontbakery.profiles.shared_conditions', ('is_variable_font',))
]


@check(
    id='io.github.abysstypeco/check/ytlc_sanity',
    rationale="""
        This check follows the proposed values of the ytlc axis proposed by font bureau at the site url. add more later.
    """,
    conditions=["is_variable_font"]
)
def io_github_abysstypeco_check_ytlc_sanity(ttFont):
    """Check if ytlc values are sane in vf"""
    passed = True

    for axis in ttFont['fvar'].axes:
        if not axis.axisTag == 'ytlc': continue

        if axis.minValue < 0 or axis.maxValue > 1000:
            passed = False
            yield FAIL,\
                  Message("invalid-range",
                          f'The range of ytlc values ({axis.minValue} - {axis.maxValue})'
                          f'does not conform to the expected range of ytlc which should be min value 0 to max value 1000')
    if passed:
        yield PASS, 'ytlc is sane'


    
  