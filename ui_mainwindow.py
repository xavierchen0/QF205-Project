# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLineEdit, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)
import calc_functions
from datetime import date

class Ui_window(object):
    def _calculate(self):
        '''
        Using the provided inputs, calculate the option price.
        '''
        S = float(self.in_assetprice.text().strip())
        K = float(self.in_strikeprice.text().strip())
        r = float(self.in_strikeprice.text().strip()) / 100
        sigma = float(self.in_std.text().strip())
        M = int(self.in_pricestep.text().strip())
        N = int(self.in_timestep.text().strip())
        
        input_date = self.in_maturitydate.date().toPython()
        current_date = date.today()
        T = (input_date - current_date).days / 365

        return calc_functions.eurcall_explicit(S, K, r, sigma, T, M, N)

    def _displayresult(self):
        '''
        Display the option price after calculation.
        '''
        opPrice = self._calculate()
        self.output.setText(f"<center><b><font color='blue' size='20'>{opPrice}</font></b></center>")

    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.setEnabled(True)
        window.resize(600, 600)
        self.introduction = QTextBrowser(window)
        self.introduction.setObjectName(u"introduction")
        self.introduction.setGeometry(QRect(10, 10, 580, 80))
        self.text_option_type = QTextBrowser(window)
        self.text_option_type.setObjectName(u"text_option_type")
        self.text_option_type.setGeometry(QRect(10, 100, 275, 30))
        self.text_asset_price = QTextBrowser(window)
        self.text_asset_price.setObjectName(u"text_asset_price")
        self.text_asset_price.setGeometry(QRect(10, 140, 275, 30))
        self.text_strike_price = QTextBrowser(window)
        self.text_strike_price.setObjectName(u"text_strike_price")
        self.text_strike_price.setGeometry(QRect(10, 180, 275, 30))
        self.text_interest = QTextBrowser(window)
        self.text_interest.setObjectName(u"text_interest")
        self.text_interest.setGeometry(QRect(10, 220, 275, 30))
        self.text_volatility = QTextBrowser(window)
        self.text_volatility.setObjectName(u"text_volatility")
        self.text_volatility.setGeometry(QRect(10, 260, 275, 30))
        self.text_maturity_date = QTextBrowser(window)
        self.text_maturity_date.setObjectName(u"text_maturity_date")
        self.text_maturity_date.setGeometry(QRect(10, 300, 275, 30))
        self.text_price_step = QTextBrowser(window)
        self.text_price_step.setObjectName(u"text_price_step")
        self.text_price_step.setGeometry(QRect(10, 340, 275, 30))
        self.text_time_step = QTextBrowser(window)
        self.text_time_step.setObjectName(u"text_time_step")
        self.text_time_step.setGeometry(QRect(10, 380, 275, 30))
        self.text_time_step.setAutoFillBackground(False)
        self.in_option_type = QComboBox(window)
        self.in_option_type.addItem("")
        self.in_option_type.addItem("")
        self.in_option_type.setObjectName(u"in_option_type")
        self.in_option_type.setGeometry(QRect(315, 100, 275, 30))
        self.in_assetprice = QLineEdit(window)
        self.in_assetprice.setObjectName(u"in_assetprice")
        self.in_assetprice.setGeometry(QRect(315, 140, 275, 30))
        self.in_strikeprice = QLineEdit(window)
        self.in_strikeprice.setObjectName(u"in_strikeprice")
        self.in_strikeprice.setGeometry(QRect(315, 180, 275, 30))
        self.in_interestrate = QLineEdit(window)
        self.in_interestrate.setObjectName(u"in_interestrate")
        self.in_interestrate.setGeometry(QRect(315, 220, 275, 30))
        self.in_std = QLineEdit(window)
        self.in_std.setObjectName(u"in_std")
        self.in_std.setGeometry(QRect(315, 260, 275, 30))
        self.in_pricestep = QLineEdit(window)
        self.in_pricestep.setObjectName(u"in_pricestep")
        self.in_pricestep.setGeometry(QRect(315, 340, 275, 30))
        self.in_timestep = QLineEdit(window)
        self.in_timestep.setObjectName(u"in_timestep")
        self.in_timestep.setGeometry(QRect(315, 380, 275, 30))
        self.in_maturitydate = QDateEdit(window)
        self.in_maturitydate.setObjectName(u"in_maturitydate")
        self.in_maturitydate.setGeometry(QRect(315, 300, 275, 30))
        self.in_maturitydate.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.but_calculate = QPushButton(window)
        self.but_calculate.setObjectName(u"but_calculate")
        self.but_calculate.setGeometry(QRect(10, 420, 580, 30))
        self.output = QTextBrowser(window)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 460, 580, 100))

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)

        # calculate and display result
        self.but_calculate.clicked.connect(self._displayresult)
        
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Options Calculator", None))
#if QT_CONFIG(tooltip)
        window.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        window.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        window.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.introduction.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This options calculator approximates the fair price of an European Option using the <span style=\" font-weight:600;\">Explicit Finite Difference</span> method to solve Black-Scholes Partial Differential Equation.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">* Assumes Maximum Price of Asset &lt; 2 * Option's Strike Price</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margi"
                        "n-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">** Assumes Asset does not pay dividends</span></p></body></html>", None))
        self.text_option_type.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Option Type</span></p></body></html>", None))
        self.text_asset_price.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Current Asset Price</span></p></body></html>", None))
        self.text_strike_price.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Option Strike Price</span></p></body></html>", None))
        self.text_interest.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Risk-Free Interest Rate</span></p></body></html>", None))
        self.text_volatility.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Asset's Standard Deviation</span></p></body></html>", None))
        self.text_maturity_date.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Option's Maturity Date</span></p></body></html>", None))
        self.text_price_step.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Number of Price Steps</span></p></body></html>", None))
        self.text_time_step.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Number of Time Steps</span></p></body></html>", None))
        self.in_option_type.setItemText(0, QCoreApplication.translate("window", u"Call", None))
        self.in_option_type.setItemText(1, QCoreApplication.translate("window", u"Put", None))

        self.in_assetprice.setInputMask("")
        self.in_assetprice.setPlaceholderText(QCoreApplication.translate("window", u"Input underlying asset's current price.", None))
        self.in_strikeprice.setInputMask("")
        self.in_strikeprice.setText("")
        self.in_strikeprice.setPlaceholderText(QCoreApplication.translate("window", u"Input option's strike price.", None))
        self.in_interestrate.setInputMask("")
        self.in_interestrate.setText("")
        self.in_interestrate.setPlaceholderText(QCoreApplication.translate("window", u"Input risk-free interest rate in percentage.", None))
        self.in_std.setInputMask("")
        self.in_std.setText("")
        self.in_std.setPlaceholderText(QCoreApplication.translate("window", u"Input standard deviation of underlying asset.", None))
        self.in_pricestep.setInputMask("")
        self.in_pricestep.setText("")
        self.in_pricestep.setPlaceholderText("")
        self.in_timestep.setInputMask("")
        self.in_timestep.setText("")
        self.in_timestep.setPlaceholderText("")
        self.but_calculate.setText(QCoreApplication.translate("window", u"Calculate", None))
        self.output.setHtml(QCoreApplication.translate("window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

