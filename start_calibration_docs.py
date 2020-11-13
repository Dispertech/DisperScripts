import logging
# import os
# import sys
# from time import sleep

#
# if __name__ == "__main__":
#     os.environ.setdefault("EXPERIMENTOR_SETTINGS_MODULE", "calibration_settings")
#
#     this_dir = os.path.abspath(os.path.dirname(__file__))
#     sys.path.append(this_dir)
#
#     from experimentor.core.app import ExperimentApp
#
#     app = ExperimentApp(gui=True, logger=logging.INFO)
#
#     while app.is_running:
#         sleep(1)
#     app.finalize()
import sys
import time

import yaml
from PyQt5.QtWidgets import QApplication

from calibration.models.experiment import CalibrationSetup
from calibration.view.fiber_window import FiberWindow
from calibration.view.microscope_window import MicroscopeWindow
from calibration.view.testing_docks import MainWindow
from experimentor.lib.log import log_to_screen, get_logger

if __name__ == "__main__":
    logger = get_logger()
    handler = log_to_screen(logger=logger)
    experiment = CalibrationSetup()
    experiment.load_configuration('dispertech.yml', yaml.UnsafeLoader)
    executor = experiment.initialize()
    while executor.running():
        time.sleep(.1)

    app = QApplication([])
    mw = MainWindow(experiment=experiment, parent=None)
    mw.show()
    app.exec()
    experiment.finalize()
    sys.exit()
