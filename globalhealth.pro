#-------------------------------------------------
#
# Project created by QtCreator 2016-10-03T10:14:42
#
#-------------------------------------------------

QT       += core gui

QT += webenginewidgets webchannel
CONFIG += c++11
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = globalhealth
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui

OTHER_FILES += \
    site/template/*.html \
    site/static/*.css  \
    site/static/*.png   \
    site/app/*.py   \
    site/app/*.json \
    site/static/*.js


OTHER_FILES += \
    ../lib/metro/docs/templates/*.html

DISTFILES += \
    site/template/base.html \
    site/static/start.js    \
    site\static\metro\css\*.css \
    site\static\metro\js\*.js   \
    site/static/index.js \
    site/app/tile.json \
    site/static/start.css \
    site/template/content.html \
    site/static/content.js \
    site/static/pi/bjavid/*.md \
    site/static/meeting/*.md \
    site/static/aboutus.md \
    site/static/pi/yexiang/yexiang.md \
    site/static/pi/fengcheng/fengcheng.md \
    site/static/pi/gongcheng/gongcheng.md \
    site/static/pi/jingrenzhang/jingrenzhang.md \
    site/static/pi/linqizhang/linqizhang.md
