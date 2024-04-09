coffee_menu={'아메리카노':1500, '카페라떼':2700, '카라멜 마끼아또':3700, '바닐라 라떼':3400}
coffee_pay=[1500,2700,3700,3400]
ade_menu={'자몽에이드':3500, '레몬에이드':3500, '청포도에이드':3500}
ade_pay=[3500,3500,3500]
tea_menu={'페퍼민트티':2500,'케모마일티':2500, '밀크티':3800, '루이보스티':2500}
tea_pay=[2500,2500,3000,2500]
cof_k = list(coffee_menu.keys())
cof_v= list(coffee_menu.values())
ade_k = list(ade_menu.keys())
ade_v = list(ade_menu.values())
tea_k = list(tea_menu.keys())
tea_v = list(tea_menu.values())

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from time import sleep

form_class = uic.loadUiType("team3kiosk_test2.ui")[0]

class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        #메인 작업
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.turn = 0
        self.turn_m = 0
        self.cof_m = 0
        self.ade_m = 0
        self.tea_m = 0
        self.total_a = 0
        self.pointidn = ""
        self.stamp = {}
        self.line = {'번호표' :  1}
        self.loading.hide()
        self.movie = QMovie('mainpage.gif', QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.main.setMovie(self.movie)
        self.movie.start()
        self.ice.setAutoExclusive(True)
        self.hot.setAutoExclusive(True)
        self.tall.setAutoExclusive(True)
        self.venti.setAutoExclusive(True)
        self.total_lb.setText("%d"% self.total_a)
        self.bucket_g.setDisabled(True)
        self.stampbtn.setDisabled(True)
        self.bucket_m.horizontalHeader().setVisible(True)
        self.loading.setStyleSheet("QProgressBar::chunk "
                       "{"
                       "background-color: #BCA37F;"
                       "}")
        header = self.bucket_m.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header = self.receipt.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header = self.pointid_2.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)


        #버튼
        self.mainbtn.clicked.connect(lambda : self.btn_f(a=1))
        self.store.clicked.connect(lambda : self.purchase_limited(a=2))
        self.pack.clicked.connect(lambda : self.purchase_limited(a=2))
        self.backbtn_1.clicked.connect(lambda : self.btn_rev_2(a=0))
        self.backbtn_2.clicked.connect(lambda : self.btn_rev_2(a=0))
        self.backbtn_3.clicked.connect(lambda : self.btn_rev(a=2))
        self.backbtn_4.clicked.connect(lambda : self.btn_rev_1(a=2))
        self.backbtn_5.clicked.connect(lambda: self.btn_rev_3(a=6))
        self.ice.clicked.connect(self.b_btn)
        self.hot.clicked.connect(self.b_btn)
        self.tall.clicked.connect(self.b_btn)
        self.venti.clicked.connect(self.b_btn)
        self.purchase.clicked.connect(lambda : self.purchase_btn(a=6))
        self.yes.clicked.connect(lambda : self.btn_f(a=8))
        self.no.clicked.connect(lambda : self.btn_f(a=8))
        self.lineup.clicked.connect(self.changenum)
        self.cash.clicked.connect(lambda: self.btn_f(a=9))
        self.gocounter.clicked.connect(self.clear)

        #음료 버튼
        self.americano.clicked.connect(lambda: self.cof_btn(a=1))
        self.cafelatte.clicked.connect(lambda: self.cof_btn(a=2))
        self.caramel.clicked.connect(lambda: self.cof_btn(a=3))
        self.vanilla.clicked.connect(lambda: self.cof_btn(a=4))
        self.jamong.clicked.connect(lambda: self.ade_btn(a=1))
        self.lemon.clicked.connect(lambda: self.ade_btn(a=2))
        self.grape.clicked.connect(lambda: self.ade_btn(a=3))
        self.mint.clicked.connect(lambda: self.tea_btn(a=1))
        self.mile.clicked.connect(lambda: self.tea_btn(a=2))
        self.milk.clicked.connect(lambda: self.tea_btn(a=3))
        self.Luibos.clicked.connect(lambda: self.tea_btn(a=4))
        self.bucket_g.clicked.connect(self.bucket_f)


        # 시럽 버튼
        self.turn = 0
        self.syrup_h.clicked.connect(self.hWidget)
        self.syrup_v.clicked.connect(self.vWidget)
        self.shot.clicked.connect(self.sWidget)

        #포인트적립관련 버튼
        self.yes_btn.clicked.connect(lambda: self.btn_f(a=7))
        self.no_btn.clicked.connect(lambda:self.btn_f(a=4))
        self.stampbtn.clicked.connect(lambda: self.btn_f(a=4))
        self.point_btn0.clicked.connect(lambda:self.point('0'))
        self.point_btn.clicked.connect(lambda:self.point('1'))
        self.point_btn2.clicked.connect(lambda:self.point('2'))
        self.point_btn3.clicked.connect(lambda:self.point('3'))
        self.point_btn4.clicked.connect(lambda:self.point('4'))
        self.point_btn5.clicked.connect(lambda:self.point('5'))
        self.point_btn6.clicked.connect(lambda:self.point('6'))
        self.point_btn7.clicked.connect(lambda:self.point('7'))
        self.point_btn8.clicked.connect(lambda:self.point('8'))
        self.point_btn9.clicked.connect(lambda:self.point('9'))
        self.point_btn_del.clicked.connect(lambda:self.cal(c=2))
        self.point_btn_ac.clicked.connect(lambda:self.cal(c=1))
        self.card.clicked.connect(self.cardf)
        # self.gocounter.clicked.connect(self.goco)
        # self.cash.clicked.connect(self.cashf)



    def purchase_limited(self,a):
        self.total_a = 0
        self.total_lb.setText("0")
        self.total_lb_2.setText("0")
        self.turn_m = 0
        self.stackedWidget.setCurrentIndex(a)
        i = self.bucket_m.rowCount()
        print(self.bucket_m.rowCount())
        if i < 1:
            self.purchase.setDisabled(True)
        else:
            self.purchase.setEnabled(True)

    #버튼 함수
    def btn_f(self,a):
        self.stackedWidget.setCurrentIndex(a)


    def btn_rev(self,a):
        self.stackedWidget.setCurrentIndex(a)
        self.ice.setCheckable(False)
        self.hot.setCheckable(False)
        self.tall.setCheckable(False)
        self.venti.setCheckable(False)
        self.ice.setCheckable(True)
        self.hot.setCheckable(True)
        self.tall.setCheckable(True)
        self.venti.setCheckable(True)
        self.cof_m = 0
        self.ade_m = 0
        self.tea_m = 0
        self.ta1.setRowCount(0)
        self.turn = 0
        i = self.bucket_m.rowCount()
        print(self.bucket_m.rowCount())
        if i < 1:
            self.purchase.setDisabled(True)
        else:
            self.purchase.setEnabled(True)

    def btn_rev_1(self,a):
        self.stackedWidget.setCurrentIndex(a)
        self.receipt.setRowCount(0)
    def btn_rev_2(self,a):
        self.stackedWidget.setCurrentIndex(a)
        self.bucket_m.setRowCount(0)
    def btn_rev_3(self,a):
        self.stackedWidget.setCurrentIndex(a)
        self.pointid.clear()
        self.pointidn = ''



    #커피 버튼
    def cof_btn(self,a):
        self.stackedWidget.setCurrentIndex(3)
        self.image.setPixmap(QPixmap("%d"% a))
        self.menu_n.setText(str(cof_k[a - 1]))
        self.purch.setText(str(cof_v[a - 1]))
        self.ice.show()
        self.temper.show()
        self.hot.show()
        self.syrup_h.show()
        self.syrup_v.show()
        self.shot.show()
        self.ta1.show()
        self.line_3.show()
        self.cof_m += a
        self.label_34.show()
        self.label_35.show()
        self.label_36.show()

    #에이드 버튼
    def ade_btn(self,a):
        self.stackedWidget.setCurrentIndex(3)
        self.image.setPixmap(QPixmap("%d"% (a+100)))
        self.menu_n.setText(str(ade_k[a - 1]))
        self.purch.setText(str(ade_v[a - 1]))
        self.ice.hide()
        self.temper.hide()
        self.hot.hide()
        self.syrup_h.hide()
        self.syrup_v.hide()
        self.shot.hide()
        self.ta1.hide()
        self.line_3.hide()
        self.ade_m += a
        self.label_34.hide()
        self.label_35.hide()
        self.label_36.hide()
    #티 버튼
    def tea_btn(self,a):
        self.stackedWidget.setCurrentIndex(3)
        self.image.setPixmap(QPixmap("%d"% (a+200)))
        self.menu_n.setText(str(tea_k[a - 1]))
        self.purch.setText(str(tea_v[a - 1]))
        self.ice.show()
        self.temper.show()
        self.hot.show()
        self.syrup_h.hide()
        self.syrup_v.hide()
        self.shot.hide()
        self.ta1.hide()
        self.line_3.hide()
        self.tea_m += a
        self.label_34.hide()
        self.label_35.hide()
        self.label_36.hide()
    #시럽 추가 버튼
    def hWidget(self):
        i = self.turn
        self.ta1.insertRow(i)
        self.ta1.setItem(i, 0, QTableWidgetItem("헤이즐넛 시럽"))

        cancel_button = QPushButton("취소")
        cancel_button.clicked.connect(self.on_cancel_clicked)

        self.ta1.setCellWidget(i, 1, cancel_button)
        self.turn += 1

    def vWidget(self):
        i = self.turn
        self.ta1.insertRow(i)
        self.ta1.setItem(i, 0, QTableWidgetItem("바닐라 시럽"))
        cancel_button = QPushButton("취소")
        cancel_button.clicked.connect(self.on_cancel_clicked)

        self.ta1.setCellWidget(i, 1, cancel_button)
        self.turn += 1

    def sWidget(self):
        i = self.turn
        self.ta1.insertRow(i)
        self.ta1.setItem(i, 0, QTableWidgetItem("샷추가"))
        cancel_button = QPushButton("취소")
        cancel_button.clicked.connect(self.on_cancel_clicked)

        self.ta1.setCellWidget(i, 1, cancel_button)
        self.turn += 1
    #시럽 취소 버튼
    def on_cancel_clicked(self):
        button = self.sender()
        item = self.ta1.indexAt(button.pos())
        self.ta1.removeRow(item.row())
        self.turn -= 1

    def on_cancel_clicked1(self):
        # print(f'Cancel button clicked for row {row}')
        button = self.sender()
        it = self.bucket_m.indexAt(button.pos())
        self.total_a -= int(self.bucket_m.item(it.row(),3).text())
        # self.total_a -= int(self.bucket_m.item(item.row(),3))
        self.bucket_m.removeRow(it.row())
        self.total_lb.setText("%d" % self.total_a)
        self.turn_m -= 1
        i = self.bucket_m.rowCount()
        print(self.bucket_m.rowCount())
        if i < 1:
            self.purchase.setDisabled(True)
        else:
            self.purchase.setEnabled(True)
    def b_btn(self):
        self.bucket_g.setEnabled(True)


    #담기 버튼
    def bucket_f(self):
        # i = 0
        i = self.turn_m
        self.bucket = []
        self.stackedWidget.setCurrentIndex(2)
        self.bucket_m.insertRow(i)
        self.c_f = coffee_pay[self.cof_m-1] + (500 * self.turn)
        self.a_f = ade_pay[self.ade_m-1] + (500 * self.turn)
        self.t_f = tea_pay[self.tea_m-1] + (500 * self.turn)

        for a in range(self.turn):
            self.pocket = self.ta1.item(a,0).text()
            self.bucket.append(self.pocket)
        if self.ice.isChecked():
            self.bucket_m.setItem(i, 0, QTableWidgetItem(self.menu_n.text() + "ice"))
            self.c_f += 300
            self.t_f += 300
        else:
            self.bucket_m.setItem(i, 0, QTableWidgetItem(self.menu_n.text() + "hot"))
        if self.venti.isChecked():
            self.bucket_m.setItem(i,1,QTableWidgetItem("venti"))
            self.c_f += 500
            self.a_f += 500
            self.t_f += 500
        else :
            self.bucket_m.setItem(i,1,QTableWidgetItem("tall"))
        if self.turn > 0 :
            self.bucket_m.setItem(i,2,QTableWidgetItem("헤이즐넛시럽 %d번바닐라시럽 %d번샷추가 %d번"% (self.bucket.count('헤이즐넛 시럽'),self.bucket.count('바닐라 시럽'),self.bucket.count('샷추가'))))
        if self.cof_m > 0 and self.ade_m == 0 and self.tea_m == 0:
            self.bucket_m.setItem(i,3,QTableWidgetItem("%d"% self.c_f))
        elif self.cof_m == 0 and self.ade_m > 0 and self.tea_m == 0:
            self.bucket_m.setItem(i,3,QTableWidgetItem("%d"% self.a_f))
            self.bucket_m.setItem(i, 0, QTableWidgetItem(self.menu_n.text()))
        elif self.cof_m == 0 and self.ade_m == 0 and self.tea_m > 0:
            self.bucket_m.setItem(i,3,QTableWidgetItem("%d"% self.t_f))

        cancel_button = QPushButton("취소")
        cancel_button.clicked.connect(self.on_cancel_clicked1)

        self.bucket_m.setCellWidget(i, 4, cancel_button)

        self.total_a += int(self.bucket_m.item(i,3).text())
        self.total_lb.setText("%d" % self.total_a)
        self.ta1.setRowCount(0)
        self.turn = 0
        self.cof_m = 0
        self.ade_m = 0
        self.tea_m = 0
        self.ice.setCheckable(False)
        self.hot.setCheckable(False)
        self.tall.setCheckable(False)
        self.venti.setCheckable(False)
        self.ice.setCheckable(True)
        self.hot.setCheckable(True)
        self.tall.setCheckable(True)
        self.venti.setCheckable(True)
        self.turn_m += 1
        self.bucket_g.setDisabled(True)
        m = self.bucket_m.rowCount()
        print(self.bucket_m.rowCount())
        if m < 1:
            self.purchase.setDisabled(True)
        else:
            self.purchase.setEnabled(True)

    # 결제 버튼
    def purchase_btn(self,a):
        self.stackedWidget.setCurrentIndex(a)
        for i in range(self.turn_m):
            self.receipt.insertRow(i)
            for j in range(4):
                bucket_a = self.bucket_m.item(i,j)
                if bucket_a:
                    self.receipt.setItem(i,j,QTableWidgetItem(bucket_a))
        self.total_lb_2.setText("%d" % self.total_a)



    #포인트적립버튼
    def point(self, text):
        if len(self.pointidn) < 13:
            self.pointidn += text
            if len(self.pointidn) == 3 or len(self.pointidn) == 8:
                self.pointidn +=("-")
            self.pointid.setText(self.pointidn)

        if len(self.pointidn) == 13:
            self.stampbtn.setEnabled(True)

    def cashf(self,a):
        user_id = self.pointid.text()
        cardl = len(user_id)
        if cardl > 0:
            # ID가 이미 테이블에 있는지 확인
            for row in range(self.pointid_2.rowCount()):
                if self.pointid_2.item(row, 0).text() == user_id:
                    # 이미 존재하는 ID라면 해당 행에 스탬프를 추가
                    self.stamp[user_id] += 1
                    self.pointid_2.setItem(row, 1, QTableWidgetItem(str(self.stamp.get(user_id, 0))))
                    self.stackedWidget.setCurrentIndex(5)  # 이 부분이 수정되었습니다.
                    self.pointid.clear()
                    self.pointidn = ''
                return

            # ID가 존재하지 않으면 새로운 행 추가
            row_position = self.pointid_2.rowCount()
            self.pointid_2.insertRow(row_position)
            self.pointid_2.setItem(row_position, 0, QTableWidgetItem(user_id))
            self.stamp[user_id] = 1
            self.pointid_2.setItem(row_position, 1, QTableWidgetItem(str(self.stamp.get(user_id, 0))))

            # 인풋 데이터 초기화
        self.pointid.clear()
        self.pointidn = ''

        # 페이지 이동
        self.stackedWidget.setCurrentIndex(a)

    def cal(self, c):
        if c == 1:
            self.pointid.clear()
            self.pointidn = ''
        else:
            self.pointid.setText(self.pointid.text()[:-1])
            self.pointidn = self.pointidn[:-1]
        self.stampbtn.setDisabled(True)

    # 카드결제
    def cardf(self):
        self.loading.show()
        #self.loading_bar.show()
        for j in range(101):
            self.loading.setValue(j)
            sleep(0.02)

        user_id = self.pointid.text()
        if user_id in self.stamp:
            self.stamp[user_id] += 1
            self.pointid_2.insertRow(0)
            self.pointid_2.setItem(0, 1, QTableWidgetItem(str(self.stamp.get(user_id, 0))))
            self.pointid_2.setItem(0, 0, QTableWidgetItem(user_id))

        else:
            if len(self.pointidn) == 13:
                self.stamp[user_id] = 0
                self.stamp[user_id] += 1
                self.pointid_2.insertRow(0)
                self.pointid_2.setItem(0, 1, QTableWidgetItem(str(self.stamp.get(user_id, 0))))
                self.pointid_2.setItem(0, 0, QTableWidgetItem(user_id))

        self.stackedWidget.setCurrentIndex(5)

    # 인풋 데이터 초기화
        self.pointid.clear()
        self.pointidn = ''
        self.loading.hide()

    def changenum(self,):
        self.stackedWidget.setCurrentIndex(0)
        self.line['번호표'] += 1  # 번호표 값 1씩 증가
        new_text = self.line['번호표']
        self.lineup.setText(str(new_text))
        # self.bucket_m.clearContents()
        self.bucket_m.setRowCount(0)
        self.total_a = 0
        self.total_lb.clear()
        self.total_lb_2.clear()
        self.turn_m = 0
        self.receipt.setRowCount(0)
        self.stampbtn.setDisabled(True)
        self.pointid_2.setRowCount(0)

    #현금 클리어
    def clear(self):
        self.stackedWidget.setCurrentIndex(0)
        self.total_lb.clear()
        self.bucket_m.setRowCount(0)
        self.receipt.setRowCount(0)
        self.total_lb_2.clear()
        self.pointid.clear()
        self.pointidn = ''

    def thiefbar(self):
        for j in range(101):
            self.progressBar.setValue(j)
            sleep(0.02)


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
