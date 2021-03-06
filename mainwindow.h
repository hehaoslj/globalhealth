#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QResizeEvent>
#include <QWebEngineView>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
protected :
    void resizeEvent(QResizeEvent *event);
private:
    Ui::MainWindow *ui;
    QWebEngineView *view;
};

#endif // MAINWINDOW_H
