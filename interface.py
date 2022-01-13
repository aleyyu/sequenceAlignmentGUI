from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QFileInfo
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pyqtgraph import PlotWidget
import kmer_algorithm
import fm_index_algorithm
import pyqtgraph as pg
import icons_rc
from pathlib import Path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1667, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-image: url(:/backgrounds/bckg_son_1690x750.jpg);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lyt_sol = QtWidgets.QVBoxLayout()
        self.lyt_sol.setObjectName("lyt_sol")
        self.lyt_input = QtWidgets.QVBoxLayout()
        self.lyt_input.setObjectName("lyt_input")
        self.lyt_txt = QtWidgets.QHBoxLayout()
        self.lyt_txt.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.lyt_txt.setObjectName("lyt_txt")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lyt_txt.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.btn_upload_txt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upload_txt.sizePolicy().hasHeightForWidth())
        self.btn_upload_txt.setSizePolicy(sizePolicy)
        self.btn_upload_txt.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_upload_txt.setFont(font)
        self.btn_upload_txt.setStyleSheet("background-color: rgb(248, 169, 120);\n"
"color: rgb(1, 1, 1);")
        self.btn_upload_txt.setObjectName("btn_upload_txt")
        self.verticalLayout_4.addWidget(self.btn_upload_txt)
        self.btn_upload_txt.clicked.connect(self.load_txt)

        self.lbl_txt = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_txt.sizePolicy().hasHeightForWidth())
        self.lbl_txt.setSizePolicy(sizePolicy)
        self.lbl_txt.setText("")
        self.lbl_txt.setObjectName("lbl_txt")
        self.verticalLayout_4.addWidget(self.lbl_txt)
        self.lyt_txt.addLayout(self.verticalLayout_4)
        self.lyt_input.addLayout(self.lyt_txt)
        self.lyt_ptrn = QtWidgets.QHBoxLayout()
        self.lyt_ptrn.setObjectName("lyt_ptrn")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.lyt_ptrn.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.btn_upload_ptrn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upload_ptrn.sizePolicy().hasHeightForWidth())
        self.btn_upload_ptrn.setSizePolicy(sizePolicy)
        self.btn_upload_ptrn.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_upload_ptrn.setFont(font)
        self.btn_upload_ptrn.setStyleSheet("background-color: rgb(248, 169, 120);\n"
"color: rgb(1, 1, 1);")
        self.btn_upload_ptrn.setObjectName("btn_upload_ptrn")
        self.verticalLayout_6.addWidget(self.btn_upload_ptrn)
        self.btn_upload_ptrn.clicked.connect(self.load_ptrn)

        self.lbl_ptrn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ptrn.sizePolicy().hasHeightForWidth())
        self.lbl_ptrn.setSizePolicy(sizePolicy)
        self.lbl_ptrn.setText("")
        self.lbl_ptrn.setObjectName("lbl_ptrn")
        self.verticalLayout_6.addWidget(self.lbl_ptrn)
        self.lyt_ptrn.addLayout(self.verticalLayout_6)
        self.lyt_input.addLayout(self.lyt_ptrn)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_search.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("background-color: rgb(248, 169, 120);\n"
"color: rgb(1, 1, 1);")
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_3.addWidget(self.btn_search, 0, 0, 1, 1)
        self.btn_search.clicked.connect(self.btn_alignment)
        #self.btn_search = Button(command= self.cut)

        self.lyt_input.addLayout(self.gridLayout_3)
        self.lyt_input_kmer = QtWidgets.QHBoxLayout()
        self.lyt_input_kmer.setObjectName("lyt_input_kmer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lyt_input_kmer.addLayout(self.verticalLayout_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.input_k_value = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_k_value.sizePolicy().hasHeightForWidth())
        self.input_k_value.setSizePolicy(sizePolicy)
        self.input_k_value.setMaximumSize(QtCore.QSize(200, 30))
        self.input_k_value.setStyleSheet("background-color: rgb(221,255,221);")
        self.input_k_value.setObjectName("input_k_value")
        self.gridLayout_5.addWidget(self.input_k_value, 0, 0, 1, 1)
        self.lyt_input_kmer.addLayout(self.gridLayout_5)
        self.lyt_input.addLayout(self.lyt_input_kmer)
        self.lyt_btn_kmer = QtWidgets.QHBoxLayout()
        self.lyt_btn_kmer.setObjectName("lyt_btn_kmer")

        self.btn_calc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy)
        self.btn_calc.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_calc.setFont(font)
        self.btn_calc.setStyleSheet("background-color: rgb(248, 169, 120);\n"
"color: rgb(1, 1, 1);")
        self.btn_calc.setObjectName("btn_calc")
        self.lyt_btn_kmer.addWidget(self.btn_calc)
        self.btn_calc.clicked.connect(self.btn_kmer)
        self.btn_calc.clicked.connect(self.kmer_freq_top)
        self.btn_calc.clicked.connect(self.calc_kmer)
        self.btn_calc.clicked.connect(lambda:self.draw_graph_1())
        self.btn_calc.clicked.connect(lambda:self.draw_graph_2())
        self.btn_calc.clicked.connect(lambda:self.draw_graph_3())

        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(248, 169, 120);\n""color: rgb(1, 1, 1);")
        self.btn_clear.setObjectName("btn_clear")
        self.lyt_btn_kmer.addWidget(self.btn_clear)
        self.btn_clear.clicked.connect(self.clear)

        self.lyt_input.addLayout(self.lyt_btn_kmer)
        self.lyt_sol.addLayout(self.lyt_input)
        self.lyt_otpt_alignment = QtWidgets.QGridLayout()
        self.lyt_otpt_alignment.setObjectName("lyt_otpt_alignment")

        self.txt_align_output = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_align_output.sizePolicy().hasHeightForWidth())
        self.txt_align_output.setSizePolicy(sizePolicy)
        self.txt_align_output.setStyleSheet("background-image: url(:/backgrounds/back2.jpg);")
        self.txt_align_output.setObjectName("txt_align_output")
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(15)
        font.setBold(True)
        self.txt_align_output.setFont(font)
        #font.setWeight(75)
        #self.txt_align_output.setFont(QFont('Garamond', 15))
        #self.txt_align_output.setBold(True)
        self.lyt_otpt_alignment.addWidget(self.txt_align_output, 0, 0, 1, 1)

        self.lyt_sol.addLayout(self.lyt_otpt_alignment)
        self.horizontalLayout.addLayout(self.lyt_sol)
        self.lyt_sag = QtWidgets.QVBoxLayout()
        self.lyt_sag.setObjectName("lyt_sag")
        self.lyt_output_kmer = QtWidgets.QHBoxLayout()
        self.lyt_output_kmer.setObjectName("lyt_output_kmer")
        self.lyt_otpt_kmer = QtWidgets.QVBoxLayout()
        self.lyt_otpt_kmer.setObjectName("lyt_otpt_kmer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lyt_otpt_kmer.addWidget(self.label)

        self.txt_kmer_freq = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_kmer_freq.sizePolicy().hasHeightForWidth())
        self.txt_kmer_freq.setSizePolicy(sizePolicy)
        self.txt_kmer_freq.setStyleSheet("background-image: url(:/backgrounds/back1.jpg);")
        self.txt_kmer_freq.setObjectName("txt_kmer_freq")
        self.txt_kmer_freq.verticalScrollBar().setDisabled(False)
        self.txt_kmer_freq.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lyt_otpt_kmer.addWidget(self.txt_kmer_freq)


        self.lyt_output_kmer.addLayout(self.lyt_otpt_kmer)
        self.lyt_kmer_top = QtWidgets.QVBoxLayout()
        self.lyt_kmer_top.setObjectName("lyt_kmer_top")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lyt_kmer_top.addWidget(self.label_5)
        self.txt_kmer_top = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_kmer_top.sizePolicy().hasHeightForWidth())
        self.txt_kmer_top.setSizePolicy(sizePolicy)
        self.txt_kmer_top.setStyleSheet("background-image: url(:/backgrounds/back1.jpg);")
        self.txt_kmer_top.setObjectName("txt_kmer_top")
        self.lyt_kmer_top.addWidget(self.txt_kmer_top)
        self.lyt_output_kmer.addLayout(self.lyt_kmer_top)
        self.lyt_sag.addLayout(self.lyt_output_kmer)
        self.lyt_graph = QtWidgets.QHBoxLayout()
        self.lyt_graph.setObjectName("lyt_graph")
        self.lyt_graph3 = QtWidgets.QVBoxLayout()
        self.lyt_graph3.setObjectName("lyt_graph3")

        self.graph_1 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_1.sizePolicy().hasHeightForWidth())
        self.graph_1.setSizePolicy(sizePolicy)
        self.graph_1.setStyleSheet("background-color: rgb(221,255,221);")
        self.graph_1.setObjectName("graph_1")
        self.lyt_graph3.addWidget(self.graph_1)
        self.graph_1.setBackground('w')

        self.lyt_graph.addLayout(self.lyt_graph3)
        self.lyt_graph1 = QtWidgets.QVBoxLayout()
        self.lyt_graph1.setObjectName("lyt_graph1")

        self.graph_2 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_2.sizePolicy().hasHeightForWidth())
        self.graph_2.setSizePolicy(sizePolicy)
        self.graph_2.setStyleSheet("background-color: rgb(221,255,221);")
        self.graph_2.setObjectName("graph_2")
        self.lyt_graph1.addWidget(self.graph_2)
        self.graph_2.setBackground('w')

        self.lyt_graph.addLayout(self.lyt_graph1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.graph_3 = PlotWidget(self.centralwidget)
        self.graph_3.setStyleSheet("background-color: rgb(221,255,221);")
        self.graph_3.setObjectName("graph_3")
        self.verticalLayout_5.addWidget(self.graph_3)
        self.graph_3.setBackground('w')

        self.lyt_graph.addLayout(self.verticalLayout_5)
        self.lyt_sag.addLayout(self.lyt_graph)
        self.horizontalLayout.addLayout(self.lyt_sag)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1667, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence Alignment GUI"))
        self.label_6.setText(_translate("MainWindow", "Select FATSA File for Text Sequence"))
        self.btn_upload_txt.setText(_translate("MainWindow", "UPLOAD FILE"))
        self.label_7.setText(_translate("MainWindow", "Select FATSA File for Pattern Sequence"))
        self.btn_upload_ptrn.setText(_translate("MainWindow", "UPLOAD FILE"))
        self.btn_search.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_search.setText(_translate("MainWindow", "SEARCH WITH FM-INDEX"))
        self.label_8.setText(_translate("MainWindow", "Enter K Value for K-mer Calculation"))
        self.btn_calc.setText(_translate("MainWindow", "CALCULATE K-MER"))
        self.btn_clear.setText(_translate("MainWindow", "CLEAN"))
        self.label.setText(_translate("MainWindow", "K-MER FREQUENCE RESULTS"))
        self.label_5.setText(_translate("MainWindow", "K-MER TOP 5 FREQUENCE "))

    txt = ""
    ptrn = ""
    sonuc = []
    k = 0
    f_name_txt = ""
    f_name_ptrn = ""


    """
    def show_alignment(self):
        print(self.sonuc)
        goster = self.sonuc
        #self.textBrowser_3.setPlainText(self.sonuc)
        for i in goster:
            self.textBrowser_3.append(i)
    """

    def clear(self):
        self.txt_align_output.clear()
        self.txt_kmer_top.clear()
        self.txt_kmer_freq.clear()
        self.graph_1.clear()
        self.graph_2.clear()
        self.graph_3.clear()


    # ALIGNMENT
    def btn_alignment(self):
        t = self.txt
        p = self.ptrn
        count = 0
        output = []
        run_time = 0.0

        if self.f_name_txt == "":
            QMessageBox.about(MainWindow, "ERROR", "No FATSA file for text sequence selected. Please select one.")
            QMessageBox.show()

        elif self.f_name_ptrn == "":
            QMessageBox.about(MainWindow, "ERROR", "No FATSA file for pattern sequence selected. Please select one.")
            QMessageBox.show()
        else:
            result = fm_index_algorithm.align(t, p)
            output = result[0]
            run_time = result[1]
            #print(result)

            self.txt_align_output.setText("The start position of pattern sequence is: ")

            for i in output:
                # self.textBrowser_3.append("i: {}".format(i))
                self.txt_align_output.append("- {}".format(i))
                count += 1

            self.txt_align_output.append("\n-----------------------------------------------------------------------------------------------")
            self.txt_align_output.append("\n {} start position found".format(count))
            self.txt_align_output.append("\n-----------------------------------------------------------------------------------------------")
            self.txt_align_output.append("\n Run time is: {}".format(run_time))

        # runtime = fm_index_algorithm.run_time()
        # self.txt_align_output.setText(runtime)

        # print(output)
        # self.textBrowser_3.setPlainText(output)

    def load_txt(self):
        dialog = QFileDialog(directory = "D:\Masaüstü\FATSA files")
        dialog.setWindowTitle("Choose FATSA file for text sequence.")
        dialog.setNameFilter("FNA files (*.fna)")
        dialog.setFilter(QDir.Files)

        str_fname = ""

        if dialog.exec_():
            file_name = dialog.selectedFiles()
            self.f_name_txt = file_name

            if file_name[0].endswith('.fna'):
                with open(file_name[0], 'r') as f:
                    text = f.read()
                    self.txt = text
                    f.close()
            else:
                pass

        str_fname = str_fname.join(file_name)

        if file_name:
            fname = Path(str_fname)
            self.lbl_txt.setText("Selected file: {}".format(fname.name))
        else:
            self.lbl_txt.setText("No file is chosen. Please choose a file.")

            return text

    def load_ptrn(self):
        dialog = QFileDialog(directory = "D:\Masaüstü\FATSA files")
        dialog.setWindowTitle("Choose FATSA file for pattern sequence.")
        dialog.setNameFilter("FNA files (*.fna)")
        dialog.setFilter(QDir.Files)

        str_fname = ""

        if dialog.exec_():
            file_name = dialog.selectedFiles()
            self.f_name_ptrn = file_name

            if file_name[0].endswith('.fna'):
                with open(file_name[0], 'r') as f:
                    pattern = f.read()
                    self.ptrn = pattern
                    f.close()
            else:
                pass

        str_fname = str_fname.join(file_name)

        if file_name:
            fname = Path(str_fname)
            self.lbl_ptrn.setText("Selected file: {}".format(fname.name))
        else:
            self.lbl_ptrn.setText("No file was choosed. Please choose a file.")

            return pattern

    # KMER
    def btn_kmer(self):
        sequence = self.ptrn
        get_k = self.input_k_value.text()

        if self.f_name_ptrn == "":
            QMessageBox.about(MainWindow, "ERROR", "No FATSA file for pattern sequence selected. Please select one.")
            QMessageBox.show()

        elif get_k == "":
            QMessageBox.about(MainWindow, "ERROR", "K value for K-Mer algorithm can't be 0. Please enter a valid value.")
            QMessageBox.show()
        else:
            self.calc_kmer()
            self.kmer_freq_top()
            self.draw_graph_1()
            self.draw_graph_2()
            self.draw_graph_3()

    def calc_kmer(self):
        sequence = self.ptrn
        get_k = self.input_k_value.text()

        ksize = int(get_k)
        self.k = ksize
        kmers = kmer_algorithm.build_kmers(sequence, ksize)

        for kmer, freq in kmers.items():
            txt = "kmer: {} - freq: {}".format(kmer, freq)
            self.txt_kmer_freq.append(txt)
        verScrollBar = self.txt_kmer_freq.setVerticalScrollBar()
        verScrollBar.setValue(verScrollBar.minimum())

    def kmer_freq_top(self):

        sequence = self.ptrn
        get_k = self.input_k_value.text()
        ksize = int(get_k)
        self.k = ksize

        mc = kmer_algorithm.kmer_freq_top(sequence, ksize)
        """
        kmer_string = []
        kmer_freq = []
        kmer = {}

        for a, b in mostcommon:
            kmer_string.append(a)
            kmer_freq.append(b)
            kmer[a] = b
        """
        for kmer, freq in mc:
            txt = "kmer: {} - freq: {}".format(kmer, freq)
            self.txt_kmer_top.append("{}".format(txt))

    def draw_graph_1(self):
        sequence = self.ptrn
        get_k = self.input_k_value.text()
        ksize = int(get_k)
        self.k = ksize

        x = []
        y = []

        sonuc = kmer_algorithm.kmer_graph_1(sequence, ksize)
        x = sonuc[0]
        y = sonuc[1]

        pen = pg.mkPen(color=(255, 0, 0), width=1, style=QtCore.Qt.DotLine)
        styles = {'color': 'r', 'font-size': '15px'}
        self.graph_1.setLabel('left', '1/freq', **styles)
        self.graph_1.setLabel('bottom', 'freqs', **styles)
        self.graph_1.setTitle("K-Mer Period Graph",color="red", size="10pt")
        self.graph_1.plot(x, y, pen=pen)
        self.graph_1.updateMatrix()

    def draw_graph_2(self):
        sequence = self.ptrn
        get_k = self.input_k_value.text()
        ksize = int(get_k)
        self.k = ksize

        x = []
        y = []

        sonuc2 = kmer_algorithm.kmer_graph_2(sequence, ksize)
        x = sonuc2[0]
        y = sonuc2[1]

        #pen = pg.mkPen(color="blue", width=1, style=QtCore.Qt.SolidLine)
        styles = {'color': 'r', 'font-size': '15px'}
        self.graph_2.setLabel('left', 'freq', **styles)
        self.graph_2.setLabel('bottom', 'k-mer no', **styles)
        self.graph_2.setTitle("K-Mer Frequence Graph", color="b", size="10pt")
        #self.graph_2.plot(x, y,pen=pen, symbol='+', symbolSize=5, symbolBrush=('b'))
        self.graph_2.plot(x, y, pen=None, symbol='o')
        self.graph_2.updateMatrix()


    def draw_graph_3(self):
        sequence = self.ptrn
        get_k = self.input_k_value.text()
        ksize = int(get_k)
        self.k = ksize

        x = []
        y = []

        sonuc3 = kmer_algorithm.kmer_graph_3(sequence, ksize)
        x = sonuc3[0]
        y = sonuc3[1]

        #pen = pg.mkPen(color="white", width=1, style=QtCore.Qt.SolidLine)
        bargraph =pg.BarGraphItem(x=x, height=y, width=0.6, brush='g')
        styles = {'color': 'r', 'font-size': '15px'}
        self.graph_3.setLabel('left', 'freq', **styles)
        self.graph_3.setLabel('bottom', 'kmer no', **styles)
        self.graph_3.setTitle("Top 5 Frequence Graph", color="g", size="10pt")
        self.graph_3.plot(x,y)
        self.graph_3.addItem(bargraph)

        self.graph_3.updateMatrix()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



