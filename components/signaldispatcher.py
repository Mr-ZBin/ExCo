# -*- coding: utf-8 -*-

"""
Copyright (c) 2013-2023 Matic Kukovec. 
Released under the GNU GPL3 license.

For more information check the 'LICENSE.txt' file.
For complete license information of the dependencies, check the 'additional_licenses' directory.
"""

import qt
import data


class GlobalSignalDispatcher(qt.QObject):
    '''
    Global signal dispatcher
    '''
    update_title = qt.pyqtSignal()

    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)