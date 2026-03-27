from .median_coffee import MedianCoffeeReport
from .avg_sleep import AvgSleepReport
from .avg_study import  AvgStudyReport
REPORTS = {
    MedianCoffeeReport.name: MedianCoffeeReport(),
    AvgSleepReport.name: AvgSleepReport(),
    AvgStudyReport.name: AvgStudyReport(),

}

