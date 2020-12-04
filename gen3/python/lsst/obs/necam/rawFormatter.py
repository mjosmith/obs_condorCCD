from lsst.obs.base import FitsRawFormatterBase
from ._instrument import CondorCCD
from .necamFilters import CONDOR_FILTER_DEFINITIONS
# Comment-out the following line if you put .translators/necam.py in the 
# astro_metadata_translator repository: 
from .translators import CondorCCDTranslator
# ...and uncomment the following:
# from astro_metadata_translator import NeCamTranslator

class CondorCCDRawFormatter(FitsRawFormatterBase):
    """
    Gen3 Butler formatter for NeCam raw data.
    """
    translatorClass = CondorCCDTranslator
    filterDefinitions = CONDOR_FILTER_DEFINITIONS

    def getDetector(self, id):
        return CondorCCD().getCamera()[id]
