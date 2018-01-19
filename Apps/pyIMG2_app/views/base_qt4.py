# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.h_layout_central = QtGui.QHBoxLayout()
        self.h_layout_central.setContentsMargins(0, -1, 0, -1)
        self.h_layout_central.setObjectName(_fromUtf8("h_layout_central"))
        self.v_layou_options = QtGui.QVBoxLayout()
        self.v_layou_options.setObjectName(_fromUtf8("v_layou_options"))
        self.tabs_options = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_options.sizePolicy().hasHeightForWidth())
        self.tabs_options.setSizePolicy(sizePolicy)
        self.tabs_options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabs_options.setObjectName(_fromUtf8("tabs_options"))
        self.tab_filters = QtGui.QWidget()
        self.tab_filters.setObjectName(_fromUtf8("tab_filters"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_filters)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.v_layout_noise = QtGui.QVBoxLayout()
        self.v_layout_noise.setObjectName(_fromUtf8("v_layout_noise"))
        self.lbl_noise = QtGui.QLabel(self.tab_filters)
        self.lbl_noise.setObjectName(_fromUtf8("lbl_noise"))
        self.v_layout_noise.addWidget(self.lbl_noise)
        self.cb_noise = QtGui.QComboBox(self.tab_filters)
        self.cb_noise.setObjectName(_fromUtf8("cb_noise"))
        self.v_layout_noise.addWidget(self.cb_noise)
        self.lbl_noise_amount = QtGui.QLabel(self.tab_filters)
        self.lbl_noise_amount.setObjectName(_fromUtf8("lbl_noise_amount"))
        self.v_layout_noise.addWidget(self.lbl_noise_amount)
        self.sl_noise_amount = QtGui.QSlider(self.tab_filters)
        self.sl_noise_amount.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sl_noise_amount.setOrientation(QtCore.Qt.Horizontal)
        self.sl_noise_amount.setObjectName(_fromUtf8("sl_noise_amount"))
        self.v_layout_noise.addWidget(self.sl_noise_amount)
        self.lbl_noise_params = QtGui.QLabel(self.tab_filters)
        self.lbl_noise_params.setObjectName(_fromUtf8("lbl_noise_params"))
        self.v_layout_noise.addWidget(self.lbl_noise_params)
        self.edit_noise_params = QtGui.QLineEdit(self.tab_filters)
        self.edit_noise_params.setObjectName(_fromUtf8("edit_noise_params"))
        self.v_layout_noise.addWidget(self.edit_noise_params)
        self.btn_insert_noise = QtGui.QPushButton(self.tab_filters)
        self.btn_insert_noise.setObjectName(_fromUtf8("btn_insert_noise"))
        self.v_layout_noise.addWidget(self.btn_insert_noise)
        self.horizontalLayout_3.addLayout(self.v_layout_noise)
        self.v_layout_filter = QtGui.QVBoxLayout()
        self.v_layout_filter.setContentsMargins(0, -1, -1, -1)
        self.v_layout_filter.setObjectName(_fromUtf8("v_layout_filter"))
        self.lbl_filter = QtGui.QLabel(self.tab_filters)
        self.lbl_filter.setObjectName(_fromUtf8("lbl_filter"))
        self.v_layout_filter.addWidget(self.lbl_filter)
        self.cb_filter = QtGui.QComboBox(self.tab_filters)
        self.cb_filter.setObjectName(_fromUtf8("cb_filter"))
        self.v_layout_filter.addWidget(self.cb_filter)
        self.lbl_filter_size = QtGui.QLabel(self.tab_filters)
        self.lbl_filter_size.setObjectName(_fromUtf8("lbl_filter_size"))
        self.v_layout_filter.addWidget(self.lbl_filter_size)
        self.sl_filter_size = QtGui.QSlider(self.tab_filters)
        self.sl_filter_size.setOrientation(QtCore.Qt.Horizontal)
        self.sl_filter_size.setObjectName(_fromUtf8("sl_filter_size"))
        self.v_layout_filter.addWidget(self.sl_filter_size)
        self.lbl_filter_params = QtGui.QLabel(self.tab_filters)
        self.lbl_filter_params.setObjectName(_fromUtf8("lbl_filter_params"))
        self.v_layout_filter.addWidget(self.lbl_filter_params)
        self.edit_filter_params = QtGui.QLineEdit(self.tab_filters)
        self.edit_filter_params.setObjectName(_fromUtf8("edit_filter_params"))
        self.v_layout_filter.addWidget(self.edit_filter_params)
        self.btn_insert_filter = QtGui.QPushButton(self.tab_filters)
        self.btn_insert_filter.setObjectName(_fromUtf8("btn_insert_filter"))
        self.v_layout_filter.addWidget(self.btn_insert_filter)
        self.horizontalLayout_3.addLayout(self.v_layout_filter)
        self.tabs_options.addTab(self.tab_filters, _fromUtf8(""))
        self.tab_segmentations = QtGui.QWidget()
        self.tab_segmentations.setObjectName(_fromUtf8("tab_segmentations"))
        self.tabs_options.addTab(self.tab_segmentations, _fromUtf8(""))
        self.v_layou_options.addWidget(self.tabs_options)
        self.h_layout_options = QtGui.QHBoxLayout()
        self.h_layout_options.setObjectName(_fromUtf8("h_layout_options"))
        self.btn_equalize = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equalize.sizePolicy().hasHeightForWidth())
        self.btn_equalize.setSizePolicy(sizePolicy)
        self.btn_equalize.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_equalize.setFlat(False)
        self.btn_equalize.setObjectName(_fromUtf8("btn_equalize"))
        self.h_layout_options.addWidget(self.btn_equalize)
        self.radio_compare = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_compare.sizePolicy().hasHeightForWidth())
        self.radio_compare.setSizePolicy(sizePolicy)
        self.radio_compare.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.radio_compare.setAutoExclusive(False)
        self.radio_compare.setObjectName(_fromUtf8("radio_compare"))
        self.h_layout_options.addWidget(self.radio_compare)
        self.radio_hist = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_hist.sizePolicy().hasHeightForWidth())
        self.radio_hist.setSizePolicy(sizePolicy)
        self.radio_hist.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.radio_hist.setChecked(True)
        self.radio_hist.setAutoExclusive(False)
        self.radio_hist.setObjectName(_fromUtf8("radio_hist"))
        self.h_layout_options.addWidget(self.radio_hist)
        self.v_layou_options.addLayout(self.h_layout_options)
        self.h_layout_original_image = QtGui.QHBoxLayout()
        self.h_layout_original_image.setObjectName(_fromUtf8("h_layout_original_image"))
        self.replace_original_image = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_original_image.sizePolicy().hasHeightForWidth())
        self.replace_original_image.setSizePolicy(sizePolicy)
        self.replace_original_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.replace_original_image.setObjectName(_fromUtf8("replace_original_image"))
        self.h_layout_original_image.addWidget(self.replace_original_image)
        self.v_layou_options.addLayout(self.h_layout_original_image)
        self.h_layout_central.addLayout(self.v_layou_options)
        self.v_layout_edited_image = QtGui.QVBoxLayout()
        self.v_layout_edited_image.setContentsMargins(0, -1, -1, -1)
        self.v_layout_edited_image.setObjectName(_fromUtf8("v_layout_edited_image"))
        self.replace_edited_image = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace_edited_image.sizePolicy().hasHeightForWidth())
        self.replace_edited_image.setSizePolicy(sizePolicy)
        self.replace_edited_image.setObjectName(_fromUtf8("replace_edited_image"))
        self.v_layout_edited_image.addWidget(self.replace_edited_image)
        self.h_layout_central.addLayout(self.v_layout_edited_image)
        self.verticalLayout.addLayout(self.h_layout_central)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_fixed_status = QtGui.QLabel(self.centralwidget)
        self.lbl_fixed_status.setObjectName(_fromUtf8("lbl_fixed_status"))
        self.horizontalLayout.addWidget(self.lbl_fixed_status)
        self.lbl_status_msg = QtGui.QLabel(self.centralwidget)
        self.lbl_status_msg.setObjectName(_fromUtf8("lbl_status_msg"))
        self.horizontalLayout.addWidget(self.lbl_status_msg)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtGui.QAction(MainWindow)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionReset)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs_options.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Medical Images App", None))
        self.lbl_noise.setText(_translate("MainWindow", "Ruído:", None))
        self.lbl_noise_amount.setText(_translate("MainWindow", "Quantidade:", None))
        self.lbl_noise_params.setText(_translate("MainWindow", "Parâmetros:", None))
        self.btn_insert_noise.setText(_translate("MainWindow", "Inserir", None))
        self.lbl_filter.setText(_translate("MainWindow", "Filtro:", None))
        self.lbl_filter_size.setText(_translate("MainWindow", "Size:", None))
        self.lbl_filter_params.setText(_translate("MainWindow", "Parâmetros:", None))
        self.btn_insert_filter.setText(_translate("MainWindow", "Inserir", None))
        self.tabs_options.setTabText(self.tabs_options.indexOf(self.tab_filters), _translate("MainWindow", "Filtros", None))
        self.tabs_options.setTabText(self.tabs_options.indexOf(self.tab_segmentations), _translate("MainWindow", "Segmentação", None))
        self.btn_equalize.setText(_translate("MainWindow", "Equalizar", None))
        self.radio_compare.setText(_translate("MainWindow", "Comparar", None))
        self.radio_hist.setText(_translate("MainWindow", "Histograma", None))
        self.replace_original_image.setText(_translate("MainWindow", "Original Image", None))
        self.replace_edited_image.setText(_translate("MainWindow", "Edited Image", None))
        self.lbl_fixed_status.setText(_translate("MainWindow", "Status:", None))
        self.lbl_status_msg.setText(_translate("MainWindow", "Iniciado.", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre", None))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))

