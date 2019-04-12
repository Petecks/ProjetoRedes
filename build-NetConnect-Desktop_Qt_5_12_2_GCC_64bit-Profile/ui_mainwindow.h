/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionAudio;
    QAction *actionDatai;
    QAction *actionBefehle;
    QWidget *centralWidget;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QGraphicsView *graphicsView;
    QLabel *label;
    QCheckBox *Checksum;
    QCheckBox *checkBox_2;
    QMenuBar *menuBar;
    QMenu *menuNetConnect_Sofware;
    QMenu *menuHilfe;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->setEnabled(true);
        MainWindow->resize(800, 600);
        MainWindow->setDockOptions(QMainWindow::AllowTabbedDocks|QMainWindow::AnimatedDocks);
        actionAudio = new QAction(MainWindow);
        actionAudio->setObjectName(QString::fromUtf8("actionAudio"));
        actionDatai = new QAction(MainWindow);
        actionDatai->setObjectName(QString::fromUtf8("actionDatai"));
        actionBefehle = new QAction(MainWindow);
        actionBefehle->setObjectName(QString::fromUtf8("actionBefehle"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        centralWidget->setAutoFillBackground(false);
        radioButton = new QRadioButton(centralWidget);
        radioButton->setObjectName(QString::fromUtf8("radioButton"));
        radioButton->setEnabled(true);
        radioButton->setGeometry(QRect(10, 0, 121, 23));
        radioButton->setCheckable(true);
        radioButton->setAutoExclusive(true);
        radioButton_2 = new QRadioButton(centralWidget);
        radioButton_2->setObjectName(QString::fromUtf8("radioButton_2"));
        radioButton_2->setEnabled(true);
        radioButton_2->setGeometry(QRect(10, 20, 121, 23));
        radioButton_2->setCheckable(true);
        radioButton_2->setAutoExclusive(true);
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setGeometry(QRect(750, 0, 50, 50));
        graphicsView->setAutoFillBackground(false);
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(680, 540, 121, 17));
        Checksum = new QCheckBox(centralWidget);
        Checksum->setObjectName(QString::fromUtf8("Checksum"));
        Checksum->setGeometry(QRect(160, 0, 92, 23));
        checkBox_2 = new QCheckBox(centralWidget);
        checkBox_2->setObjectName(QString::fromUtf8("checkBox_2"));
        checkBox_2->setGeometry(QRect(160, 20, 92, 23));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 800, 22));
        menuBar->setNativeMenuBar(true);
        menuNetConnect_Sofware = new QMenu(menuBar);
        menuNetConnect_Sofware->setObjectName(QString::fromUtf8("menuNetConnect_Sofware"));
        menuHilfe = new QMenu(menuBar);
        menuHilfe->setObjectName(QString::fromUtf8("menuHilfe"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        menuBar->addAction(menuNetConnect_Sofware->menuAction());
        menuBar->addAction(menuHilfe->menuAction());
        menuNetConnect_Sofware->addSeparator();
        menuNetConnect_Sofware->addSeparator();
        menuNetConnect_Sofware->addAction(actionAudio);
        menuNetConnect_Sofware->addAction(actionDatai);
        menuHilfe->addAction(actionBefehle);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "NetTransfer", nullptr));
        actionAudio->setText(QApplication::translate("MainWindow", "Audio", nullptr));
        actionDatai->setText(QApplication::translate("MainWindow", "Datei", nullptr));
        actionBefehle->setText(QApplication::translate("MainWindow", "Befehle", nullptr));
        radioButton->setText(QApplication::translate("MainWindow", "UDP Protokoll", nullptr));
        radioButton_2->setText(QApplication::translate("MainWindow", "TCP Protokoll", nullptr));
        label->setText(QApplication::translate("MainWindow", "Peteck Develops", nullptr));
        Checksum->setText(QApplication::translate("MainWindow", "Checksum", nullptr));
        checkBox_2->setText(QApplication::translate("MainWindow", "CRC", nullptr));
        menuNetConnect_Sofware->setTitle(QApplication::translate("MainWindow", "\303\234bertragungsmodus", nullptr));
        menuHilfe->setTitle(QApplication::translate("MainWindow", "Hilfe", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
