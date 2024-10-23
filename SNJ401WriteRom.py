#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from MyWindow import *

patternHeadInfo = """SET_DEC_FILE "SHX689.DEC"

HEADER  PA3,VPP,PB3,PB2,VPP_CTRL;

SPM_PATTERN(writeRom)
{
       //PVPP
       //APBB
       //3P32
        *11XX0*TS9;
        *00000*;
        *00000*;
        *00000*;
        *10000*;//  0
        *10000*;
        *01000*;
        *11000*;//  1
        *11000*;
        *01000*;
        *10000*;//  0
        *10000*;
        *00000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *00000*;
        *10000*;//  0
        *00000*;
        *00000*;
        *10000*;//  0
        *10000*;
        *01000*;
        *11000*;//  1
        *11000*;
        *01000*;
        *11000*;//  1
        *11000*;
        *01000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *00000*;
        *10000*;//  0
        *00000*;
        *01000*;
        *11000*;//  1
        *11000*;
        *00000*;
        *10000*;//  0
        *10000*;
        *00000*;
        *11000*;//  1
        *11000*;
        *01000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *01000*;
        *11000*;//  1
        *11000*;
        *00000* RPT 80;
        *00000*;
        *10000*;// 0
        *10000*;
        *00000*;
        *11000*;// 1
        *11000*;
        *01000*;
        *00000*;
        *10000*;//  0
        *00000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *00000*;
        *10000*;//  0
        *10000*;
        *00000*;
        *10000*;//  0
        *10000*;
        *00000*;
        *11000*;//  1
        *11000*;
        *01000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *00000*;
        *10000*;//  0
        *10000*;
        *01000*;
        *11000*;//  1
        *11000*;
        *01000*;
        *10000*;//  0
        *10000*;
        *00000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *01000*;
        *11000*;//  1
        *01000*;
        *00000*;
        *10000*;// 0
        *10000*;
        *01000*;
        *11000*;// 1
        *11000*;
        *01000*;
        *00000*;
        *00000*;
        *00000* RPT 10;
        *X0000*;
        *X0000*;
        *X0000*;
        *X0000*;
        *X0110*;
        *X0110*RPT 15;
        *X0110*;
        *X0110*;
        *X0100*;// i2c start
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0000*;// Read ID0 (CMD 2)
        *X0000*;
        *X0000*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0100*;
        *X0000*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0100*;
        *X0000*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0100*;
        *X0000*;
        *X0010*;
        *X0010*;
        *X0010*;
        *X0110*;//  1
        *X0110*;
        *X0110*;
        *X0010*;
        *X0000*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0100*;
        *X0000*;
        *X00L0*;
        *X01L0*;//
        *X00H0*;// ID0
        *X01H0*;//   1
        *X00H0*;
        *X01H0*;//   1
        *X00L0*;
        *X01L0*;//   0
        *X00L0*;
        *X01L0*;//   0
        *X00L0*;
        *X01L0*;//   0
        *X00L0*;
        *X01L0*;//   0
        *X00L0*;
        *X01L0*;//   0
        *X00L0*;
        *X01L0*;//   0
        *X00H0*;
        *X01H0*;//   1
        *X00L0*;
        *X01L0*;//   0
        *X0000*;
        *X0000*;
        *X0100*;
        *X0100*;//  stop
        *X0110*;
        *X0110*;
        *X0110*;
        *X0110*;
        *X0110*RPT 22;
        *X0110*;
        *X0110*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0000*;// Read ID0 (CMD 3)
        *X0000*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0000*;
        *X0000*;
        *X0100*;//  0
        *X0100*;
        *X0000*;
        *X0010*;
        *X0010*;
        *X0110*;//  1
        *X0110*;
        *X0010*;
        *X0010*;
        *X0110*;//  1
        *X0110*;
        *X0010*;
        *X00L0*;
        *X01L0*;//  ack
        *X00H0*;//  ID1
        *X01H0*;// 1
        *X00H0*;
        *X01H0*;// 1
        *X00L0*;
        *X01L0*;// 0
        *X00L0*;
        *X01L0*;// 0
        *X00L0*;
        *X01L0*;// 0
        *X00H0*;
        *X01H0*;// 1
        *X00L0*;
        *X01L0*;// 0
        *X00L0*;
        *X01L0*;// 0
        *X00L0*;
        *X01L0*;// 0
        *X00H0*;
        *X01H0*;// 1
        *X00X0*;
        *X0000*;
        *X0000*;
        *X0100*;
        *X0100*;// stop
        *X0110*;
        *X0110*;
        *X0110*;
        *X0110*RPT 10;
        *X0110*;
        *X0110*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0100*;
        *X0000*;
        *X0000*;
        *X0100*;// 0
        *X0100*;
        *X0000*;
        *X0000*;
        *X0010*;// A3
        *X0110*;// A3  1        //SET Program waiting time RWT to #32H (CMD 8)
        *X0010*;// A3
        *X0000*;// A2
        *X0100*;// A2  0
        *X0000*;// A2
        *X0000*;// A1
        *X0100*;// A1  0
        *X0000*;// A1
        *X0000*;// A0
        *X0100*;// A0  0
        *X0000*;// A0
        *X00X0*;// ACK
        *X01L0*;// ACK
        *X00X0*;// ACK
        *X0000*;// D9
        *X0100*;// D9   0     //SET RWT BIT[9:0]=032H;
        *X0000*;// D9
        *X0000*;// D8
        *X0100*;// D8   0
        *X0000*;// D8
        *X0000*;// D7
        *X0100*;// D7   0
        *X0000*;// D7
        *X0000*;// D6
        *X0100*;// D6
        *X0000*;// D6   0
        *X0010*;// D5
        *X0110*;// D5   1
        *X0010*;// D5
        *X0010*;// D4
        *X0110*;// D4   1
        *X0010*;// D4
        *X0000*;// D3
        *X0100*;// D3   0
        *X0000*;// D3
        *X0000*;// D2
        *X0100*;// D2   0
        *X0000*;// D2
        *X0010*;// D1
        *X0110*;// D1   1
        *X0010*;// D1
        *X0000*;// D0
        *X0100*;// D0   0
        *X0000*;// D0
        *X00X0*;// ACK
        *X01L0*;// ACK
        *X00X0*;// ACK
        *X0000*;
        *X0000*;
        *X0100*;
        *X0100*;
        *X0110*;
        *X0110*;
        *X0110*;
        *XX110*;// PA2(VPP) set to 6.8V for OTP program
        *XX110*RPT 12;
        *XX100*;
        *XX100*;
        *XX000*;// OTP Sequential programming
        *XX000*;
        *XX010*;
        *XX010*;
        *XX110*;//  1
        *XX110*;
        *XX010*;
        *XX010*;
        *XX000*;
        *XX000*;
        *XX100*;//  0
        *XX100*;
        *XX000*;
        *XX000*;//
IO:     *0X000*;
P6V:    *0X000*RPT 10;//PMU 6.75V接上 write data start
"""

patternForNotEnd = """        *XX100*;// ENDB 0
        *XX000*;// ENDB 0
        *XX0H0*;// OTP write pulse
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0H0*;
        *XX1H0*;
        *XX0L0*;// ack low
        *XX1L0*;
        *XX0X0*;
        *XX0X0*;
"""
patternForEnd = """        *XX110*;// ENDB 1 data stop
        *XX010*;// ENDB 1 data stop
        *XX0H0*;// OTP write pulse
        *XX1H0*;// 1
        *XX0H0*;
        *XX1H0*;// 2
        *XX0H0*;
        *XX1H0*;// 3
        *XX0H0*;
        *XX1H0*;// 4
        *XX0H0*;
        *XX1H0*;// 5
        *XX0H0*;
        *XX1H0*;// 6
        *XX0H0*;
        *XX1H0*;// 7
        *XX0H0*;
        *XX1H0*;// 8
        *XX0H0*;
        *XX1H0*;// 9
        *XX0H0*;
        *XX1H0*;// 10
        *XX0H0*;
        *XX1H0*;// 11
        *XX0L0*;// ack low
        *XX1L0*;// 12
        *XX0X0*;
        *XX0X0*;
        *XX0X1*RPT 2000;//VPP PMU(6.75V) OFF
        *XX011*;
        *XX111*;//  1
        *XX011*;
        *XX111*;//  2
        *XX011*;
        *XX111*;//  3
        *XX011*;
        *XX111*;//  4
        *XX011*;
        *XX111*;//  5
        *XX011*;
        *XX111*;//  6
        *XX011*;
        *XX111*;//  7
        *XX011*;
        *XX111*;//  8
        *XX011*;
        *XX111*;//  9
        *X0011*;
        *X0111*;//  10
        *X0001*;
        *X0101*;// AKI8 11
        *X00H1*;
        *X01H1*;
        *X00H1*;
        *X01H1*;
        *X00H1*;
        *X01H1*;
        *X00H1*;
        *X01H1*;
        *X00H1*;
        *X00H1*;
        *X0101*;// L
        *X0001*;// L
        *X0101*;// AKO9 L
        *X0011*;
        *X0111*;
        *X0001*;
        *X0001*;
        *X0101*;
        *X0101*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
        *X0111*;
}
"""


def data2bitList(data):
    bitList = ["0"] * 8
    for i in range(8 - 1, -1, -1):
        if data >> i & 1:
            bitList[i] = "1"
        else:
            bitList[i] = "0"
    return bitList


def writeData2File(data, bitList, byteCnt, fp, fileSize):
    for i in range(8 - 1, -1, -1):
        if i == 7:
            fp.write(
                "        *XX1%s0*;// D%s %s addr=%s(%d), data = %s => %s %s\n"
                % (
                    bitList[i],
                    i,
                    bitList[i],
                    "0x" + str(hex(byteCnt)[2:].zfill(5)).upper(),
                    byteCnt,
                    "0x" + str(hex(data)[2:].zfill(2)).upper(),
                    "".join(bitList[7:3:-1]),
                    "".join(bitList[-5:-9:-1]),
                )
            )
            fp.write("        *XX0%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
        else:
            if i == 6 and byteCnt == 0x07A7:
                fp.write("O8M:    ")
                fp.write("*XX1%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
                fp.write("        *XX0%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
                continue
            if i == 5 and byteCnt == 0x07A8:
                fp.write("O32:    ")
                fp.write("*XX1%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
                fp.write("        *XX0%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
                continue
            fp.write("        *XX1%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
            fp.write("        *XX0%s0*;// D%s %s\n" % (bitList[i], i, bitList[i]))
    if byteCnt != fileSize - 1:
        fp.write(patternForNotEnd)
    else:
        fp.write(patternForEnd)


def data2Pattern(self, dataList, patternFile, fileSize):
    byteCnt = 0
    bitList = ["0"] * 8
    with open(patternFile, "a", encoding="UTF-8") as fp:
        fp.write(patternHeadInfo)
        for data in dataList:
            bitList = data2bitList(data)
            writeData2File(data, bitList, byteCnt, fp, fileSize)
            byteCnt += 1
            if byteCnt % (int(fileSize / 100)) == 0 or byteCnt == fileSize:
                self.labelStatus.setText(
                    f"生成writeRom.pat: 共 {int(fileSize/1024)} KB, 已处理 {int(byteCnt/1024)} KB, {int((byteCnt/fileSize)*100)}%"
                )
                self.labelStatus.repaint()
                self.pBar.setValue(int((byteCnt / fileSize) * 100))
    return byteCnt


def checkFileSize(self, file, size):
    fileSize = os.path.getsize(file)
    if fileSize != size:
        QMessageBox.critical(
            self, "警告", f"{file} 不是{size/1024}KB 文件大小,请确认fpga文件是否正确!"
        )


def getFileData(file):
    dataList = list()
    with open(file, "rb") as fp:
        while True:
            data = fp.read(16)
            if not data:  # 文件末尾跳出
                break
            for metaData in data:
                dataList.append(metaData)
    return dataList


def writeRom(self, filePath, fileSize):
    parDir = os.path.dirname(filePath)
    _, file = os.path.split(filePath)
    fileName, _ = os.path.splitext(file)
    srcFile = parDir + "/" + "WRITE_" + fileName.upper() + ".pat"
    if os.path.exists(srcFile):
        os.remove(srcFile)
    checkFileSize(self, filePath, fileSize)
    dataList = getFileData(filePath)
    byteCnt = data2Pattern(self, dataList, srcFile, fileSize)
    if byteCnt != fileSize:
        QMessageBox.critical(
            self, "警告", f"生成的{srcFile} 写入字节数不是{fileSize},请确认！！！"
        )
    QMessageBox.information(self, "完成", "writeRom 任务完成!")
