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
    *00XX0*TS7,RPT 5;//TS 10uS
    *00XX0*;// 0    To enter I2C mode: VPP= 0101 0011 1010 11 01
    *10XX0*;
    *01XX0*;// 1
    *11XX0*;
    *00XX0*;// 0
    *10XX0*;
    *01XX0*;// 1
    *11XX0*;
    *00XX0*;// 0
    *10XX0*;
    *00XX0*;// 0
    *10XX0*;
    *01XX0*;// 1
    *11XX0*;
    *01XX0*;// 1
    *11XX0*;
    *01XX0*;// 1
    *11XX0*;
    *00XX0*;// 0
    *10XX0*;
    *01XX0*;// 1
    *11XX0*;
    *00XX0*;// 0
    *10XX0*;
    *01XX0*;// 1
    *11XX0*;
    *01XX0*;// 1
    *11XX0*;
    *00XX0*;// 0
    *10XX0*;
    *01XX0*;// 1
    *11XX0*;
    *0X110*RPT 8; //delay
    *0X110*;//I2C MODE
    *0X110*;//I2C start
    *0X100*;
    *0X000*;//CCIN CC=0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X000*;//0  COMMAND ADDR
    *0X100*;
    *0X100*;
    *0X000*;
    *0X000*;//0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X010*;//1
    *0X110*;
    *0X110*;
    *0X010*;
    *0X000*;//0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;//ACK
    *0X1L0*;
    *0X1L0*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;//H  READ ID0=11 0000 0010
    *0X1H0*;
    *0X0X0*;//H
    *0X1H0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//H
    *0X1H0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X000*;//STOP
    *0X100*;
    *0X110*;
    *0X110*;//I2C start
    *0X110*;
    *0X100*;
    *0X000*;//CCIN CC=0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X000*;//0  COMMAND ADDR
    *0X100*;
    *0X100*;
    *0X000*;
    *0X000*;//0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X010*;//1
    *0X110*;
    *0X110*;
    *0X010*;
    *0X010*;//1
    *0X110*;
    *0X110*;
    *0X010*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;//ACK
    *0X1L0*;
    *0X1L0*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;//X     READ ID0=XX 0001 0001
    *0X1X0*;
    *0X0X0*;//X
    *0X1X0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//H
    *0X1H0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//L
    *0X1L0*;
    *0X0X0*;//H
    *0X1H0*;
    *0X000*;//STOP
    *0X100*;
    *0X110*;
    *0X110*;//I2C start     set rwt 32H
    *0X110*;
    *0X100*;
    *0X000*;//CCIN CC=0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X010*;//1  COMMAND ADDR
    *0X110*;
    *0X110*;
    *0X010*;
    *0X000*;//0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X000*;//0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X000*;//0
    *0X100*;
    *0X100*;
    *0X000*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;//ACK
    *0X1L0*;
    *0X1L0*;
    *0X0X0*;
    *0X0X0*;
    *0X0X0*;
    *0X000*;//0 write 32H 00 0011 0010
    *0X100*;
    *0X000*;//0
    *0X100*;
    *0X000*;//0
    *0X100*;
    *0X000*;//0
    *0X100*;
    *0X010*;//1
    *0X110*;
    *0X010*;//1
    *0X110*;
    *0X000*;//0
    *0X100*;
    *0X000*;//0
    *0X100*;
    *0X010*;//1
    *0X110*;
    *0X000*;//0
    *0X100*;
    *0X0X0*;
    *0X0X0*;//ACK
    *0X1L0*;
    *0X1L0*;
    *0X0X0*;
    *0X0X0*;
    *0X000*;//STOP
    *0X100*;
    *0X110*;
    *0X110*;//I2C start 
    *0X100*;
    *0X100*;
    *0X010*;//进入write mode
    *0X010*;
    *0X110*;//CC=1
    *0X110*;
    *0X000*;
    *0X000*;
    *0X100*;//RWB=0
    *0X100*;
IO: *0X000*;
P6V:*0X000*RPT 10;//PMU 6.75V接上 VPP set to 6.75V for OTP program 
    *0X000*RPT 10;//write data start
"""

patternForNotEnd = """    *0X000*;
    *0X100*;//NOT END 0
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1L0*;//ACK AK06
    *0X0X0*;
    *0X0X0*;
"""
patternForEnd = """    *0X010*TS1;//5uS
    *0X110*;//END 1
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1H0*;
    *0X0X0*;
    *0X1L0*;//ACK AK06
    *0X0X1*RPT 2000;//VPP PMU(6.75V) OFF
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X011*;
    *0X111*;
    *0X001*;
    *0X101*;//AKI8
    *0X001*RPT 50;
    *0X0H1*;
    *0X1H1*;
    *0X0H1*;
    *0X1H1*;
    *0X0H1*;
    *0X1H1*;
    *0X0H1*;
    *0X1H1*;
    *0X0H1*;
    *0X1L1*;//AKO9
    *0X0L1*;
    *0X1L1*;
    *0X0H1*;
    *0X1H1*;
    *0X011*;
    *0X111*;
    *0X001*;//STOP
    *0X101*;
    *0X111*;
    *0X111*;
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
                "    *0X0%s0*;//addr=%s(%d), data = %s => %s %s\n"
                % (
                    bitList[i],
                    "0x" + str(hex(byteCnt)[2:].zfill(5)).upper(),
                    byteCnt,
                    "0x" + str(hex(data)[2:].zfill(2)).upper(),
                    "".join(bitList[7:3:-1]),
                    "".join(bitList[-5:-9:-1]),
                )
            )
            fp.write("    *0X1%s0*;//D%s %s\n" % (bitList[i], i, bitList[i]))
        else:
            if i == 6 and byteCnt == 0x07A7:
                fp.write("O8M:")
                fp.write("*0X0%s0*;\n" % bitList[i])
                fp.write("    *0X1%s0*;//D%s %s\n" % (bitList[i], i, bitList[i]))
                continue
            if i == 5 and byteCnt == 0x07A8:
                fp.write("O32:")
                fp.write("*0X%s00*;\n" % bitList[i])
                fp.write("    *0X1%s0*;//D%s %s\n" % (bitList[i], i, bitList[i]))
                continue
            fp.write("    *0X0%s0*;\n" % bitList[i])
            fp.write("    *0X1%s0*;//D%s %s\n" % (bitList[i], i, bitList[i]))
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
            # if byteCnt % (int(fileSize / 100)) == 0 or byteCnt == fileSize:
            #     self.labelStatus.setText(
            #         f"生成writeRom.pat: 共 {int(fileSize/1024)} KB, 已处理 {int(byteCnt/1024)} KB, {int((byteCnt/fileSize)*100)}%"
            #     )
            #     self.labelStatus.repaint()
            #     self.pBar.setValue(int((byteCnt / fileSize) * 100))
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
