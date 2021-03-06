from lsst.obs.base.ingest import RawFileData
import lsst.obs.base
from ._instrument import CondorCCD

class CondorCCDRawIngestTask(lsst.obs.base.RawIngestTask):

    def extractMetadata(self, filename: str) -> RawFileData:

        datasets = []   
        fitsData = lsst.afw.fits.Fits(filename, 'r')
        header = fitsData.readMetadata()
        datasets.append(self._calculate_dataset_info(header, filename))

        instrument = CondorCCD()
        FormatterClass = instrument.getRawFormatter(datasets[0].dataId)

        return RawFileData(datasets=datasets, filename=filename,
                           FormatterClass=FormatterClass,
                           instrumentClass=type(instrument)) 
                
